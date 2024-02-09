class WebhookNotFound(Exception):
    def __init__(self, name: str):
        super().__init__(f"webhook named {name} not found")


class Webhooks:
    def __init__(self, api):
        self._api = api

    def get_id_by_name(self, name: str) -> str:
        endpoint = "/integrations"
        response = self._api.request(endpoint)
        webhooks = response["integrations"]["webhook"]
        for webhook in webhooks:
            if webhook["integrationName"] == name:
                return webhook["integrationId"]

        raise WebhookNotFound(name)
