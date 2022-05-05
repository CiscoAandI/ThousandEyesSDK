from unittest import TestCase
from unittest.mock import patch
from thousandeyessdk import ThousandEyes as TE

from . import ALERT_LIST, USERNAME, AUTH_TOKEN


class TestAlerts(TestCase):

    @patch('thousandeyessdk.requests.request')
    def test_alerts_ids(self, m__request):
        m__request().json.return_value = ALERT_LIST
        m__request().ok = True

        te_client = TE(username=USERNAME, auth_token=AUTH_TOKEN)

        alerts = te_client.alerts.list()
        alert_ids = [alert.id for alert in alerts]
        
        assert alert_ids == [111111111, 444444444]
