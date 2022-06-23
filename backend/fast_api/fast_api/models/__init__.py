import typing as t
import pydantic as pd


class FormatDTO(pd.BaseModel):
    code: str


class RunDTO(pd.BaseModel):
    code: str
    stdin: t.Optional[str]
    problem_id: t.Optional[str]


class RunRO(pd.BaseModel):
    cpu_time: t.Optional[float]
    memory: t.Optional[float]  # in KB
    is_correct: t.Optional[bool]
    stdout: t.Optional[str]
    stderr: t.Optional[str]
