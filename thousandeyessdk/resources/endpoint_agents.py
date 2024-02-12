import logging
from dataclasses import dataclass

LOG = logging.getLogger(__name__)


@dataclass
class EndpointAgent:
    id: str
    name: str

    @classmethod
    def from_dict(self, data: dict) -> "EndpointAgent":
        return EndpointAgent(
            id=data["agentId"],
            name=data["agentName"],
        )


class EndpointAgents:
    def __init__(self, api):
        self._api = api

    def by_id(self, agent_id: int) -> EndpointAgent:
        url = f"/endpoint-agents/{agent_id}"

        details = self._api.request(url)["endpointAgents"][0]
        return EndpointAgent.from_dict(details)

    def by_ids(self, agent_ids: list[int]) -> list[EndpointAgent]:
        agents = map(self.by_id, agent_ids)
        return list(agents)
