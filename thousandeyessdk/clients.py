import logging
from json.decoder import JSONDecodeError
from typing import Optional

import requests
from requests import Response
from werkzeug.exceptions import default_exceptions

from . import resources

from .v7 import resources as resources_v7

from .rate_limit import RateLimit


LOG = logging.getLogger(__name__)


def log_request(response: Response):
    request = response.request
    LOG.debug(f"Request Header: {request.headers} Request Body: {request.body}")
    LOG.debug(f"Response Header: {response.headers} Response Body: {response.content}")


class InvalidCredentials(Exception):
    def __init__(self):
        super().__init__("missing or invalid credentials")


class API:
    DEFAULT_URL = "https://api.thousandeyes.com"

    # This variable is set to ensure we don't enter an infinite loop.
    # If there are more than 10,000 alert pages, there are bigger problems than this SDK not working.
    MAXIMUM_PAGES = 10000

    def __init__(
        self,
        username: str,
        auth_token: str,
        url: Optional[str] = None,
        aid: int = None,
        version: int = 6,
    ):
        self.version = version
        if not (username and auth_token):
            raise InvalidCredentials()
        self._auth = (username, auth_token)

        # AID is a very poor name for the account group id. But this is what the thousandeyes api calls it
        # So we should stick to their nomenclature as much as possible, even if it's bad.
        self.aid = aid
        self.url = (url or ThousandEyes.DEFAULT_URL) + f"/v{version}"

        # Verify connectivity
        self._request("/status")

    @property
    def aid(self) -> int:
        return self._aid

    @aid.setter
    def aid(self, value: int) -> None:
        if value and not isinstance(value, int):
            raise TypeError(
                f"Account group ID (aid) must be an Integer. Instead we found {value} of type {type(value)}"
            )
        self._aid = value

    def request(self, url: str, method: str = "GET", data: Optional[dict] = None):
        return self._request(url, method, json=data)

    def _request(self, url: str, method: str = "GET", json=None, raw=False, exact_url=False) -> dict:
        # window = self._generate_window(window_integer=window_integer, window_unit=window_unit)

        params = {"format": "json", "window": None, "aid": self.aid}
        headers = {"content-type": "application/json"}

        url = url if exact_url else self.url + url
        params = {} if exact_url else params
        LOG.debug(f"sending request to {url}")
        while True:
            response = requests.request(
                method=method,
                url=url,
                headers=headers,
                auth=self._auth,
                params=params,
                json=json,
            )
            log_request(response)

            rate_limit_reached = response.status_code == 429
            if rate_limit_reached:
                RateLimit(response).wait()
            else:
                break
        if raw:
            return response

        try:
            data = response.json()
            error_message = data.get("errorMessage")
            if not error_message:
                return data

            exception_class = default_exceptions[response.status_code]
            raise exception_class(error_message)
        except (JSONDecodeError, requests.JSONDecodeError):
            LOG.error(f'Cannot decode response from "{url}": {response.text} ')

        response.raise_for_status()

    def _list(self, url, key=None):
        """
        generic generator for handling API pagination
        """
        # Use timeout pattern to ensure no infinite loops
        page = 0
        for response in self._follow_pagination(url):
            for instance in response[key] if key else response:
                yield instance

            page += 1
            if page > self.MAXIMUM_PAGES:
                break

    def _follow_pagination(self, url: str):
        response = self._request(url)
        next_page_url = self._get_next_page_url(response)

        yield response

        while next_page_url:
            response = self._request(next_page_url, exact_url=True)
            next_page_url = self._get_next_page_url(response)

            yield response

    def _get_next_page_url(self, response):
        # we might get sth other than dict as response
        pages = {}
        if isinstance(response, dict):
            pages = response.get("pages", {})

        return pages.get("next", None)


class Resources:
    def __init__(self, api):
        self.alert_rules = resources.AlertRules(api)
        self.tests_e2e = resources.Tests(api)
        self.webhooks = resources.Webhooks(api)
        self.dashboards = resources.Dashboards(api)
        self.user_sessions = resources.UserSessions(api)
        self.endpoint_agents = resources.EndpointAgents(api)
        self.groups = resources.Groups(api)


class ResourcesV7:
    def __init__(self, api):
        self.outages = resources_v7.Outages(api)


class ThousandEyes(API):
    def __init__(
        self,
        username: str,
        auth_token: str,
        url: Optional[str] = None,
        aid: int = None,
    ):
        super().__init__(username, auth_token, url, aid, version=6)
        self.resources = Resources(self)
        self.alert_rules = resources.AlertRules(self)
        self.tests_e2e = resources.Tests(self)
        self.webhooks = resources.Webhooks(self)
        self.dashboards = resources.Dashboards(self)

    @property
    def alerts(self):
        from .alerts import Alerts

        return Alerts(self)

    @property
    def tests(self):
        from .tests import Tests

        return Tests(self)

    @property
    def endpoint_tests(self):
        from .endpoint_tests import EndpointTests

        return EndpointTests(self)

    @property
    def endpoint_test_labels(self):
        from .endpoint_test_labels import EndpointTestLabels

        return EndpointTestLabels(self)

    @property
    def agents(self):
        from .agents import Agents

        return Agents(self)

    @property
    def endpoint_agents(self):
        from .endpoint_agents import EndpointAgents

        return EndpointAgents(self)

    @property
    def endpoint_data(self):
        from .endpoint_data import EndpointData

        return EndpointData(self)

    @property
    def integrations(self):
        from .alert_notifications import Integrations

        return Integrations(self).notifications


class ThousandEyesV7(API):
    def __init__(
        self,
        username: str,
        auth_token: str,
        url: Optional[str] = None,
        aid: int = None,
    ):
        super().__init__(
            username,
            auth_token,
            url,
            aid,
            version=7,
        )
        self.resources = ResourcesV7(self)

    @property
    def alerts(self):
        from .v7 import Alerts

        return Alerts(self)

    @property
    def dashboards(self):
        from .v7 import Dashboards

        return Dashboards(self)
