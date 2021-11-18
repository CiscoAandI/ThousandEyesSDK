# https://developer.thousandeyes.com/v6/alerts/#/integrations

from .alert_notifications import AlertNotifications
from .core.base_entity import BaseEntity
from .enum import AlertRuleDirection, AlertType, RoundsViolatingMode
from .tests import Tests


class AlertRule(BaseEntity):
    """A single instance for a single alert rule"""

    def _get_detail(self) -> None:
        self._data |= self._api._request(f'/alert-rules/{self.id}')['alertRules'][0]

    @property
    def id(self) -> int:
        """unique ID of the alert rule"""
        return self._data.get('ruleId')

    @property
    def name(self) -> str:
        """name of the alert rule"""
        return self._data.get('ruleName')

    @property
    def expression(self) -> str:
        """string expression of alert rule"""
        return self._data.get('expression')

    @property
    def direction(self) -> AlertRuleDirection:
        """
        optional field with one of the following values: TO_TARGET, FROM_TARGET, BIDIRECTIONAL, for applicable
        alert types (eg. path trace, End-to-End (Agent) etc.)
        """
        return AlertRuleDirection.get(self._data.get('direction'))

    @property
    def notify_on_clear(self) -> bool:
        """1 to send notification when alert clears"""
        return self._data.get('notifyOnClear') == 1

    @property
    def default(self) -> bool:
        """
        Alert rules allow up to 1 alert rule to be selected as a default for each type.
        By checking the default option, this alert rule will be automatically included on subsequently created
        tests that test a metric used in alerting here.
        """
        return self._data.get('default') == 1

    @property
    def alert_type(self) -> AlertType:
        """type of alert rule, as determined by metric selection"""
        return AlertType.get(self._data.get('alertType'))

    @property
    def minimum_sources(self) -> int:
        """
        the minimum number of agents or monitors that must meet the specified criteria in order to trigger the alert
        """
        return self._data.get('minimumSources')

    @property
    def minimum_sources_percentage(self) -> int:
        """
        the minimum percentage of all assigned agents or monitors that must meet the specified
        criteria in order to trigger the alert
        """
        return self._data.get('minimumSourcesPct')

    @property
    def rounds_violating_mode(self) -> RoundsViolatingMode:
        """EXACT requires that the same agent(s) meet the threshold in consecutive rounds; default is ANY"""
        return RoundsViolatingMode.get(self._data.get('roundsViolatingMode'))

    @property
    def rounds_violating_out_of(self) -> int:
        """applies to only v6 and higher, specifies the divisor (y value) for the "X of Y times" condition."""
        return self._data.get('roundsViolatingOutOf')

    @property
    def rounds_violating_required(self) -> int:
        """applies to only v6 and higher, specifies the numerator (x value) for the "X of Y times" condition"""
        return self._data.get('roundsViolatingRequired')

    # The properties below require the detailed endpoint to be called

    @property
    def notifications(self) -> list[dict]:
        if 'notifications' not in self._data:
            self._get_detail()
        notifications = self._data.get('notifications')
        return AlertNotifications(self._api, notifications) if notifications else None

    @property
    def tests(self) -> list[dict]:
        if 'tests' not in self._data:
            self._get_detail()
        tests = self._data.get('tests')
        return Tests(self._api, tests) if tests else None

    def __repr__(self):
        return f'<AlertRule name={self.name}>'
