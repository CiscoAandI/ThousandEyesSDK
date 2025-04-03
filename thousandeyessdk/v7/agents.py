#https://developer.cisco.com/docs/thousandeyes/v7/list-cloud-and-enterprise-agents/

from .list_like import ListLikeListingClass
from ..core import BaseEntity


class AgentListing(BaseEntity):

    @property
    def id(self):
        return self._data.get("agentId")

    @property
    def name(self):
        return self._data.get("agentName")

    @property
    def type(self):
        return self._data.get("agentType")

    @property
    def country_id(self):
        return self._data.get("countryId")

    @property
    def location(self):
        return self._data.get("location")
        
    @property
    def created_date(self):
        return self._data.get("createdDate")

    @property
    def ip_addresses(self):
        return self._data.get("ipAddresses")


class Agent(AgentListing):

    @property
    def group_names(self):
        return self.label_names

    @property
    def label_names(self):
        return [label.get("name") for label in self.labels]

    @property
    def labels(self):
        return self._data.get("labels", [])

    @property
    def links(self):
        return self._data.get("_links", {})

    @property
    def network(self):
        return self._data.get("network")

    @property
    def prefix(self):
        return self._data.get("prefix")


class Agents(ListLikeListingClass):
    SINGULAR_CLASS = Agent
    LISTING_CLASS = AgentListing
    ROUTE = "/agents"
    OBJECT_NAME = "Agent"
    KEY = "agents"

    def get(self, agent_id: int):
        url = f"{self.ROUTE}/{agent_id}"
        return self.SINGULAR_CLASS(self._api, self._api._request(url), url)