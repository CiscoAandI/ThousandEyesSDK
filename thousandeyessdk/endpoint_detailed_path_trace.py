# https://developer.thousandeyes.com/v6/endpoint_test_data/#/endpoint_traceroute
from .core.base_entity import BaseEntity
from .endpoint_detailed_path_trace import EndpointDetailedPathTrace


class EndpointDetailedPathTrace(BaseEntity):
    """A single instance for a single endpoint detailed path trace"""

    def __repr__(self):
        return '<EndpointDetailedPathTrace>'
