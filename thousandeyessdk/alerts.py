from . import API
from .alert import Alert
from .list_like import ListLike


class Alerts(ListLike):
    """
    A list-like class for handling alert generation and pagination
    """
    SINGULAR_CLASS = Alert
    ROUTE = '/alerts'
    OBJECT_NAME = 'Alert'

    @staticmethod
    def create(api: API) -> "Alerts":
        if api.version == 7:
            return AlertsV7(api)
        return AlertsV6(api)


class AlertsV6(Alerts):
    KEY = 'alert'


class AlertsV7(Alerts):
    KEY = 'alerts'

    def get(self, alert_id: int, alert_type: str):
        url = f"{self.ROUTE}/{alert_type}/{alert_id}"
        result = self._api._request(url)
        return self.SINGULAR_CLASS(
            self._api,
            result,
            url
        )
