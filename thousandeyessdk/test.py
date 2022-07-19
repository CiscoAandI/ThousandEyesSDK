from werkzeug.exceptions import BadRequest

from .core.base_entity import BaseEntity


class Test(BaseEntity):
    """A single instance for a single test"""

    def _get_detail(self) -> None:
        self._data |= self._api._request(f'/tests/{self.id}')['test'][0]

    @property
    def id(self) -> int:
        """unique ID of the test"""
        return self._data.get('testId')

    @property
    def agent_list(self):
        return self._data.get('agents')

    @property
    def interval(self):
        return self._data.get('interval')

    # this should be done in a way that informs user if there is no domain field
    @property
    def domain(self):
        return self._data.get('domain', None)

    @property
    def country_id(self):
        return self._data.get('countryId', None)

    def _get_test_data(self, url, object_key, list_key):
        try:
            for response in self._api._follow_pagination(url):
                for instance in response[object_key].get(list_key, []):
                    yield instance
        except BadRequest:
            return []

    def get_end_to_end_metrics(self):
        endpoint = f'/net/metrics/{self.id}'
        return self._get_test_data(
            endpoint, "net", "metrics"
        )

    def get_path_visualization(self):
        endpoint = f'/net/path-vis/{self.id}'
        return self._get_test_data(
            endpoint, "net", "pathVis"
        )

    def get_detailed_path_trace(self, agent_id, round_id):
        endpoint = f'/net/path-vis/{self.id}/{agent_id}/{round_id}'
        return self._get_test_data(
            endpoint, "net", "pathVis"
        )

    def get_bgp_metrics(self):
        endpoint = f'/net/bgp-metrics/{self.id}'
        return self._get_test_data(
            endpoint, "net", "bgpMetrics"
        )

    def get_bgp_route_information(self, prefix_id, round_id):
        endpoint = f'/net/bgp-routes/{self.id}/{prefix_id}/{round_id}'
        return self._get_test_data(
            endpoint, "net", "bgpRoutes"
        )

    def get_http_server(self):
        endpoint = f'/web/http-server/{self.id}'
        return self._get_test_data(
            endpoint, "web", "httpServer"
        )

    def get_page_load(self):
        endpoint = f'/web/page-load/{self.id}'
        return self._get_test_data(
            endpoint, "web", "pageLoad"
        )

    def get_page_load_component_detail(self, agent_id, round_id):
        endpoint = f'/web/page-load/{self.id}/{agent_id}/{round_id}'
        return self._get_test_data(
            endpoint, "web", "pageLoad"
        )

    def get_web_transactions(self):
        endpoint = f'/web/web-transactions/{self.id}'
        return self._get_test_data(
            endpoint, "web", "webTransaction"
        )

    def get_web_transaction_detail(self, agent_id, round_id):
        endpoint = f'/web/web-transactions/{self.id}/{agent_id}/{round_id}'
        return self._get_test_data(
            endpoint, "web", "webTransaction"
        )

    def get_web_transaction_component_detail(self, agent_id, round_id, page_num):
        endpoint = f'/web/web-transactions/{self.id}/{agent_id}/{round_id}/{page_num}'
        return self._get_test_data(
            endpoint, "web", "webTransaction"
        )

    def get_ftp_server(self):
        endpoint = f'/web/ftp-server/{self.id}'
        return self._get_test_data(
            endpoint, "web", "ftpServer"
        )

    def get_domain_trace(self):
        endpoint = f"/dns/trace/{self.id}"
        return self._get_test_data(
            endpoint, "dns", "trace"
        )

    def get_server_metrics(self):
        endpoint = f"/dns/server/{self.id}"
        return self._get_test_data(
            endpoint, "dns", "server"
        )

    def get_dnssec(self):
        endpoint = f"/dns/dnssec/{self.id}"
        return self._get_test_data(
            endpoint, "dns", "dnssec"
        )

    def get_sip_server(self):
        endpoint = f"/voice/sip-server/{self.id}"
        return self._get_test_data(
            endpoint, "voice", "sipMetrics"
        )

    def get_rtp_stream(self):
        endpoint = f"/voice/rtp-stream/{self.id}"
        return self._get_test_data(
            endpoint, "voice", "metrics"
        )

    def __repr__(self):
        return f'<Test id={self.id}>'
