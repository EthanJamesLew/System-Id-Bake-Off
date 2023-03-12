import requests
import sysbakeoff.model as sysmodel
from functools import cached_property

from typing import List


class SysidApiClient:
    @staticmethod
    def _build_request(hostname, api_request):
        r = requests.get(f"{hostname}{api_request}")
        assert isinstance(r, requests.Response)
        assert r.status_code == 200, f"for now, expecting 200 code"
        return r.json()

    def __init__(self, hostname) -> None:
        """maybe this should be a transport object"""
        self.hostname = hostname

    @cached_property
    def benchmarks(self) -> List[sysmodel.Benchmark]:
        rjson = SysidApiClient._build_request(self.hostname, "/benchmarks/")
        return [sysmodel.Benchmark(**elem) for elem in rjson]

    @cached_property
    def systemid_methods(self) -> List[sysmodel.Score]:
        rjson = SysidApiClient._build_request(self.hostname, "/systemid-methods/")
        return [sysmodel.SystemIdMethod(**elem) for elem in rjson]

    @cached_property
    def scores(self) -> List[sysmodel.Score]:
        rjson = SysidApiClient._build_request(self.hostname, "/scores/")
        return [sysmodel.Score(**elem) for elem in rjson]

    @cached_property
    def results(self):
        rjson = SysidApiClient._build_request(self.hostname, "/results/")
        return [
            [[sysmodel.BenchmarkResult(**r) for r in _v] for __, _v in v.items()]
            for _, v in rjson.items()
        ]
