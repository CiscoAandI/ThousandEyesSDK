FORMATS = ["json", "xml"]
DEFAULT_URL = "https://api.thousandeyes.com"
VERSION = "v6"
URL = '/'.join([DEFAULT_URL, VERSION])
USERNAME = 'foouser@foo.com'
AUTH_TOKEN = 'fooauthtoken'
BEARER_TOKEN = 'bearer token'
ALERT={
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
            "permalink": "https://app.thousandeyes.com/alerts/list/?__a=333666&alertId=123456789&agentId=111111"
        },
        {
            "active": 0,
            "metricsAtStart": "Response Time: 1,643 ms",
            "metricsAtEnd": "Response Time: 50 ms",
            "agentId": 222222,
            "agentName": "AGENT2",
            "dateStart": "2022-03-01 20:46:00",
            "dateEnd": "2022-03-01 21:32:00",
            "permalink": "https://app.thousandeyes.com/alerts/list/?__a=333666&alertId=123456789&agentId=111111"
        }
    ],
    "alertId": 123456789,
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
    "permalink": "https://app.thousandeyes.com/alerts/list/?__a=333666&alertId=123456789",
    "ruleExpression": "((responseTime >= 300 ms))",
    "ruleId": 555555,
    "ruleName": "response time rule",
    "testId": 4443322,
    "testName": "HTTP test to server",
     "violationCount": 2,
    "type": "HTTP Server",
    "severity": "INFO"
}