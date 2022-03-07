# https://developer.thousandeyes.com/v6/endpoint_tests/

from .agent_test import AgentTest
from .list_like import ListLike


class AgentTests(ListLike):
    """
    A list-like class for handling Agent tests
    """
    SINGULAR_CLASS = AgentTest
    ROUTE = '/tests'
    KEY = 'test'
    OBJECT_NAME = 'Agent Tests'
