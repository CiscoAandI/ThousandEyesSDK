import warnings

from .agents import Agent
from .list_like import ListLikeListingClass
from ..core import BaseEntity


class AlertListing(BaseEntity):
    @property
    def id(self):
        return self._data.get("alertId")

    @property
    def type(self):
        return self._data.get("alertType")

    @property
    def date_start(self):
        return self._data.get("startDate")

    @property
    def date_end(self):
        return self._data.get("endDate")

    @property
    def test_id(self):
        test = self._data.get("_links", {}).get("test", {}).get("href")
        return int(test.split("/")[-1]) if test and "/" in test else None

    @property
    def violation_count(self):
        return self._data.get("violationCount")

    @property
    def permalink(self):
        return self._data.get("permalink")

    @property
    def severity(self):
        return self._data.get("severity")

    @property
    def state(self):
        return self._data.get("state")

    @property
    def active(self):
        return self.state == "ACTIVE"

    @property
    def api_links(self):
        return self._data.get("apiLinks")

    @property
    def links(self):
        return self._data.get("_links")

    @property
    def rule_id(self):
        return self._data.get("ruleId")

    def get_single(self) -> 'Alert':
        if self._details:
            return self._details
        path = f"/alerts/{self.id}"
        result = self._api._request(path)
        self._details = Alert(self._api, result, path)
        return self._details

    def __repr__(self):
        return f"<AlertListing id={self.id}, type={self.type}>"


class Alert(AlertListing):
    @property
    def locations(self):
        return self._data.get("locations", [])

    @property
    def details(self) -> list[Agent]:
        details = self.data.get("details", [])
        return [Agent(self._api, detail, f"/agents/{detail.get('id')}") for detail in details]

    def __repr__(self):
        return f"<Alert id={self.id}, type={self.type}>"


class Alerts(ListLikeListingClass):
    SINGULAR_CLASS = Alert
    LISTING_CLASS = AlertListing
    ROUTE = "/alerts"
    OBJECT_NAME = "Alert"
    KEY = "alerts"

    def get(self, alert_id: int, alert_type: str = ""):
        if alert_type:
            warnings.warn("Passing alert_type is redundant and will be removed soon")
        url = f"{self.ROUTE}/{alert_id}"
        result = self._api._request(url)
        return self.SINGULAR_CLASS(self._api, result, url)

    def list(self, query="", state="", start_date="", end_date="",
             window="", max_=""):
        q = []
        names = ["state", "startDate", "endDate", "window", "max"]
        values = [state, start_date, end_date, window, max_]
        for name, val in zip(names, values):
            if val and name not in query:
                q.append(f"{name}={val}")
        q = "&".join(q)
        if query and q:
            query = query + "&" + q
        return super().list(query)
