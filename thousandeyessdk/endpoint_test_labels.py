from .core import BaseEntity, ListLike


class EndpointTestLabel(BaseEntity):
    @property
    def id(self) -> int:
        return self._data["groupId"]

    @property
    def name(self) -> str:
        return self._data["name"]

    def _get_details(self) -> dict:
        if self._details is None:
            self._details = self._api._request(f"/groups/endpoint-tests/{self.id}")["groups"][0]

        return self._details

    @property
    def test_ids(self) -> set[int]:
        tests: list[dict] = self._get_details().get("endpointTests", [])
        ids = [t["testId"] for t in tests]
        return set(ids)


class EndpointTestLabels(ListLike):
    SINGULAR_CLASS = EndpointTestLabel
    ROUTE = "/groups/endpoint-tests"
    KEY = "groups"
    OBJECT_NAME = "Endpoint Test Labels"
