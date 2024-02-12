from enum import Enum


class EnumBase(Enum):
    @classmethod
    def get(cls, name):
        for member in cls.__members__.values():
            if member.value == name:
                return member


class AlertNotificationIntegrationType(EnumBase):
    PAGER_DUTY = "PAGER_DUTY"
    WEBHOOK = "WEBHOOK"
    SLACK = "SLACK"
    APP_DYNAMICS = "APP_DYNAMICS"
    SERVICE_NOW = "SERVICE_NOW"
