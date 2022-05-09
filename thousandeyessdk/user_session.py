from .core.base_entity import BaseEntity


class UserSession(BaseEntity):
    """A single instance for a single user session"""

    @property
    def id(self):
        return self._data.get('userSessionId')

    @property
    def round_id(self) -> int:
        return self._data.get('roundId')

    @property
    def source_address(self):
        return self._data.get('sourceAddr')

    @property
    def agent_id(self):
        return self._data.get('agentId')

    @property
    def visited_site(self):
        return self._data.get('visitedSite')

    @property
    def experience_score(self):
        return self._data.get('experienceScore')

    @property
    def protocol(self):
        return self._data.get('protocol')

    @property
    def network(self):
        return self._data.get('network')

    def _get_detail(self) -> None:
        self._data |= self._api._request(f'/endpoint-data/user-sessions/{self.id}')['userSessions'][0]

    def __repr__(self):
        return f'<UserSession id={self.id}>'
