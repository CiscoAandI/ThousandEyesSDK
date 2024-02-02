# https://developer.thousandeyes.com/v6/agents/#/agents
# https://developer.thousandeyes.com/v6/agents/#/agentid
from .core import BaseEntity, ListLike


class Agent(BaseEntity):
    """A single instance for a single agent"""

    def _get_detail(self) -> None:
        self._data |= self._api._request(f"/agents/{self.id}")["agents"][0]

    @property
    def id(self) -> int:
        """unique ID of the agent"""
        return self._data.get("agentId")

    @property
    def name(self) -> int:
        """unique name of the agent"""
        return self._data.get("agentName")

    @property
    def activity_state(self):
        return self._data.get("active")

    @property
    def active(self):
        return self.activity_state == 1

    @property
    def metrics_at_start(self):
        return self._data.get("metricsAtStart")

    @property
    def metrics_at_end(self):
        return self._data.get("metricsAtEnd")

    @property
    def date_start(self):
        return self._data.get("dateStart")

    @property
    def permalink(self):
        return self._data.get("permalink")

    @property
    def groups(self):
        return self._data.get("groups", [])

    @property
    def country_id(self):
        return self._data.get("countryId")

    @property
    def location(self):
        return self._data.get("location")

    @property
    def tests(self):
        from .tests import Tests

        all_tests: Tests = self._api.tests
        return [all_tests.get(test.get("testId")) for test in self._data.get("tests", [])]

    @property
    def group_names(self):
        return [group["name"] for group in self.groups]

    def update(self, **data):
        # This is yet another really silly api design decision by the thousand eyes team.
        # No reason you need to POST to an /update route. This API is wonky.
        return self._api._request(method="POST", json=data, url=f"/agents/{self.id}/update")

    def delete(self):
        # This is a really silly api design decision. No reason you need to POST to a /delete route.
        return self._api._request(method="POST", url=f"/agents/{self.id}/delete")

    def __repr__(self):
        return f"<Agent id={self.id} name={self.name}>"


class Agents(ListLike):
    """
    A list-like class for handling agents
    """

    SINGULAR_CLASS = Agent
    ROUTE = "/agents"
    KEY = "agents"
    OBJECT_NAME = "Agent"
