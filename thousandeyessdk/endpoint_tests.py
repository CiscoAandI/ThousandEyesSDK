# https://developer.thousandeyes.com/v6/endpoint_tests/

from .endpoint_test import EndpointTest
from .list_like import ListLike


class EndpointTests(ListLike):
    """
    A list-like class for handling endpoint tests
    """
    SINGULAR_CLASS = EndpointTest
    ROUTE = '/endpoint-tests'
    KEY = 'endpointTest'
    OBJECT_NAME = 'Endpoint Tests'
