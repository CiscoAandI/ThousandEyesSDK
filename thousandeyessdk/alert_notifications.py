import re
from typing import Optional, Union

from .core import BaseEntity
from .enums import AlertNotificationIntegrationType


class AlertNotificationEmail(BaseEntity):
    @property
    def message(self):
        return self._data.get("message")

    @property
    def recipient(self):
        return self._data.get("recipient")

    def __repr__(self):
        return f"<AlertNotificationEmail recipient={self.recipient}>"


class AlertNotificationIntegration(BaseEntity):
    @property
    def id(self):
        return self._data.get("integrationId")

    @property
    def name(self):
        return self._data.get("integrationName")

    @property
    def type(self):
        return AlertNotificationIntegrationType.get(self._data.get("integrationType"))

    @property
    def target(self) -> str:
        return self._data.get("target")

    def __repr__(self):
        return f"<AlertNotificationIntegration type={self.type.name} name={self.name}>"


class WebhookIntegration(AlertNotificationIntegration):
    def __repr__(self):
        return f"<WebhookIntegration type={self.type.name} name={self.name}>"


class PagerDutyIntegration(AlertNotificationIntegration):
    @property
    def auth_method(self) -> str:
        return self._data.get("authMethod")

    @property
    def auth_user(self) -> str:
        return self._data.get("authUser")

    @property
    def auth_token(self) -> str:
        return self._data.get("authToken")

    def __repr__(self):
        return f"<PagerDutyIntegration type={self.type.name} name={self.name}>"


class SlackIntegration(AlertNotificationIntegration):
    @property
    def channel(self) -> str:
        return self._data.get("channel")

    def __repr__(self):
        return f"<SlackIntegration type={self.type.name} name={self.name}>"


class IntegrationTypeFactory:
    def get(self, item, api):
        if item["integrationType"] == "PAGER_DUTY":
            return PagerDutyIntegration(api, item, None)
        elif item["integrationType"] == "SLACK":
            return SlackIntegration(api, item, None)
        elif item["integrationType"] == "WEBHOOK":
            return WebhookIntegration(api, item, None)


class IntegrationsList(list):
    def __init__(self, data: list[AlertNotificationIntegration]):
        super().__init__(data)

    def get_by_name(self, name):
        return self.search_by_query("name", name)

    def get_by_id(self, id_):
        return self.search_by_query("id", id_)

    def search_by_query(self, search_attr, *args, **kwargs):
        results = []
        queries = list(args)
        match_any = kwargs.get("match_any", False)
        for key, value in kwargs.items():
            queries.append(rf"{key}={value}")
        for item in self:
            query_results = []
            for query in queries:
                query_results.append(re.search(query, getattr(item, search_attr)))
            query_results = any(query_results) if match_any else all(query_results)
            if query_results:
                results.append(item)
        return results


class WebhookIntegrationList(IntegrationsList):
    def get_by_target(self, *args, customer_name=""):
        return self.search_by_query("target", *args, customer_name=customer_name)


class AlertNotifications(BaseEntity):
    """
    A class for handling alert notifications
    """

    _factory = IntegrationTypeFactory()

    def __init__(self, api, data, path, details=None):
        super().__init__(api, data, path, details=details)
        self._get_data()

    def _get_data(self):
        if self._data is None:
            self._data = self._api._request(f"{self._path}")["integrations"]
        return self._data

    @property
    def email(self) -> Optional[AlertNotificationEmail]:
        email = self._data.get("email")
        return AlertNotificationEmail(self._api, email, None) if email else None

    @property
    def webhooks(self) -> WebhookIntegrationList[WebhookIntegration]:
        return WebhookIntegrationList([self._factory.get(i, self._api) for i in self._data.get("webhook", [])])

    @property
    def third_party(self) -> IntegrationsList[Union[PagerDutyIntegration, SlackIntegration]]:
        return IntegrationsList([self._factory.get(i, self._api) for i in self._data.get("thirdParty", [])])


class Integrations:
    def __init__(self, api):
        self._api = api

    @property
    def notifications(self):
        return AlertNotifications(self._api, None, "/integrations")
