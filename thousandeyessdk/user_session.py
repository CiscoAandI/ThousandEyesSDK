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

    def _get_detail(self) -> None:
        self._data |= self._api._request(f'/endpoint-data/user-sessions/{self.id}')['userSessions'][0]

    def __repr__(self):
        return f'<UserSession id={self.id}>'
