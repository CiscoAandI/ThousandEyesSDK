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

    def get_detailed_path_trace(self, agent_id, round_id):
        """
        Request
            Required parameters:

            {agentId} the ID of the endpoint agent from which you wish to obtain data
            {roundId} the round ID for which you wish to obtain data. Equals the beginning of the testing round, in epoch time format.
            There is no request body for this request.
        Response
            Each route should start with a hop of 1
            Where a hop number is missing from response data, this is an indication that a star (*) response was returned in the path trace attempt for that hop.
        """
        if self._api.version != 6:
            return {}

        endpoint = f'/net/path-vis/{self.id}/{agent_id}/{round_id}'
        response = self._api._request(endpoint)
        return response['net']

    def __repr__(self):
        return f'<Test id={self.id}>'
