
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
