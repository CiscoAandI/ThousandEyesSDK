# Thousand Eyes SDK

Note: This SDK is beta and is supported at best-effort. Please raise issues as you find them. Pull requests are more than welcome.

A Thousand Eyes Python SDK for the Thousand Eyes Monitoring Service API

``` python
from thousandeyessdk import ThousandEyes
client = ThousandEyes(username='<your_username>', auth_token='<your_auth_token>')

# Get a single alert
alert = client.alerts.get('<alert_id>')

# Print rule expression from all alerts
for alert in client.alerts.list():
    print(alert.rule.expression)

# Print all test IDs
for test in client.tests.list():
    print(test.id)

# Print all endpoint test intervals
for endpoint_test in client.endpoint_tests.list():
    print(endpoint_test.interval)

# Get the test for an alert
alert = client.alerts.get('<alert_id>')
alert_test = alert.test

# Get only active alerts
active_alerts = [i for i in alerts if i.active == 1]

# Hit the API directly without the SDK abstraction
alerts = te._request('/alerts')

# Hit the api directly and specify the method explicitly
agents = te._request(method='GET', url='/agents')
```
