import pytest
import werkzeug.exceptions

from thousandeyessdk.clients import ThousandEyes, InvalidCredentials
from . import AUTH_TOKEN, USERNAME


class TestMain:
    def test_instantiation(self, mocked_requests):
        ThousandEyes("client", "secret")

    def test_no_credentials(self):
        with pytest.raises(TypeError):
            ThousandEyes()

    def test_invalid_credentials(self):
        with pytest.raises(InvalidCredentials):
            ThousandEyes("username", "")

    def test_negative_invalid_aid(self):
        with pytest.raises(
                TypeError,
                match=r"Account group ID \(aid\) must be an Integer. Instead we found invalid of type <class 'str'>",
        ):
            ThousandEyes(username=USERNAME, auth_token=AUTH_TOKEN, aid="invalid")

    def test_throws_error_when_wrong_credentials(self, mocked_requests__invalid_credentials):
        with pytest.raises(werkzeug.exceptions.Unauthorized):
            te = ThousandEyes("", "", bearer_token="invalid token")
            list(te.tests.list())
