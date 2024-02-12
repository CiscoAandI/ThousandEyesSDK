from unittest.mock import Mock

import pytest

from thousandeyessdk.resources.alert_rules import (
    AlertRuleDefinition,
    AlertRuleId,
    AlertRules,
    TestId,
)


@pytest.fixture
def api():
    return Mock()


@pytest.fixture
def alert_rules(api):
    return AlertRules(api)


def test_create_alert_rule(alert_rules, api):
    api.request.return_value = {"alertRuleId": 2345}

    definition = AlertRuleDefinition(
        alert_type="some-type",
        rule_name="my-rule",
        expression="(some expr>222)",
        test_ids=[TestId(id=10, type="http-server"), TestId(id=11, type="http-server")],
        minimum_sources=2,
        rounds_violating_required=8,
        rounds_violating_out_of=10,
        webhook_id="wb-333",
        severity="CRITICAL",
        notify_on_clear=1,
    )
    alert_rule_id = alert_rules.create(definition)

    assert alert_rule_id == 2345
    api.request.assert_called_with(
        "/alert-rules/new",
        method="POST",
        data={
            "alertType": "some-type",
            "ruleName": "my-rule",
            "expression": "(some expr>222)",
            "testIds": [10, 11],
            "minimumSources": 2,
            "roundsViolatingRequired": 8,
            "roundsViolatingOutOf": 10,
            "notifications": {
                "webhook": [
                    {"integrationId": "wb-333", "integrationType": "WEBHOOK"},
                ],
            },
            "severity": "CRITICAL",
            "notifyOnClear": 1,
        },
    )


def test_delete_alert_rule(alert_rules, api):
    alert_rule_id = AlertRuleId(58732)
    alert_rules.delete(alert_rule_id)

    api.request.assert_called_with("/alert-rules/58732/delete", method="POST")
