# https://developer.thousandeyes.com/v6/agents/#/agents

from .agent import Agent
from .list_like import ListLike


class Agents(ListLike):
    """
    A list-like class for handling agents
    """
    SINGULAR_CLASS = Agent
    ROUTE = '/agents'
    KEY = 'agents'
    OBJECT_NAME = 'Agent'
