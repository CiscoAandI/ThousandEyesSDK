from thousandeyessdk.alert import Alert

from . import ALERT


class TestAlert():

    def test_alert_id(self):
        alert = Alert('api', ALERT, '/alerts')
        assert alert.id == 123456789