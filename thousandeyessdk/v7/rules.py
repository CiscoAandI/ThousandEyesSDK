from ..core import BaseEntity
from .list_like import ListLikeListingClass


class RuleListing(BaseEntity):

    @property
    def expression(self) -> str:
        return self._data.get("expression")


class Rule(RuleListing):
    pass


class Rules(ListLikeListingClass):
    SINGULAR_CLASS = Rule
    LISTING_CLASS = RuleListing
    ROUTE = "/alerts/rules"
    OBJECT_NAME = "Rule"
    KEY = "alertRules"

    def get(self, rule_id: int):
        url = f"{self.ROUTE}/{rule_id}"
        return self.SINGULAR_CLASS(self._api, self._api._request(url), url)
