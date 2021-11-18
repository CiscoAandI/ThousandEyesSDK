from .alert import Alert
from .list_like import ListLike


class Alerts(ListLike):
    """
    A list-like class for handling alert generation and pagination
    """
    SINGULAR_CLASS = Alert
    ROUTE = '/alerts'
    KEY = 'alert'
    OBJECT_NAME = 'Alert'
