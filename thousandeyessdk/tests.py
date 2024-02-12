from werkzeug.exceptions import BadRequest

from .core import BaseEntity, ListLike


class Test(BaseEntity):
    """A single instance for a single test"""

    def _get_details(self) -> dict:
        if self._details is None:
            return self._api._request(f"/tests/{self.id}")["test"][0]

        return self._details

    @property
    def id(self) -> int:
        """unique ID of the test"""
        return self._data.get("testId")

    @property
    def name(self) -> int:
        return self._data.get("testName")

    @property
    def agent_list(self):
        return self._data.get("agents")

    @property
    def interval(self):
        return self._data.get("interval")

    @property
    def labels(self) -> set[str]:
        details = self._get_details()
        groups = details.get("groups", [])
        names = [g["name"] for g in groups]
        return set(names)

    # this should be done in a way that informs user if there is no domain field
    @property
    def domain(self):
        return self._data.get("domain", None)

    @property
    def url(self):
        return self._data.get("url", None)

    @property
    def server(self):
        return self._data.get("server", None)

    @property
    def type(self) -> int:
        return self._data.get("type")

    @property
    def country_id(self):
        return self._data.get("countryId", None)

    def _get_test_data(self, url, object_key, list_key):
        try:
            for response in self._api._follow_pagination(url):
                for instance in response[object_key].get(list_key, []):
                    yield instance
        except BadRequest:
            return []

    def get_detailed_path_trace(self, agent_id, round_id):
        endpoint = f"/net/path-vis/{self.id}/{agent_id}/{round_id}"
        return self._get_test_data(endpoint, "net", "pathVis")

    def __repr__(self):
        return f"<Test id={self.id}>"


class Tests(ListLike):
    """
    A list-like class for handling tests
    """

    SINGULAR_CLASS = Test
    ROUTE = "/tests"
    KEY = "test"
    OBJECT_NAME = "Test"
