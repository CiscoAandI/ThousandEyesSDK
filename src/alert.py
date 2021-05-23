# From thousand eyes api docs
# |----------------|--------------------------|---------------------|--------|
# |     field      |         data type        |       units         |  notes |
# | alertId        | integer                  | n/a                 | unique ID of the alert; each alert occurrence is assigned a new unique ID
# | testId         | integer                  | n/a                 | unique ID of the test (see /tests/{testId} endpoint for more detail)
# | ruleId         | integer                  | n/a                 | unique ID of the alert rule (see /alert-rules endpoint for more detail)
# | testName       | string                   | n/a                 | name of the test
# | active         | integer                  | n/a                 | 0 for inactive, 1 for active, 2 for disabled. Alert is disabled if either alert rule itself has been deleted or the test it is applied to has been disabled, deleted, disabled alerting, or disassociated the alert rule from the test
# | ruleExpression | string                   | n/a                 | string expression of alert rule
# | dateStart      | dateTime                 | yyyy-MM-dd hh:mm:ss | the date/time where an alert rule was triggered, expressed in UTC
# | dateEnd        | dateTime                 | yyyy-MM-dd hh:mm:ss | the date/time where the alert was marked as cleared, expressed in UTC
# | violationCount | integer                  | n/a                 | number of sources currently meeting the alert criteria
# | ruleName       | string                   | n/a                 | name of the alert rule
# | permalink      | string                   | n/a                 | hyperlink to alerts list, with row expanded
# | type           | string                   | n/a                 | type of alert being triggered
# | agents         | array of agent objects   | n/a                 | array of monitors where the alert has at some point been active since the point that the alert was triggered. Not shown on BGP alerts.
# | monitors       | array of monitor objects | n/a                 | array of monitors where the alert has at some point been active since the point that the alert was triggered. Only shown on BGP alerts.
# | apiLinks       | array of links           | n/a                 | list of hyperlinks to other areas of the API

from .enum import AlertType
from .alert_rule import AlertRule

class Alert:
    """A single instance for a single alert"""
    def __init__(self, api, data):
        self._api = api
        self._data = data
    
    @property
    def id(self):
        return self._data.get('alertId')
    
    @property
    def activity_state(self):
        return self._data.get('active')
    
    @property
    def active(self):
        return self.activity_state == 1
    
    @property
    def inactive(self):
        return self.activity_state == 0
    
    @property
    def disabled(self):
        return self.activity_state == 2
    
    @property
    def type(self):
        return AlertType.get(self._data.get('type'))
    
    @property
    def rule(self) -> AlertRule:
        return self._api.alert_rules.get(self._data.get('ruleId'))
    
    @property
    def test(self):
        return self._api.tests.get(self._data.get('testId'))
    
    @property
    def date_start(self):
        pass
    
    @property
    def date_end(self):
        pass
    
    @property
    def violation_count(self):
        pass
    
    @property
    def permalink(self):
        pass
    
    @property
    def agents(self):
        pass
    
    @property
    def monitors(self):
        pass
    
    @property
    def api_links(self):
        pass
    
    def __repr__(self):
        return f'<Alert id={self.id}>'