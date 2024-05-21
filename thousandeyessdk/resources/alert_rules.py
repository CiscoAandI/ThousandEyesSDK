import logging
from dataclasses import dataclass
from typing import NewType

from .tests import TestId

LOG = logging.getLogger(__name__)

AlertRuleId = NewType("AlertRuleId", int)


@dataclass
class AlertRuleDefinition:
    alert_type: str
    rule_name: str
    expression: str
    test_ids: list[TestId]
    minimum_sources: int
    rounds_violating_required: int
    rounds_violating_out_of: int
    webhook_id: str
    severity: str = "INFO"
    notify_on_clear: int = 0

    def asdict(self):
        if not self.webhook_id:
            notifications = {}
        else:
            notifications = {
                "webhook": [
                    {"integrationId": self.webhook_id, "integrationType": "WEBHOOK"},
                ],
            }
        return {
            "alertType": self.alert_type,
            "ruleName": self.rule_name,
            "expression": self.expression,
            "testIds": [test_id.id for test_id in self.test_ids],
            "minimumSources": self.minimum_sources,
            "roundsViolatingRequired": self.rounds_violating_required,
            "roundsViolatingOutOf": self.rounds_violating_out_of,
            "notifications": notifications,
            "severity": self.severity,
            "notifyOnClear": self.notify_on_clear,
        }


class AlertRules:
    def __init__(self, api):
        self._api = api

    def create(self, alert_rule_definition: AlertRuleDefinition) -> AlertRuleId:
        url = "/alert-rules/new"
        payload = alert_rule_definition.asdict()

        response = self._api.request(url, method="POST", data=payload)
        return response["alertRuleId"]

    def delete(self, alert_rule_id: AlertRuleId):
        url = f"/alert-rules/{alert_rule_id}/delete"
        self._api.request(url, method="POST")
