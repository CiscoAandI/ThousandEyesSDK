from requests import Response
from datetime import datetime
import logging
from time import sleep
from typing import Optional

LOG = logging.getLogger(__name__)


class RateLimit:
    def __init__(self, response: Response):
        self.response = response

    def wait(self):
        sleep_time = self.get_sleep_time() + 1
        LOG.warning(
            f"Maximum number of requests per minute reached for {self.response.url}"
            f"sleep time applied, waiting {sleep_time} seconds"
        )
        sleep(sleep_time)

    def get_sleep_time(self) -> int:
        rollover = self.rollover
        current = self.current

        # test ThousandEyes provided dates
        try:
            sleep_time = rollover - current
            sleep_time = sleep_time.seconds
            if sleep_time < 60:
                return sleep_time
        except TypeError:
            pass

        # fallback in case of problem with ThousandEyes dates
        return self.calculate_sleep_time()

    def calculate_sleep_time(self):
        current = rollover = datetime.utcnow()
        rollover = rollover.replace(minute=rollover.minute + 1)
        rollover = rollover.replace(second=0, microsecond=0)
        sleep_time = rollover - current
        sleep_time = sleep_time.seconds
        LOG.warning(f"rollover and current date validation failed, using self calculated sleep time: {sleep_time}")
        return sleep_time

    @property
    def current(self) -> Optional[datetime]:
        date_format = "%a, %d %b %Y %H:%M:%S %Z"
        try:
            current_date_string = self.response.headers["Date"]
            current = datetime.strptime(current_date_string, date_format)
            LOG.debug(f"using date string contained in HTTP response: {current}")
        except (KeyError, ValueError, AttributeError):
            LOG.warning(f"could not obtain rollover date from HTTP response headers: {self.response.headers}")
            return None

        return current

    @property
    def rollover(self) -> Optional[datetime]:
        try:
            rollover_timestamp_string = self.response.headers["x-organization-rate-limit-reset"]
            rollover = datetime.utcfromtimestamp(int(rollover_timestamp_string))
            LOG.debug(f"using rollover date contained in HTTP response: {rollover}")
        except (KeyError, ValueError, AttributeError):
            LOG.warning(f"could not obtain rollover date from HTTP response headers: {self.response.headers}")
            return None

        return rollover
