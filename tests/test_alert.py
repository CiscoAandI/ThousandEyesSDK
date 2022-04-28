from thousandeyessdk.alert import Alert
from thousandeyessdk.enum import AlertType

from . import ALERT


class TestAlert():

    def test_alert_id(self):
        alert = Alert('api', ALERT, '/alerts')
        assert alert.id == 123456789

    def test_active(self):
        alert = Alert('api', ALERT, '/alerts')
        assert alert.active == False
    
    def test_inactive(self):
        alert = Alert('api', ALERT, '/alerts')
        assert alert.inactive == True
    
    def test_disabled(self):
        alert = Alert('api', ALERT, '/alerts')
        assert alert.disabled == False
    
    def test_rule_expression(self):
        alert = Alert('api', ALERT, '/alerts')
        assert alert.rule_expression == "((responseTime >= 300 ms))"
 
    def test_type(self):
        alert = Alert('api', ALERT, '/alerts')
        assert alert.type.value == "HTTP Server"
        assert alert.type.name == "HTTP_SERVER"
        assert alert.type == AlertType("HTTP Server")

    def test_string_type(self):
        alert = Alert('api', ALERT, '/alerts')
        assert alert.string_type == "HTTP Server"

    def test_date_start(self):
        """date_start not supported currently"""
        alert = Alert('api', ALERT, '/alerts')
        assert alert.date_start == None

    def test_date_end(self):
        """not supported currently"""
        alert = Alert('api', ALERT, '/alerts')
        assert alert.date_end == None



    