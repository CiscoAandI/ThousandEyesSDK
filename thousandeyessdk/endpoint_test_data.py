

class EndpointTestData:
    """
    A class for handling endpoint test data
    https://developer.thousandeyes.com/v6/endpoint-data/tests
    """
    def __init__(self, api):
        self._api = api

    def http_server_test_data(self, test_id, query=""):
        url = f'/endpoint-data/tests/web/http-server/{test_id}'
        url = f'{url}?{query}' if query else url
        return self._api._request(url)
