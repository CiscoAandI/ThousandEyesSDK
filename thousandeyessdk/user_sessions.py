from .user_session import UserSession
from .list_like import ListLike


class UserSessions(ListLike):
    """
    A list-like class for handling user sessions
    """
    SINGULAR_CLASS = UserSession
    ROUTE = '/endpoint-data/user-sessions'
    KEY = 'userSessions'
    OBJECT_NAME = 'UserSession'
