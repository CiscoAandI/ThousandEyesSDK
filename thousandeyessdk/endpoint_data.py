
class EndpointData:
    """
    A class for handling endpoint data
    https://developer.thousandeyes.com/v6/endpoint/
    """

    def __init__(self, api):
        self._api = api

    @property
    def user_sessions(self):
        from .user_sessions import UserSessions
        return UserSessions(self._api)

    @property
    def test_data(self):
        from .endpoint_test_data import EndpointTestData
        return EndpointTestData(self._api)
