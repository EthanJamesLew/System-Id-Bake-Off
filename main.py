from sysbakeoff import *
import sysbakeoff.mockup as mock
from fastapi import FastAPI

from typing import Dict, List


app = FastAPI(
    title="SystemIdBakeoff",
    description="API for fetching system id method performance",
    version="0.0.1"  # TODO: change this
)


@app.get("/")
def read_root():
    return {"Version": "0.0.1"}


@app.get("/benchmarks/")
async def read_benchmarks() -> List[Benchmark]:
    return mock.benchmarks 


@app.get("/systemid-methods/")
async def read_systemid_methods() -> List[SystemIdMethod]:
    return mock.systemid_methods 


@app.get("/results/")
async def read_results() -> Dict[UUID, Dict[UUID, List[BenchmarkResult]]]:
    benchmarks_names = set([r.benchmark for r in mock.results])
    res = {}
    for b in benchmarks_names:
        b_results = [r for r in mock.results if b == r.benchmark]
        scores_names = set([r.value.score for r in b_results])
        bres = {}
        for s in scores_names:
            s_results = [r for r in b_results if s == r.value.score]
            bres[s] = s_results
        res[b] = bres
    return res