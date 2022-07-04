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
    DNS_SERVER = 'DNS Server'
    DNS_TRACE = 'DNS Trace'
    SERVER_LATENCY = 'Server Latency'
    DOMAIN = 'Domain'
    PAGE_LOAD = 'Page Load'
    TRANSACTION_CLASSIC = 'Transaction (Classic)'
    TRANSACTION = 'Transaction'
    BGP = 'BGP'
    RTP_STREAM = 'RTP Stream'


class AlertTypeV7(EnumBase):
    BGP = 'bgp'
    PATH_TRACE = 'path-trace'
    END_TO_END_SERVER = 'end-to-end-server'
    END_TO_END_AGENT = 'end-to-end-agent'
    DNS_SERVER = 'dns-server'
    DNS_TRACE = 'dns-trace'
    DNS_DNSSEC = 'dns-dnssec'
    HTTP_SERVER = 'http-server'
    PAGE_LOAD = 'page-load'
    WEB_TRANSACTION = 'web-transaction'
    FTP_SERVER = 'ftp-server'
    VOICE = 'voice'
    SIP_SERVER = 'sip-server'
    NETWORK_OUTAGE = 'network-outage'
    APPLICATION_OUTAGE = 'application-outage'


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
