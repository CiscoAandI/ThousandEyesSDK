from unittest.mock import Mock

import pytest

from thousandeyessdk.resources.label_groups import (
    LabelGroups,
    LabelGroupDetails,
    LabelGroupInList
)


@pytest.fixture
def api():
    return Mock()


@pytest.fixture
def webhooks(api):
    return LabelGroups(api)


def test_list_groups(webhooks, api):
    api.request.return_value = {
        "groups": [
            {
                "name": "Infrastructure tests",
                "groupId": 961,
                "type": "tests",
                "builtin": 0
            },
        ]
    }
    assert webhooks.list() == [LabelGroupInList(961, "Infrastructure tests", "tests", 0)]
    api.request.assert_called_once_with("/groups")


def test_list_groups_with_type(webhooks, api):
    api.request.return_value = {
        "groups": [
            {
                "name": "Infrastructure tests",
                "groupId": 961,
                "type": "agents",
                "builtin": 0
            },
        ]
    }
    assert webhooks.list(label_type="agents") == [LabelGroupInList(961, "Infrastructure tests", "agents", 0)]
    api.request.assert_called_once_with("/groups/agents")


def test_list_groups_search_by_name(webhooks, api):
    api.request.return_value = {
        "groups": [
            {
                "name": "Infrastructure tests",
                "groupId": 961,
                "type": "tests",
                "builtin": 0
            },
            {
                "name": "Other tests",
                "groupId": 962,
                "type": "tests",
                "builtin": 0
            },
        ]
    }
    assert webhooks.list(name="Other tests") == [LabelGroupInList(962, "Other tests", "tests", 0)]


def test_get_groups(webhooks, api):
    api.request.return_value = {
        "groups": [
            {
                "name": "Cloud",
                "groupId": -2,
                "type": "agents",
                "builtin": 1,
                "agents": [
                    {
                        "agentId": 3,
                        "agentName": "Singapore",
                        "agentType": "Cloud",
                        "countryId": "SG",
                        "ipAddresses": [
                            "202.150.211.165",
                            "202.150.211.164",
                            "202.150.211.163"
                        ],
                        "ipv6Policy": "FORCE_IPV4",
                        "location": "Singapore"
                    }
                ]
            }
        ]
    }
    results_id = webhooks.get(-2)
    results_name = webhooks.get(group_name="Cloud")
    results_name_empty = webhooks.get(group_name="Cloud1")
    assert results_name_empty is None
    assert isinstance(results_name, LabelGroupDetails)
    assert results_id.group_id == results_name.group_id
    assert results_id.agents[0].name == "Singapore"
