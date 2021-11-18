from json.decoder import JSONDecodeError
import requests
import werkzeug


class API:
    FORMATS = ["json", "xml"]
    DEFAULT_URL = "https://api.thousandeyes.com"
    VERSION = "v6"

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
        aid: int = None
    ):
        self._set_credentials(bearer_token, username, auth_token)

        # AID is a very poor name for the account group id. But this is what the thousandeyes api calls it
        # So we should stick to their nomenclature as much as possible, even if it's bad.
        self.aid = aid
        self.response_format = response_format
        self.url = (url or ThousandEyes.DEFAULT_URL) + f'/{API.VERSION}'

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

    def _request(self, url: str, method: str = "GET", json=None, raw=False) -> dict:
        # window = self._generate_window(window_integer=window_integer, window_unit=window_unit)

        payload = {
            'format': self.response_format,
            'window': None,  # TODO:
            'aid:': self.aid
        }
        headers = {
            **({'Authorization': f"Bearer {self._bearer_token}"} if self._bearer_token else {}),
            **({'Content-Type': 'application/json'} if method != 'GET' else {})
        }

        response = requests.request(
            method=method,
            url=self.url + url,
            headers=headers,
            auth=self._auth,
            params=payload,
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
        for _ in range(self.MAXIMUM_PAGES):
            paginated = self._request(url)
            for instance in (paginated[key] if key else paginated):
                yield instance

            # if no pages left, we are done
            if 'next' not in paginated.get('pages', {}):
                break


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
