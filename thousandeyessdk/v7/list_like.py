from ..list_like import ListLike


class ListLikeListingClass(ListLike):
    LISTING_CLASS = None

    def list(self, query=""):
        url = f"{self.ROUTE}?{query}" if query else self.ROUTE
        for item in self._data if self._data else self._api._list(url, key=self.KEY):
            yield self.LISTING_CLASS(self._api, item, self.ROUTE)
