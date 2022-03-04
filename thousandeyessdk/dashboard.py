# https://developer.thousandeyes.com/v7/dashboards/#/dashboards-list
from .core.base_entity import BaseEntity

class Dashboard(BaseEntity):
    """A single instance for a single dashboard"""

    def _get_detail(self) -> None:
        self._data |= self._api._request(f'/dashboards/{self.id}')['dashboards'][0]

    @property
    def id(self) -> int:
        """unique ID of the dashboards"""
        return self._data.get('dashboardId')

    @property
    def title(self) -> int:
        """title of the agent"""
        return self._data.get('title')

    def __repr__(self):
        return f'<Dashboard id={self.id} title={self.title}>'
