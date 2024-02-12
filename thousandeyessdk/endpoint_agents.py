from .core import BaseEntity, ListLike
import logging

LOG = logging.getLogger(__name__)


class EndpointAgent(BaseEntity):
    """A single instance for a single Endpointagent"""

    @property
    def id(self):
        return self._data["agentId"]

    @property
    def name(self):
        return self._data["agentName"]

    @property
    def usernames(self):
        """client usernames for the endpoint agent installed on the system"""
        try:
            users = [profile["userProfile"]["userName"] for profile in self._data["clients"]]
            return ",".join(users)
        except KeyError as ex:
            LOG.info(f"cannot find users info {ex.args} ")

    def __repr__(self):
        return f"<EndpointAgent id={self.id} name={self.name}>"


class EndpointAgents(ListLike):
    """
    A list-like class for handling endpoint-agents
    """

    SINGULAR_CLASS = EndpointAgent
    ROUTE = "/endpoint-agents"
    KEY = "endpointAgents"
    OBJECT_NAME = "EndpointAgent"
