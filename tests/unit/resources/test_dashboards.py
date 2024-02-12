from unittest.mock import Mock

import pytest

from thousandeyessdk.resources.dashboards import Dashboards, DASHBOARD_UI_URL


@pytest.fixture
def api():
    return Mock()


@pytest.fixture
def dashboards(api):
    return Dashboards(api)


def test_get_by_id(api: Mock, dashboards: Dashboards):
    dashboard_id = "some-dashboard-id"
    widgets = [{"some": "widget"}]
    api.request.return_value = {
        "dashboards": [
            {
                "id": dashboard_id,
                "widgets": widgets,
            }
        ]
    }

    dashboard = dashboards.by_id(dashboard_id)

    assert dashboard.id == dashboard_id
    assert dashboard.widgets == widgets


def test_all(api: Mock, dashboards: Dashboards):
    dashboards_response = {"dashboards": [{"id": "dashboard0"}, {"id": "dashboard1"}]}
    widgets0 = [{"some": "widget00"}, {"some": "widget01"}]
    dashboard0_response = {
        "dashboards": [
            {
                "id": "dashboard-id-0",
                "widgets": widgets0,
            }
        ]
    }
    widgets1 = [{"some": "widget1"}]
    dashboard1_response = {
        "dashboards": [
            {
                "id": "dashboard-id-1",
                "widgets": widgets1,
            }
        ]
    }
    api.request.side_effect = [dashboards_response, dashboard0_response, dashboard1_response]

    result = dashboards.all()
    assert len(result) == 2
    dashboard0, dashboard1 = result
    assert dashboard0.id == "dashboard-id-0"
    assert dashboard0.widgets == widgets0
    assert dashboard1.id == "dashboard-id-1"
    assert dashboard1.widgets == widgets1


def get_dashboard_response(id, test_name):
    return {
        "dashboards": [
            {
                "id": id,
                "widgets": [
                    {"dataComponents": [{"filter": {"filters": [{"value": test_name, "key": "Test Name"}]}}]},
                    {"dataComponents": [{"filter": {"filters": [{"value": "fake-test", "key": "Test Name"}]}}]},
                    {"dataComponents": [{"filter": {"filters": []}}]},
                    {
                        "dataComponents": [],
                    },
                ],
            }
        ]
    }


def test_links_for_test(api: Mock, dashboards: Dashboards):
    test_name = "some-test"

    api.request.side_effect = [
        {
            "dashboards": [
                {"id": "d-1"},
                {"id": "d-2"},
                {"id": "d-3"},
                {"id": "d-4"},
            ]
        },
        get_dashboard_response("d-1", "some-other-test"),
        get_dashboard_response("d-2", test_name),
        get_dashboard_response("d-3", None),
        get_dashboard_response("d-4", test_name),
    ]

    links = dashboards.links_for_test(test_name)
    assert links == [DASHBOARD_UI_URL + "d-2", DASHBOARD_UI_URL + "d-4"]
