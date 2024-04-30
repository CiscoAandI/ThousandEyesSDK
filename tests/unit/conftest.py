from unittest.mock import Mock

import pytest
import requests


@pytest.fixture
def mocked_requests(monkeypatch):
    mocked_request = Mock()
    mocked_request().json.return_value = {"some": "content"}
    monkeypatch.setattr(requests, "request", mocked_request)


@pytest.fixture
def mocked_requests__invalid_credentials(monkeypatch):
    mocked_request = Mock()
    mocked_request().json.return_value = {"error": "invalid credentials"}
    mocked_request().ok = False
    mocked_request().status_code = 401
    monkeypatch.setattr(requests, "request", mocked_request)

