from datetime import datetime

from unittest.mock import patch

from thousandeyessdk.clients import ThousandEyes as TE

from . import USERNAME, AUTH_TOKEN


def create_session(id: str, agent_id: str, visited_site: str):
    return {
        "userSessionId": id,
        "agentId": agent_id,
        "visitedSite": visited_site,
    }


@patch("thousandeyessdk.clients.requests.request")
def test_user_sessions_get_sessions_for_agents(m__request):
    expected_sessions = [
        create_session("sess-0", "agent-0", "site-0"),
        create_session("sess-1", "agent-0", "site-1"),
        create_session("sess-2", "agent-1", "site-0"),
        create_session("sess-3", "agent-1", "site-2"),
    ]
    extra_sessions = [
        create_session("sess-4", "agent-7", "site-2"),
        create_session("sess-5", "agent-4", "site-1"),
        create_session("sess-6", "agent-2", "site-3"),
    ]

    sessions_data = {
        "userSessions": expected_sessions + extra_sessions,
    }
    m__request().json.return_value = sessions_data
    m__request().ok = True

    te_client = TE(username=USERNAME, auth_token=AUTH_TOKEN)

    sessions = te_client.endpoint_data.user_sessions.get_sessions_for_agents(
        {"agent-0", "agent-1"}, timestamp=datetime.now()
    )
    session_ids = {s.id for s in sessions}

    assert session_ids == {"sess-0", "sess-1", "sess-2", "sess-3"}


@patch("thousandeyessdk.clients.requests.request")
def test_user_sessions_get_sessions_for_domains(m__request):
    expected_sessions = [
        create_session("sess-0", "agent-0", "site-0"),
        create_session("sess-1", "agent-0", "site-1"),
        create_session("sess-2", "agent-1", "site-0"),
        create_session("sess-3", "agent-1", "site-2"),
    ]
    extra_sessions = [
        create_session("sess-4", "agent-7", "site-3"),
        create_session("sess-5", "agent-4", "site-4"),
        create_session("sess-6", "agent-2", "site-11"),
    ]

    sessions_data = {
        "userSessions": expected_sessions + extra_sessions,
    }
    m__request().json.return_value = sessions_data
    m__request().ok = True

    te_client = TE(username=USERNAME, auth_token=AUTH_TOKEN)

    sessions = te_client.endpoint_data.user_sessions.get_sessions_for_domains(
        {"site-0", "site-1", "site-2"}, timestamp=datetime.now()
    )
    session_ids = {s.id for s in sessions}

    assert session_ids == {"sess-0", "sess-1", "sess-2", "sess-3"}
