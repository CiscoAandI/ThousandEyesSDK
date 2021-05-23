from .alert_rule import AlertRule
from .list_like import ListLike
    
class AlertRules(ListLike):
    """
    A list-like class for handling alert rules
    """
    SINGULAR_CLASS = AlertRule
    ROUTE = '/alert-rules'
    KEY = 'alertRules'
    OBJECT_NAME = 'Alert Rule'