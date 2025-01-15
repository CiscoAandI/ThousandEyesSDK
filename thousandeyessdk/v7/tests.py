from .list_like import ListLikeListingClass
from ..core import BaseEntity
from datetime import datetime
import json
from typing import Literal
from enum import Enum


TEST_TYPES = Literal[
    "agent-to-agent",
    "agent-to-server",
    "bgp",
    "dns-server",
    "dns-trace",
    "dnssec",
    "ftp-server",
    "http-server",
    "page-load",
    "sip-server",
    "voice",
    "web-transactions",
    "http-server",
    "api"
]


class TestType(Enum):
    AGENT_TO_AGENT = "agent-to-agent"
    AGENT_TO_SERVER = "agent-to-server"
    BGP = "bgp"
    DNS_SERVER = "dns-server"
    DNS_TRACE = "dns-trace"
    DNSSEC = "dnssec"
    FTP_SERVER = "ftp-server"
    HTTP_SERVER = "http-server"
    PAGE_LOAD = "page-load"
    SIP_SERVER = "sip-server"
    VOICE = "voice"
    WEB_TRANSACTIONS = "web-transactions"
    API = "api"


class TestListing(BaseEntity):
    @property
    def id(self) -> str:
        return self._data.get("testId")

    @property
    def test_id(self) -> str:
        return self._data.get("testId")

    @property
    def interval(self) -> int:
        return self._data.get("interval")

    @property
    def alerts_enabled(self) -> bool|None:
        return self._data.get("alertsEnabled")

    @property
    def created_by(self) -> str:
        return self._data.get("createdBy")

    @property
    def created_date(self) -> datetime|None:
        datetime_in_iso = self._data.get("createdDate")
        if datetime_in_iso:
            return datetime.fromisoformat(datetime_in_iso)

    @property
    def live_share(self) -> bool|None:
        return self._data.get("liveShare")

    @property
    def modified_by(self) -> str:
        return self._data.get("modifiedBy")
    
    @property
    def modified_date(self) -> datetime|None:
        datetime_in_iso = self._data.get("modifiedDate")
        if datetime_in_iso:
            return datetime.fromisoformat(datetime_in_iso)

    @property
    def saved_event(self) -> bool|None:
        return self._data.get("savedEvent")
    
    @property
    def test_name(self) -> str:
        return self._data.get("testName")
    
    @property
    def type(self) -> str:
        return self._data.get("type")

    @property
    def links(self) -> dict:
        return self._data.get("_links")

    @property
    def link_test_detail(self) -> str|None:
        return self.links.get("self", {}).get("href")
    
    @property
    def link_test_detail_path(self) -> str|None:
        try:
            return self.link_test_detail.split("/v7")[1]
        except KeyError:
            return None

    @property
    def link_test_results(self) -> list[str]:
        return [link.get("href") for link in self.links.get("testResults", [])]

    @property
    def domain(self):
        return self._data.get("domain", None)

    @property
    def url(self):
        return self._data.get("url", None)

    @property
    def server(self):
        return self._data.get("server", None)

    
class Test(TestListing):
    @property
    def agent_list(self):
        return self._data.get("agents")


class Tests(ListLikeListingClass):
    SINGULAR_CLASS = Test
    LISTING_CLASS = TestListing
    ROUTE = "/tests"
    OBJECT_NAME = "Test"
    KEY = "tests"

    @property
    def as_dict(self) -> dict[str, TestListing]:
        "Downloads (if not cached in _data) all tests and returns a dictionary with test_id as key"
        if not self._data:
            self.set_cache()
        
        if self._data:
            dict_to_return = {}
            for test in self._data:
                test_id = test.get("testId")
                dict_to_return[test_id] = self.LISTING_CLASS(self._api, test, self.ROUTE)
            return dict_to_return

    def find(self, test_id: str | int) -> TestListing:
        "Finds the test with the given test_id"
        test_id = str(test_id)
        try:
            return self.as_dict[test_id]
        except KeyError:
            raise ValueError(f"Test with ID {test_id} not found.")

    def get(self, test_id: str | int) -> Test:
        """
        Downloads all tests, finds the test with the given test_id and downloads the test details.
        This method detects the test type, but costs an additional API call.
        """ 
        test_as_listing = self.find(test_id)
        query = "expand=agent"
        url = test_as_listing.link_test_detail_path
        url = f"{url}?{query}"
        return self.SINGULAR_CLASS(self._api, self._api._request(url, ), url)

    def get_by_type(self, test_id: str | int, test_type: TestType|TEST_TYPES) -> Test:
        "Downloads test details for the given test_id and test_type"
        test_id = str(test_id)
        query = "expand=agent"
        test_type = TestType(test_type) if isinstance(test_type, str) else test_type
        url = f"{self.ROUTE}/{test_type.value}/{test_id}"
        url = f"{url}?{query}"
        return self.SINGULAR_CLASS(
            self._api,
            self._api._request(url),
            url,
        )

    def get_all_with_id(self):
        "Not compatible"
    

        


