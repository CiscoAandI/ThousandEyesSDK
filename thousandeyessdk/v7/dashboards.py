from ..core import BaseEntity
from .list_like import ListLike
from typing import List
from itertools import chain


DASHBOARD_UI_URL = "https://app.thousandeyes.com/dashboard/?dashboardId="

class Dashboard(BaseEntity):
    @property
    def id(self):
        return self._data.get("dashboardId")

    @property
    def title(self):
        return self._data.get("title")

    def __repr__(self):
        return f"<Dashboard id={self.id} title={self.title}>"

    def is_for_test(self, test_name: str) -> bool:
        filters = [w.get('filter') for w in self.widgets]
        filter_entries = [f.get('filters', []) for f in filters if f is not None]
        filter_entries = chain.from_iterable(filter_entries)
        test_name_filters = [f for f in filter_entries if f.get('key') == 'Test Name']
        test_names = [f.get('value') for f in test_name_filters]
        return test_name in test_names

    @property
    def url(self) -> str:
        return DASHBOARD_UI_URL + self.id

    @property
    def widgets(self) -> List[dict]:
        return self._data.get("widgets", [])


class Dashboards(ListLike):
    SINGULAR_CLASS = Dashboard
    ROUTE = "/dashboards"
    OBJECT_NAME = "Dashboard"
    KEY = None

    def get(self, item_id: int):
        url = f"{self.ROUTE}/{item_id}"
        return self.SINGULAR_CLASS(self._api, self._api._request(url), url)

    def all(self) -> List[Dashboard]:
        dashboards = self._api._request(self.ROUTE)
        ids = [d["dashboardId"] for d in dashboards]

        detailed_dashboards = [self.get(dashboard_id) for dashboard_id in ids]
        return detailed_dashboards
        
    def links_for_test(self, test_name: str) -> List[str]:
        detailed_dashboards = self.all()
        relevant_dashboards = filter(lambda d: d.is_for_test(test_name), detailed_dashboards)
        links = [d.url for d in relevant_dashboards if d.url is not None]
        return links

