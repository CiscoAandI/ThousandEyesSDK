from unittest.mock import Mock

import pytest

from thousandeyessdk.resources.webhooks import (
    WebhookNotFound,
    Webhooks,
)


@pytest.fixture
def api():
    return Mock()


@pytest.fixture
def webhooks(api):
    return Webhooks(api)


def test_get_id_by_name_webhook_found(webhooks, api):
    api.request.return_value = {
        "integrations": {
            "webhook": [
                {
                    "integrationId": "webhook1",
                    "integrationName": "Webhook 1",
                },
                {
                    "integrationId": "webhook2",
                    "integrationName": "Webhook 2",
                },
            ]
        }
    }
    res = webhooks.get_id_by_name("Webhook 1")
    assert res == "webhook1"


def test_get_id_by_name_webhook_not_found(webhooks, api):
    # Mock the API response
    api.request.return_value = {
        "integrations": {
            "webhook": [
                {
                    "integrationId": "webhook1",
                    "integrationName": "Webhook 1",
                },
                {
                    "integrationId": "webhook2",
                    "integrationName": "Webhook 2",
                },
            ]
        }
    }

    with pytest.raises(WebhookNotFound):
        webhooks.get_id_by_name("Webhook 3")
