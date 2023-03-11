""" System ID Bakeoff API Schema Models
"""
from pydantic import BaseModel, Field
from uuid import UUID, uuid4
from typing import List


class UUIDModel(BaseModel):
    id: UUID = Field(default_factory=uuid4)


class DescribedModel(UUIDModel):
    name: str
    descr: str


class Benchmark(DescribedModel):
    """benchmark entity
    
      - has a name and description
      - has a number of state and input dimensions
    """
    dims: int
    input_dims: int
    accepts_input: bool


class SystemIdMethod(DescribedModel):
    """system identification entity

      - has a name and description
      - can be continuous, discrete, or both
      - accepts inputs optional
    """
    is_discrete: bool
    is_continuous: bool
    accepts_inputs: bool


class Score(DescribedModel):
    """score entity

      - has a name and description
      - has lower_better to determine score ordering
    """
    lower_better: bool


class ScoreValue(BaseModel):
    """score value entity (an instance of a score)

      - references a Score 
      - has numeric float value 
    """
    score: UUID 
    value: float


class BenchmarkGroup(DescribedModel):
    """benchmark group entity

      - has a name and description
    """
    ...


class SystemIdMethodGroup(DescribedModel):
    """system id method group entity

      - has a name and description
    """
    ...


class BenchmarkResult(BaseModel):
    """a benchmark result

      - a unique identifier
      - a system id method
      - a benchmark
      - a score value
    """
    uid: UUID
    method: UUID 
    benchmark: UUID 
    value: ScoreValue
