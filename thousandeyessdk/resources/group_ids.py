import dataclasses


@dataclasses.dataclass
class AccountGroupInList:
    aid: int
    account_group_name: str
    current: int
    default: int

    @classmethod
    def from_dict(cls, data: dict) -> "AccountGroupInList":
        return cls(
            aid=data["aid"],
            account_group_name=data["accountGroupName"],
            current=data["current"],
            default=data["default"],
        )


class Groups:
    def __init__(self, api):
        self._api = api

    def list(self) -> list[AccountGroupInList]:
        endpoint = "/account-groups"
        response = self._api.request(endpoint)
        groups = response["accountGroups"]
        return [AccountGroupInList.from_dict(data) for data in groups]
