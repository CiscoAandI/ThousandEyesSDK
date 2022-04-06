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

    @property
    def agent_list(self):
        return self._data.get('agents')

    @property
    def interval(self):
        return self._data.get('interval')

    # this should be done in a way that informs user if there is no domain field
    @property
    def domain(self):
        return self._data.get('domain', None)

    @property
    def country_id(self):
        return self._data.get('countryId', None)

    def __repr__(self):
        return f'<Test id={self.id}>'
