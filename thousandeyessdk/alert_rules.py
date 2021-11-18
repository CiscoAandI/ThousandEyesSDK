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

    def create(self, name, **data):
        """
        Example Call: (
            name='foo',
            roundsViolatingOutOf=1,
            expression='(((responseCode < 200) || (responseCode >= 300)))',
            alertType='HTTP Server',
            roundsViolatingRequired=1,
            minimumSourcesPct=30
        )
        Example response: {
            'alertRuleId': 1451249,
            'alertType': 'HTTP Server',
            'ruleName': 'foo',
            'expression': '(((responseCode < 200) || (responseCode >= 300)))',
            'minimumSourcesPct': 30,
            'roundsViolatingRequired': 1,
            'roundsViolatingOutOf': 1
        }
        """
        result = self._api._request(method='POST', url=self.ROUTE + '/new', json={
            'ruleName': name,
            **data
        })
        # Thousand eyes API is inconsistent with their key names. So we need to change "alertRuleId" to "ruleId" to be
        # consumable by the alert rule class
        result['ruleId'] = result['alertRuleId']
        del result['alertRuleId']
        return AlertRule(self._api, result)
