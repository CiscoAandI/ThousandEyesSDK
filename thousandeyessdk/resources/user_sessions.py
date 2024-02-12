import logging
from dataclasses import dataclass
from datetime import datetime
from typing import Optional

LOG = logging.getLogger(__name__)


@dataclass
class UserSession:
    id: str
    agent_id: str
    visited_site: str
    protocol: str
    experience_score: Optional[float]
    network: dict

    @classmethod
    def from_dict(self, data: dict) -> "UserSession":
        return UserSession(
            id=data["userSessionId"],
            agent_id=data["agentId"],
            visited_site=data["visitedSite"],
            protocol=data["protocol"],
            experience_score=data.get("experienceScore"),
            network=data["network"],
        )


class UserSessions:
    def __init__(self, api):
        self._api = api

    def by_id(self, session_id: int) -> UserSession:
        url = f"/endpoint-data/user-sessions/{session_id}"

        details = self._api.request(url)["userSessions"][0]
        return UserSession.from_dict(details)

    def all_since(self, timestamp: datetime) -> list[UserSession]:
        list_url = f"/endpoint-data/user-sessions?from={timestamp}"
        listing = self._api.request(list_url)
        ids = map(lambda g: g["userSessionId"], listing["userSessions"])
        sessions = map(self.by_id, ids)
        return list(sessions)

    def for_agents(self, agent_ids: set[int], timestamp: datetime) -> list[UserSession]:
        sessions = self.all_since(timestamp)
        matching_sessions = filter(lambda s: s.agent_id in agent_ids, sessions)
        return list(matching_sessions)

    def for_domains(self, domains: set[str], timestamp: datetime) -> list[UserSession]:
        sessions = self.all_since(timestamp)
        matching_sessions = filter(lambda s: s.visited_site in domains, sessions)
        return list(matching_sessions)
