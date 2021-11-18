# https://developer.thousandeyes.com/v6/endpoint_tests/
from .core.base_entity import BaseEntity


class EndpointTest(BaseEntity):
    """A single instance for a single endpoint test"""

    @property
    def id(self) -> int:
        """unique test ID of the endpoint test"""
        return self._data.get('testId')

    @property
    def name(self) -> str:
        """unique name of the endpoint test"""
        return self._data.get('testName')

    @property
    def interval(self) -> int:
        """interval of the endpoint test"""
        return self._data.get('interval')
    
    # Functions

    def get_detailed_path_trace(self, agent_id, interval):
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
        return self._api._request(f'/endpoint-data/tests/net/path-vis/{self.id}/{agent_id}/{interval}')['endpointNet']

    def __repr__(self):
        return f'<EndpointTest id={self.id} name={self.name}>'
