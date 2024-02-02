from unittest.mock import Mock

import pytest

from thousandeyessdk.resources.group_ids import (
    AccountGroupInList,
    Groups,
)


@pytest.fixture
def api():
    return Mock()


@pytest.fixture
def webhooks(api):
    return Groups(api)


def test_list_groups(webhooks, api):
    api.request.return_value = {
        "accountGroups": [{"accountGroupName": "API Sandbox", "aid": 75, "current": 1, "default": 1}]
    }
    assert webhooks.list() == [AccountGroupInList(75, "API Sandbox", 1, 1)]
