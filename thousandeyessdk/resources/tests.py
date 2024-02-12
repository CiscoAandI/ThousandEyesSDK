import logging
from dataclasses import dataclass, field
from collections import namedtuple

LOG = logging.getLogger(__name__)

TestId = namedtuple("TestId", ["id", "type"])


@dataclass
class TestDefinition:
    name: str
    type: str = field(init=False)

    def asdict(self):
        return {
            "testName": self.name,
        }


@dataclass
class HTTPServerTest(TestDefinition):
    type: str = field(default="http-server", init=False)
    agents: list[int]
    interval: int
    url: str

    def asdict(self):
        base = super().asdict()
        data = {
            "agents": [{"agentId": id} for id in self.agents],
            "interval": self.interval,
            "url": self.url,
        }
        data.update(base)
        return data


class Tests:
    def __init__(self, api):
        self._api = api

    def create(self, definition: TestDefinition) -> TestId:
        url = f"/tests/{definition.type}/new"
        payload = definition.asdict()

        response = self._api.request(url, method="POST", data=payload)
        return TestId(id=response["test"][0]["testId"], type=definition.type)

    def delete(self, test_id: TestId):
        url = f"/tests/{test_id.type}/{test_id.id}/delete"
        self._api.request(url, method="POST")
