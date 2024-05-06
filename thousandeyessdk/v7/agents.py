from thousandeyessdk.core import BaseEntity


class Agent(BaseEntity):

    @property
    def id(self):
        return self.data.get("id")

    @property
    def name(self):
        return self.data.get("name")

    @property
    def type(self):
        return self.data.get("type")

    @property
    def state(self):
        return self.data.get("state")

    @property
    def metrics_at_start(self):
        return self.data.get("start", {}).get("metrics")

    @property
    def metrics_at_end(self):
        return self.data.get("end", {}).get("metrics")
