from . import API


class ListLike(API):
    SINGULAR_CLASS = None
    ROUTE = ''
    KEY = ''
    OBJECT_NAME = ''

    def __init__(self, api, data: list[dict] = None):
        self._api = api
        self._data = data

    def list(self):
        for item in self._data if self._data else self._api._list(self.ROUTE, key=self.KEY):
            yield self.SINGULAR_CLASS(self._api, item, self.ROUTE)

    def get(self, item_id: int):
        if not self._data:
            url = f'{self.ROUTE}/{item_id}'
            return self.SINGULAR_CLASS(
                self._api,
                self._api._request(url)[self.KEY][0],
                url
            )
        else:
            for item in self.list():
                if item.id == item_id:
                    return item
            raise ValueError(f"{self.OBJECT_NAME} with ID {item_id} not found.")
