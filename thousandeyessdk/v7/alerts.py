from ..core.base_entity import BaseEntity
from .list_like import ListLikeListingClass


class AlertListing(BaseEntity):
    @property
    def id(self):
        return self._data.get('alertId')

    @property
    def type(self):
        return self._data.get('alertType')

    def __repr__(self):
        return f'<AlertListing id={self.id}, type={self.type}>'


class Alert(BaseEntity):
    @property
    def id(self):
        return self._data.get('alertId')

    @property
    def type(self):
        return self._data.get('alertType')

    @property
    def locations(self):
        return self._data.get('locations', [])

    def __repr__(self):
        return f'<Alert id={self.id}, type={self.type}>'


class Alerts(ListLikeListingClass):
    SINGULAR_CLASS = Alert
    LISTING_CLASS = AlertListing
    ROUTE = '/alerts'
    OBJECT_NAME = 'Alert'
    KEY = 'alerts'

    def get(self, alert_id: int, alert_type: str):
        url = f"{self.ROUTE}/{alert_type}/{alert_id}"
        result = self._api._request(url)
        return self.SINGULAR_CLASS(
            self._api,
            result,
            url
        )
