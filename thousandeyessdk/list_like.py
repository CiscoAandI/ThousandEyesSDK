from . import API


class ListLike:
    SINGULAR_CLASS = None
    ROUTE = ''
    KEY = ''
    OBJECT_NAME = ''

    def __init__(self, api, data: list[dict] = None):
        self._api = api
        self._data = data

    def list(self, query=""):
        url = f"{self.ROUTE}?{query}" if query else self.ROUTE
        for item in self._data if self._data else self._api._list(url, key=self.KEY):
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

    def get_all_with_id(self, item_id: int):
        if not self._data:
            url = f'{self.ROUTE}/{item_id}'
            return [self.SINGULAR_CLASS(self._api, obj_data, url) for obj_data in self._api._request(url)[self.KEY]]
        else:
            result_list = []
            for item in self.list():
                if item.id == item_id:
                    result_list.append(item)
            return result_list

