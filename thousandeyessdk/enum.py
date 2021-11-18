from enum import Enum


class EnumBase(Enum):
    @classmethod
    def get(cls, name):
        for member in cls.__members__.values():
            if member.value == name:
                return member


class AlertType(EnumBase):
    HTTP_SERVER = 'HTTP Server'
    END_TO_END_SERVER = 'End-to-End (Server)'
    END_TO_END_AGENT = 'End-to-End (Agent)'
    PATH_TRACE = 'Path Trace'
    TRACE_DNSSEC = 'Trace DNSSEC'
    SERVER = 'Server'
    TRACE = 'Trace'
    SERVER_LATENCY = 'Server Latency'
    DOMAIN = 'Domain'
    PAGE_LOAD = 'Page Load'
    TRANSACTION_CLASSIC = 'Transaction (Classic)'
    TRANSACTION = 'Transaction'
    BGP = 'BGP'
    RTP_STREAM = 'RTP Stream'


class AlertRuleDirection(EnumBase):
    TO_TARGET = 'TO_TARGET'
    FROM_TARGET = 'FROM_TARGET'
    BIDIRECTIONAL = 'BIDIRECTIONAL'


class RoundsViolatingMode(EnumBase):
    ANY = 'ANY'
    EXACT = 'EXACT'


class AlertNotificationIntegrationType(EnumBase):
    PAGER_DUTY = 'PAGER_DUTY'
    WEBHOOK = 'WEBHOOK'
    SLACK = 'SLACK'
    APP_DYNAMICS = 'APP_DYNAMICS'
    SERVICE_NOW = 'SERVICE_NOW'
