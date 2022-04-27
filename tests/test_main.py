from unittest import mock

import pytest
import requests
import json

from thousandeyessdk import ThousandEyes
from thousandeyessdk.alert import Alert

from . import AUTH_TOKEN, BEARER_TOKEN, URL, USERNAME, ALERT


class TestMain():
    STATUS_URL = URL + '/status'
    TEST_RESULT = {'test': 'result'}

    @mock.patch('requests.request')
    def test_token(self, mock_get):
        mock_get().json.return_value = TestMain.TEST_RESULT
        ThousandEyes(username=USERNAME, auth_token=AUTH_TOKEN)

        requests.request.assert_called_with(
            method='GET',
            url=TestMain.STATUS_URL,
            headers={}, auth=(USERNAME, AUTH_TOKEN),
            params={'format': 'json', 'window': None, 'aid:': None},
            json=None
        )
        assert TestMain.TEST_RESULT == requests.request().json()

    @mock.patch('requests.request')
    def test_username(self, mock_get):
        mock_get().json.return_value = TestMain.TEST_RESULT
        ThousandEyes(bearer_token=BEARER_TOKEN)

        requests.request.assert_called_with(
            method='GET',
            url=TestMain.STATUS_URL,
            headers={'Authorization': f'Bearer {BEARER_TOKEN}'},
            auth=None,
            params={'format': 'json', 'window': None, 'aid:': None},
            json=None
        )
        assert TestMain.TEST_RESULT == requests.request().json()

    def test_negative_no_credentials(self):
        with pytest.raises(
            TypeError,
            match='You must provide credentials. Please provide either the bearer_token or the username and auth_token.'
        ):
            ThousandEyes()

    def test_negative_invalid_response_format(self):
        with pytest.raises(
            TypeError,
            match='"invalid" is not an acceptable response format. Please use one of json, xml'
        ):
            ThousandEyes(bearer_token=BEARER_TOKEN, response_format='invalid')

    def test_negative_invalid_aid(self):
        with pytest.raises(
            TypeError,
            match=r"Account group ID \(aid\) must be an Integer. Instead we found invalid of type <class 'str'>"
        ):
            ThousandEyes(bearer_token=BEARER_TOKEN, aid='invalid')


class TestAlert():

    def test_alert_id(self):
        alert = Alert('api',json.loads(ALERT),'/alerts')
        assert alert.id == 123456789