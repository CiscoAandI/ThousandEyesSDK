import dataclasses
from typing import Literal, Optional, Union, List

from thousandeyessdk.agents import Agent
from thousandeyessdk.tests import Test


@dataclasses.dataclass
class LabelGroupInList:
    group_id: int
    name: str
    type: str
    builtin: int

    @classmethod
    def from_dict(cls, data: dict) -> "LabelGroupInList":
        return cls(
            builtin=data["builtin"],
            group_id=data["groupId"],
            name=data["name"],
            type=data["type"],
        )


@dataclasses.dataclass
class LabelGroupDetails(LabelGroupInList):
    tests: Optional[list[Test]] = None
    agents: Optional[list[Agent]] = None
    endpoint_gents: Optional[list[dict]] = None
    endpoint_tests: Optional[list[dict]] = None
    dashboard_ids: Optional[list[int]] = None

    @classmethod
    def from_dict(cls, data: dict, api=None) -> "LabelGroupDetails":
        parsed = super().from_dict(data)
        if data.get("agents"):
            agents = [Agent(api, ag, "/agents") for ag in data.get("agents")]
            parsed.agents = agents
        if data.get("tests"):
            tests = [Test(api, ag, "/tests") for ag in data.get("tests")]
            parsed.tests = tests
        parsed.endpoint_tests = data.get("endpointTests")
        parsed.endpoint_gents = data.get("endpointAgents")
        parsed.dashboard_ids = data.get("dashboardIds")
        return parsed


class LabelGroups:
    def __init__(self, api):
        self._api = api

    def list(self,
             label_type: Optional[Literal["agents", "tests", "endpoint-agents", "endpoint-tests", "dashboards"]] = None,
             name: Optional[str] = None) -> \
            list[LabelGroupInList]:
        endpoint = "/groups"
        if label_type:
            endpoint = f"{endpoint}/{label_type}"
        response = self._api.request(endpoint)
        groups = response["groups"]
        results = [LabelGroupInList.from_dict(data) for data in groups]
        if name:
            return [group for group in results if group.name == name]
        return results

    def get(self,
            group_id: Optional[int] = None,
            group_name: Optional[str] = None,
            label_type: Optional[Literal["agents", "tests", "endpoint-agents", "endpoint-tests", "dashboards"]] = None) -> Optional[Union[List[LabelGroupDetails], LabelGroupDetails]]:
        endpoint = "/groups"
        if label_type:
            endpoint = f"{endpoint}/{label_type}"
        if group_name is None and group_id is None:
            raise ValueError("At least one group_id or group_name must be provided")
        if group_id:
            endpoint = f"{endpoint}/{group_id}"
        else:
            groups = self.list(label_type, group_name)
            if not groups:
                return None
            group_id = groups[0].group_id
            endpoint = f"{endpoint}/{group_id}"

        response = self._api.request(endpoint)
        results = [LabelGroupDetails.from_dict(rp, api=self._api)
                   for rp in response.get("groups")]
        if len(results) == 1:
            return results[0]
