FORMATS = ["json", "xml"]
DEFAULT_URL = "https://api.thousandeyes.com"
VERSION = "v6"
URL = '/'.join([DEFAULT_URL, VERSION])
USERNAME = 'foouser@foo.com'
AUTH_TOKEN = 'fooauthtoken'
BEARER_TOKEN = 'bearer token'
ALERT_WITH_AGENTS={
     'alert': [
        {
            "active": 0,
            "agents": [
                {
                    "active": 0,
                    "metricsAtStart": "Response Time: 980 ms",
                    "metricsAtEnd": "Response Time: 148 ms",
                    "agentId": 111111,
                    "agentName": "AGENT1",
                    "dateStart": "2022-03-01 20:46:00",
                    "dateEnd": "2022-03-01 21:32:00",
                    "permalink": "https://app.thousandeyes.com/alerts/list/?__a=333666&alertId=111111111&agentId=111111"
                },
                {
                    "active": 0,
                    "metricsAtStart": "Response Time: 1,643 ms",
                    "metricsAtEnd": "Response Time: 50 ms",
                    "agentId": 222222,
                    "agentName": "AGENT2",
                    "dateStart": "2022-03-01 20:46:00",
                    "dateEnd": "2022-03-01 21:32:00",
                    "permalink": "https://app.thousandeyes.com/alerts/list/?__a=333666&alertId=111111111&agentId=111111"
                }
            ],
            "alertId": 111111111,
            "dateEnd": "2022-03-01 21:32:00",
            "dateStart": "2022-03-01 20:46:00",
            "apiLinks": [
                {
                    "rel": "related",
                    "href": "https://api.thousandeyes.com/v6/tests/4443322"
                },
                {
                    "rel": "data",
                    "href": "https://api.thousandeyes.com/v6/web/http-server/4443322"
                }
            ],
            "permalink": "https://app.thousandeyes.com/alerts/list/?__a=333666&alertId=111111111",
            "ruleExpression": "((responseTime >= 300 ms))",
            "ruleId": 555555,
            "ruleName": "response time rule",
            "testId": 4443322,
            "testName": "HTTP test to server",
            "violationCount": 2,
            "type": "HTTP Server",
            "severity": "INFO"
        }
    ]
}

ALERT_WITH_MONITORS={
    "alert": [
        {
            "active": 1,
            "alertId": 444444444,
            "dateStart": "2022-04-29 14:00:00",
            "apiLinks": [
                {
                    "rel": "related",
                    "href": "https://api.thousandeyes.com/v6/tests/2837820"
                },
                {
                    "rel": "data",
                    "href": "https://api.thousandeyes.com/v6/net/bgp-metrics/2837820"
                }
            ],
            "monitors": [
                {
                    "active": 1,
                    "metricsAtStart": "Reachability: 100%",
                    "metricsAtEnd": "",
                    "monitorId": 7,
                    "monitorName": "Sydney-1",
                    "prefixId": 10140666,
                    "prefix": "140.82.121.0/24",
                    "dateStart": "2022-04-29 14:00:00",
                    "permalink": "https://app.thousandeyes.com/alerts/list/?__a=333666&alertId=444444444&monitorId=7",
                    "network": "Telstra Pty Ltd (AS 1221)"
                },
                {
                    "active": 1,
                    "metricsAtStart": "Reachability: 100%",
                    "metricsAtEnd": "",
                    "monitorId": 21,
                    "monitorName": "Los Angeles, CA",
                    "prefixId": 10140666,
                    "prefix": "140.82.121.0/24",
                    "dateStart": "2022-04-29 14:00:00",
                    "permalink": "https://app.thousandeyes.com/alerts/list/?__a=333666&alertId=444444444&monitorId=21",
                    "network": "California State University, Office of the Chancellor (AS 2152)"
                },
                {
                    "active": 1,
                    "metricsAtStart": "Reachability: 100%",
                    "metricsAtEnd": "",
                    "monitorId": 42,
                    "monitorName": "Geneva",
                    "prefixId": 10140666,
                    "prefix": "140.82.121.0/24",
                    "dateStart": "2022-04-29 14:00:00",
                    "permalink": "https://app.thousandeyes.com/alerts/list/?__a=333666&alertId=444444444&monitorId=42",
                    "network": "VTX Services SA (AS 12350)"
                }
            ],
            "permalink": "https://app.thousandeyes.com/alerts/list/?__a=333666&alertId=444444444",
            "ruleExpression": "[(((prefixLengthIPv4 >= 16) && (prefixLengthIPv4 <= 32)) || ((prefixLengthIPv6 >= 32) && (prefixLengthIPv6 <= 128)))]((reachability > 10%))",
            "ruleId": 555555,
            "ruleName": "BGP rule",
            "testId": 4443322,
            "testName": "BGP test name",
            "violationCount": 61,
            "type": "BGP",
            "severity": "MINOR"
        }
    ]
}

ALERT_LIST={"alert": [ALERT_WITH_AGENTS["alert"][0],ALERT_WITH_MONITORS["alert"][0]]}
