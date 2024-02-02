from datetime import datetime

from .core import BaseEntity, ListLike


class UserSession(BaseEntity):
    """A single instance for a single user session"""

    @property
    def id(self):
        return self._data.get("userSessionId")

    @property
    def agent_id(self):
        return self._data.get("agentId")

    @property
    def visited_site(self):
        return self._data.get("visitedSite")

    @property
    def experience_score(self):
        return self._data.get("experienceScore")

    @property
    def protocol(self):
        return self._data.get("protocol")

    @property
    def network(self):
        return self._data.get("network")

    def load_details(self) -> None:
        self._get_detail()

    def _get_detail(self) -> None:
        self._data |= self._api._request(f"/endpoint-data/user-sessions/{self.id}")["userSessions"][0]

    def __repr__(self):
        return f"<UserSession id={self.id}>"


class UserSessions(ListLike):
    """
    A list-like class for handling user sessions
    """

    SINGULAR_CLASS = UserSession
    ROUTE = "/endpoint-data/user-sessions"
    KEY = "userSessions"
    OBJECT_NAME = "UserSession"

    def get_sessions_for_agents(self, agent_ids: set[str], timestamp: datetime) -> list[UserSession]:
        sessions = self._get_sessions_from(timestamp)
        return [s for s in sessions if s.agent_id in agent_ids]

    def get_sessions_for_domains(self, domains: set[str], timestamp: datetime) -> list[UserSession]:
        sessions = self._get_sessions_from(timestamp)
        return [s for s in sessions if s.visited_site in domains]

    def _get_sessions_from(self, timestamp: datetime) -> list[UserSession]:
        return list(self.list(query=f"from={timestamp}"))
