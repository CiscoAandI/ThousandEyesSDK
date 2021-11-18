# https://developer.thousandeyes.com/v6/tests/#/test_metadata
from .core.base_entity import BaseEntity


class Test(BaseEntity):
    """A single instance for a single test"""

    def _get_detail(self) -> None:
        self._data |= self._api._request(f'/tests/{self.id}')['test'][0]

    @property
    def id(self) -> int:
        """unique ID of the test"""
        return self._data.get('testId')

    def __repr__(self):
        return f'<Test id={self.id}>'
