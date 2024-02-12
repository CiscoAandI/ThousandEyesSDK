from unittest.mock import Mock

import pytest

from thousandeyessdk.resources.tests import (
    TestId,
    HTTPServerTest,
    Tests,
)


@pytest.fixture
def api():
    return Mock()


@pytest.fixture
def tests_resource(api):
    return Tests(api)


def test_create(tests_resource, api):
    api.request.return_value = {"test": [{"testId": "12345"}]}
    definition = HTTPServerTest(
        name="test1",
        agents=[1, 2, 3],
        interval=30,
        url="http://google.com",
    )
    test_id = tests_resource.create(definition)
    assert test_id == TestId(id="12345", type="http-server")

    api.request.assert_called_with(
        "/tests/http-server/new",
        method="POST",
        data={
            "testName": "test1",
            "agents": [{"agentId": 1}, {"agentId": 2}, {"agentId": 3}],
            "interval": 30,
            "url": "http://google.com",
        },
    )


def test_delete(tests_resource, api):
    test_id = TestId(id="12345", type="http-server")
    tests_resource.delete(test_id)
    api.request.assert_called_with("/tests/http-server/12345/delete", method="POST")
