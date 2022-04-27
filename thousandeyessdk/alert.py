from .alert_rule import AlertRule
from .core.base_entity import BaseEntity
from .enum import AlertType
from .agent import Agent
from .test import Test


class Alert(BaseEntity):
    """single instance for a single alert"""

    @property
    def id(self):
        """
        returns value of "alertId" key, 
        for object containing:
        {
            "alertId": 123456789
        }
        returns integer: 123456789
        """
        return self._data.get('alertId')
    
    @property
    def activity_state(self):
        """
        returns value of "active" key,
        0 for inactive, 1 for active, 2 for disabled. 
        Alert is disabled if either alert rule itself has been deleted or the test it is applied to has been disabled,
        deleted, disabled alerting, or disassociated the alert rule from the test 
        for object containing:
        {
            "active": 0
        }
        returns integer: 0
        """
        return self._data.get('active')

    @property
    def active(self):
        """
        returns true if alert "active" key is 1, 
        for object containing:
        {
            "active": 1
        }
        returns boolean: true
        """
        return self.activity_state == 1

    @property
    def inactive(self):
        """
        returns true if alert "active" key is 0,   
        for object containing:
        {
            "active": 0
        }
        returns boolean: true
        """
        return self.activity_state == 0

    @property
    def disabled(self):
        """
        returns true if alert "active" key is 2,   
        for object containing:
        {
            "active": 2
        }
        returns boolean: true
        """
        return self.activity_state == 2

    @property
    def rule_expression(self):
        """
        returns value of "ruleExpression" key, 
        for object containing:
        {
            "ruleExpression": "((responseTime >= 300 ms))"
        }
        returns string: ((responseTime >= 300 ms))
        """
        return self._data.get('ruleExpression')

    @property
    def type(self):
        """
        returns Enum name-value pair from AlertType class, refer to enum.py module
        original type value of alert object can be returned using "string_type" property
        for object containing:
        {
            "type": "HTTP Server"
        }
        returns enum: <AlertType.HTTP_SERVER: 'HTTP Server'>
        to access enum name use: "alert.type.name" which returns string: "AlertType.HTTP_SERVER"
        to access enum value use: "alert.type.value" which returns string: "HTTP Server" (equivalent to 'string_type' property )
        """
        return AlertType.get(self._data.get('type'))

    @property
    def string_type(self):
        """
        returns value of "type" key, 
        for object containing:
        {
            "type": "HTTP Server"
        }
        returns string: "HTTP Server"
        """
        return self._data.get('type')

    @property
    def test_targets_description(self):
        """
        this key is not valid for alert object,
        testTargetsDescription exists in webhook alert object only
        ticket SSE-1527 opened to remove it
        """
        return self._data.get('testTargetsDescription', [])

    @property
    def rule(self) -> AlertRule:
        """
        returns associated rule object
        WARNING: this property is sending another API to /alert-rules endpoint
                 If you need to get just a ruleId then use 'rule_id' property instead
                 If you need to get rule object for the alert then use: "thousand_eyes.rules.get('alert.rule_id')"
                 This property will be deprecated in stable release
        """
        return self._api.alert_rules.get(self._data.get('ruleId'))

    @property
    def rule_id(self):
        """
        returns value of "ruleId" key, 
        for object containing:
        {
            "ruleId": 555555
        }
        returns integer: 555555
        """
        return self._data.get('ruleId')

    @property
    def test(self) -> Test:
        """
        returns test associated test object
        WARNING: this property is sending another API to /tests endpoint
                 If you need to get just a ruleId then use 'test_id' property instead
                 If you need to get test object for the alert then use: "thousand_eyes.tests.get('alert.test_id')"
                 This property will be deprecated in stable release
        """
        return self._api.tests.get(self._data.get('testId'))

    @property
    def test_id(self):
        """
        returns value of "testId" key, 
        for object containing:
        {
            "testId": 4443322
        }
        returns integer: 4443322
        """
        return self._data.get('testId')

    @property
    def date_start(self):
        pass

    @property
    def date_end(self):
        pass

    @property
    def violation_count(self):
        """
        returns value of "violationCount" key which is,
        number of sources currently meeting the alert criteria
        for object containing:
        {
            "violationCount": 2
        }
        returns integer: 2
        """
        return self._data.get('violationCount')

    @property
    def permalink(self):
        """
        returns value of "permalink" key which is,
        hyperlink to alerts list, with row expanded
        for object containing:
        {
            "permalink": "https://app.thousandeyes.com/alerts/list/?__a=333666&alertId=123456789"
        }
        returns string: "https://app.thousandeyes.com/alerts/list/?__a=333666&alertId=123456789"
        """
        return self._data.get('permalink')

    @property
    def agents(self):
        """
        returns list of agents
        array of agents where the alert has at some point been active since the point that the alert was triggered. Not shown on BGP alerts.
        if alert is BGP then empty list is returned
        """
        return [agent_data for agent_data in self._data.get('agents',[])]

    @property
    def monitors(self):
        """
        returns list of monitors
        array of monitors where the alert has at some point been active since the point that the alert was triggered. Only shown on BGP alerts.
        if alert is not BGP then empty list is returned
        """
        return [monitor for monitor in self._data.get('monitors', [])]

    @property
    def api_links(self):
        """
        not supported currently
        """
        pass

    def __repr__(self):
        return f'<Alert id={self.id}>'
