from dataclasses import dataclass
from typing import Optional
from itertools import chain

DASHBOARD_UI_URL = "https://app.thousandeyes.com/dashboard/?dashboardId="


@dataclass
class Dashboard:
    id: str
    widgets: list[dict]

    @classmethod
    def from_dict(cls, data: dict) -> "Dashboard":
        return cls(id=data["id"], widgets=data["widgets"])

    def is_for_test(self, test_name: str) -> bool:
        # take dataComponents list from each widget
        data_components = chain.from_iterable(map(lambda w: w.get("dataComponents", []), self.widgets))
        data_components = list(data_components)
        # print(data_components)
        # take "filter" dict from each dataComponent
        filters = map(lambda c: c.get("filter"), data_components)
        # remove nones from dicts list
        filters = filter(lambda f: f is not None, filters)
        filters = list(filters)
        # print(filters)
        # get actual filter values from "filters" key
        filter_entries = chain.from_iterable(map(lambda f: f.get("filters", []), filters))
        # take only filters with key value "Test Name"
        test_name_filters = filter(lambda f: f.get("key") == "Test Name", filter_entries)
        test_name_filters = list(test_name_filters)
        # get the actual test names
        test_names = map(lambda f: f.get("value"), test_name_filters)
        return test_name in test_names

    @property
    def url(self) -> Optional[str]:
        return DASHBOARD_UI_URL + self.id


class Dashboards:
    def __init__(self, api):
        self._api = api

    def by_id(self, id: str) -> Dashboard:
        endpoint = f"/dashboards/{id}"
        response = self._api.request(endpoint)
        data = response["dashboards"][0]
        return Dashboard.from_dict(data)

    def all(self) -> list[Dashboard]:
        endpoint = "/dashboards"
        response = self._api.request(endpoint)

        dashboards = response["dashboards"]
        ids = map(lambda d: d["id"], dashboards)

        detailed_dashboards = map(self.by_id, ids)
        return list(detailed_dashboards)

    def links_for_test(self, test_name: str) -> list[str]:
        dashboards = self.all()
        dashboards = filter(lambda d: d.is_for_test(test_name), dashboards)
        links = map(lambda d: d.url, dashboards)
        links = filter(lambda l: l is not None, links)
        return list(links)
