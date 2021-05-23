from .test import Test
from typing import Optional, Iterator
from .list_like import ListLike

class Tests(ListLike):
    """
    A list-like class for handling tests
    """
    SINGULAR_CLASS = Test
    ROUTE = '/tests'
    KEY = 'test'
    OBJECT_NAME = 'Test'