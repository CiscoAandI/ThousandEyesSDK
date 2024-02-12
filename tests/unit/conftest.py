from unittest.mock import Mock

import pytest
import requests


@pytest.fixture
def mocked_requests(monkeypatch):
    mocked_request = Mock()
    mocked_request().json.return_value = {"some": "content"}
    monkeypatch.setattr(requests, "request", mocked_request)
