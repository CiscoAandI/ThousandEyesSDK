from ..core.base_entity import BaseEntity
from .list_like import ListLike


class Dashboard(BaseEntity):
    @property
    def id(self):
        return self._data.get('dashboardId')

    @property
    def title(self):
        return self._data.get('title')


class Dashboards(ListLike):
    SINGULAR_CLASS = Dashboard
    ROUTE = '/dashboards'
    OBJECT_NAME = 'Dashboard'
    KEY = None


    def get(self, item_id: int):
        url = f'{self.ROUTE}/{item_id}'
        return self.SINGULAR_CLASS(
            self._api,
            self._api._request(url),
            url
        )
