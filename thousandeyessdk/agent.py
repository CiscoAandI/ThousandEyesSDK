# https://developer.thousandeyes.com/v6/agents/#/agentid
from .core.base_entity import BaseEntity

class Agent(BaseEntity):
    """A single instance for a single agent"""

    def _get_detail(self) -> None:
        self._data |= self._api._request(f'/agents/{self.id}')['agents'][0]

    @property
    def id(self) -> int:
        """unique ID of the agent"""
        return self._data.get('agentId')

    @property
    def name(self) -> int:
        """unique name of the agent"""
        return self._data.get('agentName')

    def update(self, **data):
        # This is yet another really silly api design decision by the thousand eyes team.
        # No reason you need to POST to an /update route. This API is wonky.
        return self._api._request(method='POST', json=data, url=f'/agents/{self.id}/update')

    def delete(self):
        # This is a really silly api design decision. No reason you need to POST to a /delete route.
        return self._api._request(method='POST', url=f'/agents/{self.id}/delete')

    def __repr__(self):
        return f'<Agent id={self.id} name={self.name}>'
