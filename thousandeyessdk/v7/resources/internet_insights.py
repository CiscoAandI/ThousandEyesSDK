class Outages:
    def __init__(self, api):
        self._api = api

    def list(
        self,
        scope=None,
        time_window=None,
        app_names=None,
        interface_networks=None,
        start_date=None,
        end_date=None,
        only_active=True,
    ) -> list[dict]:
        filter = {}
        if scope:
            filter["outageScope"] = scope
        if time_window:
            filter["window"] = time_window
        if app_names:
            filter["applicationName"] = app_names
        if interface_networks:
            filter["interfaceNetwork"] = interface_networks
        if provider_names:
            filter["providerName"] = provider_names
        if only_active or end_date:
            filter["endDate"] = end_date
        if start_date:
            filter["startDate"] = start_date
        endpoint = "/internet-insights/outages/filter"
        response = self._api.request(endpoint, method="POST", data=filter)
        return response.get("outages", [])

    def get(self, type_, id_) -> dict:
        endpoint = f"/internet-insights/outages/{type_}/{id_}"
        response = self._api.request(endpoint)
        return response
