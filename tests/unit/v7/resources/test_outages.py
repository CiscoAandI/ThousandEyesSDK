from unittest.mock import Mock

import pytest

from thousandeyessdk.v7.resources import Outages


@pytest.fixture
def api():
    return Mock()


@pytest.fixture
def outages(api):
    return Outages(api)


def test_list(api: Mock, outages: Outages):
    outage_id = "some-dashboard-id"
    api.request.return_value = {
        "outages": [
            {
                "id": outage_id,
                "type": "app",
            }
        ]
    }

    outages = outages.list(outage_id)
    assert len(outages) == 1
    assert outages[0]["id"] == outage_id
    assert outages[0]["type"] == "app"


def test_get(api: Mock, outages: Outages):
    outage_id = "some-dashboard-id"
    api.request.return_value = {
        "id": outage_id,
        "type": "app",
    }

    outage = outages.get("app", outage_id)
    assert outage["id"] == outage_id
    assert outage["type"] == "app"
