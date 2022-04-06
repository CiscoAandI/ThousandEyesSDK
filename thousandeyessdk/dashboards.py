#https://developer.thousandeyes.com/v7/dashboards/#/dashboards-list

from .list_like import ListLike
from .dashboard import Dashboard

class Dashboards(ListLike):
    """
    A list-like class for handling agents
    """
    SINGULAR_CLASS = Dashboard
    ROUTE = '/dashboards'
    KEY = None
    OBJECT_NAME = 'Dashboard'
