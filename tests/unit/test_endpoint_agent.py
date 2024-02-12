from unittest.mock import patch

from thousandeyessdk.clients import ThousandEyes as TE

from . import USERNAME, AUTH_TOKEN


@patch("thousandeyessdk.clients.requests.request")
def test_endpointagent(m__request):
    endpoint_agent_data = {
        "endpointAgents": [
            {
                "agentId": "5fff7973-a116-4600-b6de-2eb1e825c0a6",
                "agentName": "KTRZCINS-M-J4E4",
                "clients": [
                    {
                        "userProfile": {"userName": "ktrzcins"},
                        "browserExtensions": [
                            {
                                "browser": "CHROME",
                                "profile": "Default",
                                "version": "1.151.0",
                                "enabled": True,
                                "active": False,
                            }
                        ],
                    }
                ],
                # ...
            }
        ]
    }
    m__request().json.return_value = endpoint_agent_data
    m__request().ok = True

    te_client = TE(username=USERNAME, auth_token=AUTH_TOKEN)

    endpoint_agent = te_client.endpoint_agents.get("5fff7973-a116-4600-b6de-2eb1e825c0a6")

    assert endpoint_agent.id == "5fff7973-a116-4600-b6de-2eb1e825c0a6"
    assert endpoint_agent.name == "KTRZCINS-M-J4E4"
    assert endpoint_agent.usernames == "ktrzcins"
