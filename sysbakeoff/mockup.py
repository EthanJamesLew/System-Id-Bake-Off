"""Mockup Data for Testing
TODO: move this out of the library
"""

from .model import *
import uuid

## system id methods ##

ak_baseline = SystemIdMethod(
    name="DMDc",
    descr="Dynamic Mode Decomposition with Control",
    is_discrete=True,
    is_continuous=False,
    accepts_inputs=True,
)

ak_polynomial = SystemIdMethod(
    name="KIC-Polynomial",
    descr="EDMD with Inputs and Polynomial Observables",
    is_discrete=True,
    is_continuous=False,
    accepts_inputs=True,
)

ak_fourier = SystemIdMethod(
    name="KIC-RFF",
    descr="EDMD with Inputs and Random Fourier Features Observables",
    is_discrete=True,
    is_continuous=False,
    accepts_inputs=True,
)

ak_nn = SystemIdMethod(
    name="KIC-NN",
    descr="EDMD with Inputs and Neural Network Observables",
    is_discrete=True,
    is_continuous=False,
    accepts_inputs=True,
)

## benchmarks ##

pendulum_bench = Benchmark(
    name="Pendulum with Input",
    descr="Torque Actuated Pendulum",
    dims=2,
    input_dims=1,
    accepts_input=True,
)

fhn_bench = Benchmark(
    name="FitzHugh-Nagumo",
    descr="FHN Oscillator",
    dims=2,
    input_dims=0,
    accepts_input=False,
)

robertson_bench = Benchmark(
    name="Robertson",
    descr="Chemical Reaction",
    dims=2,
    input_dims=0,
    accepts_input=False,
)

relative_error = Score(
    name="Relative Error", descr="<equation here>", lower_better=True
)


benchmarks = [robertson_bench, pendulum_bench, fhn_bench]


systemid_methods = [ak_baseline, ak_fourier, ak_nn, ak_polynomial]


scores = [relative_error]


results = [
    BenchmarkResult(
        uid=str(uuid.uuid4()),
        method=ak_baseline.id,
        benchmark=pendulum_bench.id,
        value=ScoreValue(
            score=relative_error.id,
            value=21.4,
        ),
    ),
    BenchmarkResult(
        uid=str(uuid.uuid4()),
        method=ak_polynomial.id,
        benchmark=pendulum_bench.id,
        value=ScoreValue(
            score=relative_error.id,
            value=1.37,
        ),
    ),
    BenchmarkResult(
        uid=str(uuid.uuid4()),
        method=ak_fourier.id,
        benchmark=pendulum_bench.id,
        value=ScoreValue(
            score=relative_error.id,
            value=1.62,
        ),
    ),
    BenchmarkResult(
        uid=str(uuid.uuid4()),
        method=ak_nn.id,
        benchmark=pendulum_bench.id,
        value=ScoreValue(
            score=relative_error.id,
            value=43.2,
        ),
    ),
    BenchmarkResult(
        uid=str(uuid.uuid4()),
        method=ak_baseline.id,
        benchmark=fhn_bench.id,
        value=ScoreValue(
            score=relative_error.id,
            value=21.4,
        ),
    ),
    BenchmarkResult(
        uid=str(uuid.uuid4()),
        method=ak_polynomial.id,
        benchmark=fhn_bench.id,
        value=ScoreValue(
            score=relative_error.id,
            value=1.37,
        ),
    ),
    BenchmarkResult(
        uid=str(uuid.uuid4()),
        method=ak_fourier.id,
        benchmark=fhn_bench.id,
        value=ScoreValue(
            score=relative_error.id,
            value=1.62,
        ),
    ),
    BenchmarkResult(
        uid=str(uuid.uuid4()),
        method=ak_nn.id,
        benchmark=fhn_bench.id,
        value=ScoreValue(
            score=relative_error.id,
            value=43.2,
        ),
    ),
    BenchmarkResult(
        uid=str(uuid.uuid4()),
        method=ak_baseline.id,
        benchmark=robertson_bench.id,
        value=ScoreValue(
            score=relative_error.id,
            value=21.4,
        ),
    ),
    BenchmarkResult(
        uid=str(uuid.uuid4()),
        method=ak_polynomial.id,
        benchmark=robertson_bench.id,
        value=ScoreValue(
            score=relative_error.id,
            value=1.37,
        ),
    ),
    BenchmarkResult(
        uid=str(uuid.uuid4()),
        method=ak_fourier.id,
        benchmark=robertson_bench.id,
        value=ScoreValue(
            score=relative_error.id,
            value=1.62,
        ),
    ),
    BenchmarkResult(
        uid=str(uuid.uuid4()),
        method=ak_nn.id,
        benchmark=robertson_bench.id,
        value=ScoreValue(
            score=relative_error.id,
            value=43.2,
        ),
    ),
]
