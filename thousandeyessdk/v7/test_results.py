class TestResults:
    def __init__(self, api):
        self._api = api

    def path_vis_by_agent_and_round(self, test_id: int, agent_id: int, round_id: int, query=""):
        url = f"/test-results/{test_id}/path-vis/agent/{agent_id}/round/{round_id}"
        url = f"{url}?{query}" if query else url
        return self._api._request(url)
