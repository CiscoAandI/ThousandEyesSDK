from unittest import TestCase
from unittest.mock import patch
from thousandeyessdk import ThousandEyes as TE
from thousandeyessdk.enum import AlertType

from . import ALERT_WITH_AGENTS, ALERT_WITH_MONITORS, USERNAME, AUTH_TOKEN, URL, USERNAME

@patch('thousandeyessdk.requests.request')
class TestAlert(TestCase):
    def test_alert_with_agents(self, response_mock):
        response_mock().json.return_value = ALERT_WITH_AGENTS
        response_mock().ok=True
        te_client = TE(username=USERNAME, auth_token=AUTH_TOKEN)
        alert = te_client.alerts.get(ALERT_WITH_AGENTS['alert'][0]['alertId'])
        assert alert.id == 111111111
        assert alert.active == False
        assert alert.inactive == True
        assert alert.disabled == False
        assert alert.rule_expression == "((responseTime >= 300 ms))"
        assert alert.type.value == "HTTP Server"
        assert alert.type.name == "HTTP_SERVER"
        assert alert.type == AlertType("HTTP Server")
        assert alert.string_type == "HTTP Server"
        assert alert.date_start == None # date_start not supported currently
        assert alert.date_end == None #d ate_end not supported currently
        assert alert.violation_count == 2
        assert alert.permalink == "https://app.thousandeyes.com/alerts/list/?__a=333666&alertId=111111111"
        agent_names = [name['agentName'] for name in alert.agents]
        assert agent_names == ['AGENT1', 'AGENT2']
        assert alert.api_links == None #api_links not supported currently

    def test_alert_with_monitors(self,response_mock):
        response_mock().json.return_value = ALERT_WITH_MONITORS
        response_mock().ok=True
        te_client = TE(username=USERNAME, auth_token=AUTH_TOKEN)
        alert = te_client.alerts.get(ALERT_WITH_MONITORS['alert'][0]['alertId'])
        monitor_names = [name['monitorName'] for name in alert.monitors]
        assert monitor_names == ['Sydney-1', 'Los Angeles, CA', 'Geneva']




