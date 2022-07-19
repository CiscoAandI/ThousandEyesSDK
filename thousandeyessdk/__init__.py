from json.decoder import JSONDecodeError
import requests
import werkzeug


class API:
    FORMATS = ["json", "xml"]
    DEFAULT_URL = "https://api.thousandeyes.com"

    # This variable is set to ensure we don't enter an infinite loop.
    # If there are more than 10,000 alert pages, there are bigger problems than this SDK not working.
    MAXIMUM_PAGES = 10000

    def __init__(
        self,
        bearer_token: str = None,
        username: str = None,
        auth_token: str = None,
        url: str = None,
        response_format: str = "json",
        aid: int = None,
        version: int = 6
    ):
        self.version = version
        self._set_credentials(bearer_token, username, auth_token)

        # AID is a very poor name for the account group id. But this is what the thousandeyes api calls it
        # So we should stick to their nomenclature as much as possible, even if it's bad.
        self.aid = aid
        self.response_format = response_format
        self.url = (url or ThousandEyes.DEFAULT_URL) + f'/v{version}'

        # Verify connectivity
        self._request('/status')

    def _set_credentials(self, bearer_token: str, username: str, auth_token: str) -> None:
        if not bearer_token:
            if not (username and auth_token):
                raise TypeError(
                    "You must provide credentials. " +
                    "Please provide either the bearer_token or the username and auth_token."
                )
            else:
                self._bearer_token = None
                self._auth = (username, auth_token)
        else:
            self._auth = None
            self._bearer_token = bearer_token

    @property
    def response_format(self) -> str:
        return self._response_format

    @response_format.setter
    def response_format(self, value: str) -> None:
        if value not in ThousandEyes.FORMATS:
            raise TypeError(
                f"\"{value}\" is not an acceptable response format. Please use one of {', '.join(ThousandEyes.FORMATS)}"
            )
        self._response_format = value

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

    def _request(self, url: str, method: str = "GET", json=None, raw=False, exact_url=False) -> dict:
        # window = self._generate_window(window_integer=window_integer, window_unit=window_unit)

        payload = {
            'format': self.response_format,
            'window': None,  # TODO:
            'aid': self.aid
        }
        headers = {
            **({'Authorization': f"Bearer {self._bearer_token}"} if self._bearer_token else {}),
            **({'Content-Type': 'application/json'} if method != 'GET' else {}),
        }

        url = url if exact_url else self.url + url
        params = {} if exact_url else payload
        response = requests.request(
            method=method,
            url=url,
            headers=headers,
            auth=self._auth,
            params=params,
            json=json
        )

        if raw:
            return response

        if response.ok:
            return response.json()
        try:
            if response.json().get('errorMessage'):
                raise werkzeug.exceptions.default_exceptions[response.status_code](response.json().get('errorMessage'))
        except JSONDecodeError:
            pass

        response.raise_for_status()

    def _list(self, url, key=None):
        """
        generic generator for handling API pagination
        """
        # Use timeout pattern to ensure no infinite loops
        page = 0
        for response in self._follow_pagination(url):
            for instance in (response[key] if key else response):
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


class ThousandEyes(API):
    @property
    def alerts(self):
        from .alerts import Alerts
        return Alerts(self)

    @property
    def alert_rules(self):
        from .alert_rules import AlertRules
        return AlertRules(self)

    @property
    def agent_tests(self):
        from .agent_tests import AgentTests
        return AgentTests(self)

    @property
    def tests(self):
        from .tests import Tests
        return Tests(self)

    @property
    def endpoint_tests(self):
        from .endpoint_tests import EndpointTests
        return EndpointTests(self)

    @property
    def agents(self):
        from .agents import Agents
        return Agents(self)

    @property
    def dashboards(self):
        from .dashboards import Dashboards
        return Dashboards(self)
        
    @property
    def endpoint_data(self):
        from .endpoint_data import EndpointData
        return EndpointData(self)


class ThousandEyesV7(API):
    def __init__(
        self,
        bearer_token: str = None,
        username: str = None,
        auth_token: str = None,
        url: str = None,
        response_format: str = "json",
        aid: int = None,
    ):
        super().__init__(
            bearer_token,
            username,
            auth_token,
            url,
            response_format,
            aid,
            version=7,
        )

    @property
    def alerts(self):
        from .v7 import Alerts
        return Alerts(self)

    @property
    def dashboards(self):
        from .v7 import Dashboards
        return Dashboards(self)
