from .alert_rule import AlertRule
from .core.base_entity import BaseEntity
from .enum import AlertType


class Alert(BaseEntity):
    """A single instance for a single alert"""

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
