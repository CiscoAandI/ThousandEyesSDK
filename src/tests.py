from .list_like import ListLike
from .test import Test


class Tests(ListLike):
    """
    A list-like class for handling tests
    """
    SINGULAR_CLASS = Test
    ROUTE = '/tests'
    KEY = 'test'
    OBJECT_NAME = 'Test'
