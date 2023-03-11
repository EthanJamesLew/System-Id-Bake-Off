""" System ID Bakeoff API Schema Models
"""
from pydantic import BaseModel
from typing import List


class Benchmark(BaseModel):
    """the benchmark entity
    
      - has a name and description
      - has a number of state and input dimensions
    """
    name: str
    descr: str
    dims: int
    input_dims: int
    accepts_input: bool


class SystemIdMethod(BaseModel):
    """system identification entity

      - has a name and description
      - can be continuous, discrete, or both
      - accepts inputs optional
    """
    name: str
    descr: str
    is_discrete: bool
    is_continuous: bool
    accepts_inputs: bool


class Score(BaseModel):
    """score entity

      - has a name and description
      - has lower_better to determine score ordering
    """
    name: str
    descr: str
    lower_better: bool


class ScoreValue(BaseModel):
    """score value entity (an instance of a score)

      - references a Score 
      - has numeric float value 
    """
    score: Score
    value: float


class BenchmarkGroup(BaseModel):
    """benchmark group entity

      - has a name and description
    """
    name: str
    descr: str


class SystemIdMethodGroup(BaseModel):
    """system id method group entity

      - has a name and description
    """
    name: str
    descr: str

