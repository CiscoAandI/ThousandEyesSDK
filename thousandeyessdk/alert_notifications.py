from typing import Optional

from .enum import AlertNotificationIntegrationType
from .core.base_entity import BaseEntity


class AlertNotificationEmail(BaseEntity):
    @property
    def message(self):
        return self._data.get('message')

    @property
    def recipient(self):
        return self._data.get('recipient')

    def __repr__(self):
        return f'<AlertNotificationEmail recipient={self.recipient}>'


class AlertNotificationIntegration(BaseEntity):
    @property
    def id(self):
        return self._data.get('integrationId')

    @property
    def name(self):
        return self._data.get('integrationName')

    @property
    def type(self):
        return AlertNotificationIntegrationType.get(self._data.get('integrationType'))

    @property
    def target(self) -> str:
        return self._data.get('target')

    # PAGER DUTY ONLY
    @property
    def auth_method(self) -> str:
        if self.type != AlertNotificationIntegrationType.PAGER_DUTY:
            raise NotImplementedError()
        else:
            return self._data.get('authMethod')

    @property
    def auth_user(self) -> str:
        if self.type != AlertNotificationIntegrationType.PAGER_DUTY:
            raise NotImplementedError()
        else:
            return self._data.get('authUser')

    @property
    def auth_token(self) -> str:
        if self.type != AlertNotificationIntegrationType.PAGER_DUTY:
            raise NotImplementedError()
        else:
            return self._data.get('authToken')

    # SLACK ONLY
    @property
    def channel(self) -> str:
        if self.type != AlertNotificationIntegrationType.SLACK:
            raise NotImplementedError()
        else:
            return self._data.get('channel')

    def __repr__(self):
        return f'<AlertNotificationIntegration type={self.type.name} name={self.name}>'


class AlertNotifications(BaseEntity):
    """
    A class for handling alert notifications
    """

    @property
    def email(self) -> Optional[AlertNotificationEmail]:
        email = self._data.get('email')
        return AlertNotificationEmail(self._api, email) if email else None

    @property
    def webhooks(self) -> list[AlertNotificationIntegration]:
        # Singular
        return [AlertNotificationIntegration(self._api, i) for i in self._data.get('webhook', [])]

    @property
    def third_party(self) -> list[AlertNotificationIntegration]:
        # Singular
        return [AlertNotificationIntegration(self._api, i) for i in self._data.get('thirdParty', [])]
