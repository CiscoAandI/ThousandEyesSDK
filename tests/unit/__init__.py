FORMATS = ["json", "xml"]
DEFAULT_URL = "https://api.thousandeyes.com"
VERSION = "v6"
URL = "/".join([DEFAULT_URL, VERSION])
USERNAME = "foouser@foo.com"
AUTH_TOKEN = "fooauthtoken"
BEARER_TOKEN = "bearer token"
ALERT_WITH_AGENTS = {
    "alert": [
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
                    "permalink": (
                        "https://app.thousandeyes.com/alerts/list/?__a=333666&alertId=111111111&agentId=111111"
                    ),
                },
                {
                    "active": 0,
                    "metricsAtStart": "Response Time: 1,643 ms",
                    "metricsAtEnd": "Response Time: 50 ms",
                    "agentId": 222222,
                    "agentName": "AGENT2",
                    "dateStart": "2022-03-01 20:46:00",
                    "dateEnd": "2022-03-01 21:32:00",
                    "permalink": (
                        "https://app.thousandeyes.com/alerts/list/?__a=333666&alertId=111111111&agentId=111111"
                    ),
                },
            ],
            "alertId": 111111111,
            "dateEnd": "2022-03-01 21:32:00",
            "dateStart": "2022-03-01 20:46:00",
            "apiLinks": [
                {
                    "rel": "related",
                    "href": "https://api.thousandeyes.com/v6/tests/4443322",
                },
                {
                    "rel": "data",
                    "href": "https://api.thousandeyes.com/v6/web/http-server/4443322",
                },
            ],
            "permalink": "https://app.thousandeyes.com/alerts/list/?__a=333666&alertId=111111111",
            "ruleExpression": "((responseTime >= 300 ms))",
            "ruleId": 555555,
            "ruleName": "response time rule",
            "testId": 4443322,
            "testName": "HTTP test to server",
            "violationCount": 2,
            "type": "HTTP Server",
            "severity": "INFO",
        }
    ]
}

ALERT_WITH_MONITORS = {
    "alert": [
        {
            "active": 1,
            "alertId": 444444444,
            "dateStart": "2022-04-29 14:00:00",
            "apiLinks": [
                {"rel": "related", "href": "https://api.thousandeyes.com/v6/tests/2837820"},
                {"rel": "data", "href": "https://api.thousandeyes.com/v6/net/bgp-metrics/2837820"},
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
                    "network": "Telstra Pty Ltd (AS 1221)",
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
                    "network": "California State University, Office of the Chancellor (AS 2152)",
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
                    "network": "VTX Services SA (AS 12350)",
                },
            ],
            "permalink": "https://app.thousandeyes.com/alerts/list/?__a=333666&alertId=444444444",
            "ruleExpression": (
                "[(((prefixLengthIPv4 >= 16) && (prefixLengthIPv4 <= 32))"
                " || ((prefixLengthIPv6 >= 32) && (prefixLengthIPv6 <= 128)))]"
                "((reachability > 10%))"
            ),
            "ruleId": 555555,
            "ruleName": "BGP rule",
            "testId": 4443322,
            "testName": "BGP test name",
            "violationCount": 61,
            "type": "BGP",
            "severity": "MINOR",
        }
    ]
}

ENDPOINT_AGENT = """{
"endpointAgents":[
      {
         "agentid":"111111111",
         "agentname":"test-agent-name",
         "computerName":"test-agent-computer",
         "osVersion":"Version 13.0.1 (Build 22A400)",
         "kernelVersion":"Darwin 22.1.0",
         "manufacturer":"Apple, Inc.",
         "model":"MacBookPro18,1",
         "lastSeen":"2023-01-31 03:48:29",
         "status":"enabled",
         "deleted":false,
         "version":"1.149.0",
         "createdTime":"2023-01-24 12:47:15",
         "numberOfClients":1,
         "publicIP":"72.163.2.246",
         "location":{
            "latitude":37.33939,
            "longitude":-121.89496,
            "locationName":"San Jose, California, US"
         },
         "clients":[
            {
               "userProfile":{
                  "userName":"test-agent-username"
               },
               "browserExtensions":[

               ]
            }
         ],
         "totalMemory":"16384 MB",
         "agentType":"enterprise",
         "vpnProfiles":[
            {
               "interfaceName":"utun3",
               "vpnType":"CiscoAnyConnect",
               "vpnGatewayAddress":"72.163.19.136",
               "vpnClientAddresses":[
                  "10.24.210.102"
               ],
               "vpnClientNetworkRange":[
                  "10.24.210.102/32"
               ]
            }
         ],
         "networkInterfaceProfiles":[
            {
               "interfaceName":"en0",
               "addressProfiles":[
                  {
                     "addressType":"UNIQUE_LOCAL",
                     "ipAddress":"192.168.1.236",
                     "prefixLength":24,
                     "gateway":"192.168.1.1",
                     "routerHardwareAddress":"08:d5:9d:07:4e:e2"
                  },
                  {
                     "addressType":"UNIQUE_GLOBAL",
                     "ipAddress":"2603:6080:6104:edbc::284",
                     "prefixLength":64,
                     "gateway":"fe80::ad5:9dff:fe07:4ee2",
                     "routerHardwareAddress":"08:d5:9d:07:4e:e2"
                  },
                  {
                     "addressType":"UNIQUE_GLOBAL",
                     "ipAddress":"2603:6080:6104:edbc:1036:3978:c769:d19f",
                     "prefixLength":64,
                     "gateway":"fe80::ad5:9dff:fe07:4ee2",
                     "routerHardwareAddress":"08:d5:9d:07:4e:e2"
                  },
                  {
                     "addressType":"UNIQUE_GLOBAL",
                     "ipAddress":"2603:6080:6104:edbc:848f:ecb4:4e29:9b53",
                     "prefixLength":64,
                     "gateway":"fe80::ad5:9dff:fe07:4ee2",
                     "routerHardwareAddress":"08:d5:9d:07:4e:e2"
                  },
                  {
                     "addressType":"UNIQUE_GLOBAL",
                     "ipAddress":"2603:6080:6104:edbc::e32",
                     "prefixLength":64,
                     "gateway":"fe80::ad5:9dff:fe07:4ee2",
                     "routerHardwareAddress":"08:d5:9d:07:4e:e2"
                  }
               ],
               "hardwareType":"WIRELESS",
               "wirelessProfile":{
                  "bssid":"08:d5:9d:07:4e:e7",
                  "ssid":"MySpectrumWiFie0-5G",
                  "rssi":-82,
                  "channel":36,
                  "phyMode":"802.11ac"
               }
            },
            {
               "interfaceName":"utun3",
               "addressProfiles":[
                  {
                     "addressType":"UNIQUE_LOCAL",
                     "ipAddress":"10.24.210.102",
                     "prefixLength":32
                  },
                  {
                     "addressType":"UNIQUE_GLOBAL",
                     "ipAddress":"2001:420:c0cc:1004::6b",
                     "prefixLength":128,
                     "gateway":"ffff:ff7f:f0b8:8135:100:0:3900:0"
                  }
               ],
               "hardwareType":"VIRTUAL"
            }
         ]
      }
   ]
}"""

ALERT_RULES = {
    "alertRules": [
        {
            "alertType": "HTTP Server",
            "default": 0,
            "expression": "((responseTime >= 1500 ms))",
            "minimumSources": 1,
            "notifications": {"email": {"message": "some message", "recipient": ["test@test"]}},
            "notifyOnClear": 1,
            "roundsViolatingMode": "EXACT",
            "roundsViolatingOutOf": 3,
            "roundsViolatingRequired": 3,
            "ruleId": 1470087,
            "ruleName": "Webex Web Response Time Delay",
            "severity": "INFO",
            "tests": [],
        },
        {
            "alertType": "Page Load",
            "default": 0,
            "expression": "((pageLoadTimedOut == true))",
            "minimumSources": 1,
            "notifications": {"email": {"message": "", "recipient": []}},
            "notifyOnClear": 1,
            "roundsViolatingMode": "EXACT",
            "roundsViolatingOutOf": 3,
            "roundsViolatingRequired": 3,
            "ruleId": 1470089,
            "ruleName": "Webex Page Load Time Out",
            "severity": "INFO",
            "tests": [],
        },
    ]
}

ALERT_LIST = {"alert": [ALERT_WITH_AGENTS["alert"][0], ALERT_WITH_MONITORS["alert"][0]]}

INTEGRATIONS = {
    "integrations": {
        "thirdParty": [
            {
                "authMethod": "Auth Token",
                "authToken": "0a4693462246893f9393ed8ab2bf22f69",
                "authUser": "te",
                "integrationId": "pa-52371",
                "integrationName": "Jira Thousandeyes",
                "integrationType": "PAGER_DUTY",
            },
            {
                "channel": "@primoz",
                "integrationId": "sl-7976",
                "integrationName": "ThousandEyes Private",
                "integrationType": "SLACK",
                "target": "https://hooks.slack.com/services/T3G3DA1EY/B3243AG4Q/kwGHQz126speipc3E0e0Hx",
            },
        ],
        "webhook": [
            {
                "integrationId": "wb-4563",
                "integrationName": "Alert ThousandEyes",
                "integrationType": "WEBHOOK",
                "target": "https://webhooker.example.com/alert/z126g4a3f2a?"
                "version=0.0.1&customer_name=ACME&workflow_name=vip",
            },
            {
                "integrationId": "test-hook",
                "integrationName": "Alert ThousandEyes",
                "integrationType": "WEBHOOK",
                "target": "https://webhooker.example1.com/alert/z126g4a3f2a?"
                "version=0.0.1&customer_name=TEST_CUSTOMER&workflow_name=vip",
            },
        ],
    }
}
