from .alert_rule import AlertRule
from .core.base_entity import BaseEntity
from .enum import AlertType
from .agent import Agent
from .test import Test


class Alert(BaseEntity):
    """A single instance for a single alert"""

    @property
    def id(self):
        """This is property to get alert ID 

        :return: value of "alertId" key
        :rtype: integer

        :example: for ThousandEyes alert object containing:
        {
            "alertId": 123456789
        }
        returns 123456789
        """
        return self._data.get('alertId')
    
    @property
    def activity_state(self):
        """This is property to get current state of alert
        0 for inactive, 1 for active, 2 for disabled. 
        Alert is disabled if either alert rule itself has been deleted or the test it is applied to has been disabled,
        deleted, disabled alerting, or disassociated the alert rule from the test

        :return: value of "active" key
        :rtype: integer
         
        :example: for ThousandEyes alert object containing:
        {
            "active": 0
        }
        returns 0
        """
        return self._data.get('active')

    @property
    def active(self):
        """This is property to check if alert is currently active

        :return: True if alert "active" key is 1
        :rtype: boolean

        example: for ThousandEyes alert object containing:
        {
            "active": 1
        }
        returns true
        """
        return self.activity_state == 1

    @property
    def inactive(self):
        """This is property to check if alert is currently inactive
        
        :return: True if alert "active" key is 0
        :rtype: boolean

        example: for ThousandEyes alert object containing:
        {
            "active": 0
        }
        returns true
        """
        return self.activity_state == 0

    @property
    def disabled(self):
        """This is property to check if alert is currently disabled
        Alert is disabled if either alert rule itself has been deleted or the test it is applied to has been disabled,
        deleted, disabled alerting, or disassociated the alert rule from the test
        
        :return: True if alert "active" key is 2
        :rtype: boolean

        example: for ThousandEyes alert object containing:
        {
            "active": 2
        }
        returns true
        """
        return self.activity_state == 2

    @property
    def rule_expression(self):
        """This is property to get rule expression that triggered the alert

        :return: value of "ruleExpression" key
        :rtype: string

        example: for ThousandEyes alert object containing:
        {
            "ruleExpression": "((responseTime >= 300 ms))"
        }
        returns "((responseTime >= 300 ms))"
        """
        return self._data.get('ruleExpression')

    @property
    def type(self):
        """This is property to get type of the alert
        
        :return: Enum name-value pair from AlertType class (refer to enum.py module) 
            original type value of alert object can be returned using "string_type" property
        :rtype: enum 'AlertType'
 
        example: for ThousandEyes alert object containing:
        {
            "type": "HTTP Server"
        }
        returns enum: <AlertType.HTTP_SERVER: 'HTTP Server'>
        to access enum name use: "alert.type.name" which returns string: "AlertType.HTTP_SERVER"
        to access enum value use: "alert.type.value" which returns string: "HTTP Server" (equivalent to 'string_type' property)
        """
        return AlertType.get(self._data.get('type'))

    @property
    def string_type(self):
        """This is property to get type of the alert
        
        :return: value of "type" key
        :rtype: string

        example: for ThousandEyes alert object containing:
        {
            "type": "HTTP Server"
        }
        returns "HTTP Server"
        """
        return self._data.get('type')

    @property
    def test_targets_description(self):
        """this key is not valid for alert object,
        testTargetsDescription exists in webhook alert object only
        This property will be deprecated in stable release        
        """
        return self._data.get('testTargetsDescription', [])

    @property
    def rule(self) -> AlertRule:
        """WARNING: this property is sending another API to /alert-rules endpoint
                 If you need to get just a ruleId then use 'rule_id' property instead
                 If you need to get rule object for the alert then use: "thousand_eyes.rules.get('alert.rule_id')"
                 This property will be deprecated in stable release

        :return: associated rule object
        :rtype: class 'thousandeyessdk.alert_rule.AlertRule'
        """
        return self._api.alert_rules.get(self._data.get('ruleId'))

    @property
    def rule_id(self):
        """This is property to get alert rule ID that triggered the alert

        :return: returns value of "ruleId" key
        :rtype: integer

        example: for ThousandEyes alert object containing:
        for object containing:
        {
            "ruleId": 555555
        }
        returns 555555
        """
        return self._data.get('ruleId')

    @property
    def test(self) -> Test:
        """WARNING: this property is sending another API to /tests endpoint
                 If you need to get just a ruleId then use 'test_id' property instead
                 If you need to get test object for the alert then use: "thousand_eyes.tests.get('alert.test_id')"
                 This property will be deprecated in stable release

        :return: associated test object
        :rtype: class 'thousandeyessdk.test.Test'
        """
        return self._api.tests.get(self._data.get('testId'))

    @property
    def test_id(self):
        """This is property to get test ID that alert was triggered for.

        :return: returns value of "testId" key
        :rtype: integer

        returns value of "testId" key
        example: for ThousandEyes alert object containing:
        {
            "testId": 4443322
        }
        returns 4443322
        """
        return self._data.get('testId')

    @property
    def date_start(self):
        """not supported currently
        """
        pass

    @property
    def date_end(self):
        """not supported currently
        """
        pass

    @property
    def violation_count(self):
        """This is property to get number of sources currently meeting the alert criteria

        :return: value of "violationCount" key
        :rtype: integer 

        example: for ThousandEyes alert object containing:
        {
            "violationCount": 2
        }
        returns 2
        """
        return self._data.get('violationCount')

    @property
    def permalink(self):
        """This is property to get hyperlink to alert

        :return: value of "permalink"
        :rtype: string
        
        example: for ThousandEyes alert object containing:
        {
            "permalink": "https://app.thousandeyes.com/alerts/list/?__a=333666&alertId=123456789"
        }
        returns "https://app.thousandeyes.com/alerts/list/?__a=333666&alertId=123456789"
        """
        return self._data.get('permalink')

    @property
    def agents(self):
        """This is property to get array of agents where the alert has at some point 
        been active since the point that the alert was triggered. Not shown on BGP alerts.
        if alert is BGP then empty list is returned

        :return: list of agents
        :rtype: list
        """
        return [agent_data for agent_data in self._data.get('agents',[])]

    @property
    def monitors(self):
        """This is property to get array of monitors where the alert has at some point been active since the point that the alert was triggered. Only shown on BGP alerts.
        if alert is not BGP then empty list is returned

        :return: list of monitors
        :rtype: list
        """
        return [monitor for monitor in self._data.get('monitors', [])]

    @property
    def api_links(self):
        """not supported currently
        """
        pass

    def __repr__(self):
        return f'<Alert id={self.id}>'
