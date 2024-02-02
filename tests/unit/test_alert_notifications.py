from unittest import TestCase
from unittest.mock import patch

import stringcase

from thousandeyessdk.alert_notifications import IntegrationsList, WebhookIntegrationList
from thousandeyessdk.clients import ThousandEyes as TE
from . import AUTH_TOKEN, INTEGRATIONS, USERNAME

search_attrs = [
    (
        "target",
        "customer_name=ACME",
        ["https://webhooker.example.com/alert/z126g4a3f2a?version=0.0.1&customer_name=ACME&workflow_name=vip"],
    ),
    (
        "target",
        "customer_name=TEST_CUSTOMER",
        [
            (
                "https://webhooker.example1.com/alert/z126g4a3f2a?"
                "version=0.0.1&customer_name=TEST_CUSTOMER&workflow_name=vip"
            )
        ],
    ),
    (
        "target",
        "workflow_name=vip",
        [
            "https://webhooker.example.com/alert/z126g4a3f2a?version=0.0.1&customer_name=ACME&workflow_name=vip",
            (
                "https://webhooker.example1.com/alert/z126g4a3f2a?"
                "version=0.0.1&customer_name=TEST_CUSTOMER&workflow_name=vip"
            ),
        ],
    ),
]


def check_integration(obj, data: dict):
    for key, expected in data.items():
        key = key.replace("integration", "")
        present = getattr(obj, stringcase.snakecase(key))
        if key == "Type":
            present = present.value

        assert present == expected


@patch("thousandeyessdk.clients.requests.request")
def get_webhooks(m__request):
    m__request().json.return_value = INTEGRATIONS
    te_client = TE(username=USERNAME, auth_token=AUTH_TOKEN)
    return te_client.integrations.webhooks


class TestIntegrationList(TestCase):
    def test_search_by_name(self):
        data = IntegrationsList(get_webhooks())
        result = data.get_by_name("Alert ThousandEyes")
        assert len(result) == 2
        assert result[0].name == "Alert ThousandEyes"

    def test_search_by_id(self):
        data = IntegrationsList(get_webhooks())
        result = data.get_by_id("wb-4563")
        assert len(result) == 1
        assert result[0].id == "wb-4563"

    def test_search_by_query(self):
        data = IntegrationsList(get_webhooks())
        for attr_name, query, expected_results in search_attrs:
            with self.subTest():
                results = data.search_by_query("target", query)
                self.assertEqual(expected_results, [getattr(result, attr_name) for result in results])


class TestWebhookIntegrationList(TestCase):
    def test_search_by_target(self):
        data = WebhookIntegrationList(get_webhooks())
        results = data.get_by_target(customer_name="ACME")
        self.assertEqual(len(results), 1)
        self.assertEqual(
            "https://webhooker.example.com/alert/z126g4a3f2a?version=0.0.1&customer_name=ACME&workflow_name=vip",
            results[0].target,
        )


@patch("thousandeyessdk.clients.requests.request")
class TestAlert(TestCase):
    def test_get_webhooks_and_third_party(self, m__request):
        m__request().json.return_value = INTEGRATIONS
        te_client = TE(username=USERNAME, auth_token=AUTH_TOKEN)
        assert isinstance(te_client.integrations.third_party, IntegrationsList)
        assert isinstance(te_client.integrations.webhooks, WebhookIntegrationList)
        [
            check_integration(integration, data)
            for integration, data in zip(te_client.integrations.third_party, INTEGRATIONS["integrations"]["thirdParty"])
        ]
        [
            check_integration(integration, data)
            for integration, data in zip(te_client.integrations.webhooks, INTEGRATIONS["integrations"]["webhook"])
        ]
