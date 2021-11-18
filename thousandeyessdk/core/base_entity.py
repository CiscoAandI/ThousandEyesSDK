class BaseEntity:
    def __init__(self, api, data, path):
        self._api = api
        self._data = data
        self._path = path