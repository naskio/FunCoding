import typing as t
import pydantic as pd


class FormatDTO(pd.BaseModel):
    code: str


class RunDTO(pd.BaseModel):
    code: str = pd.Field(description='Code to run, example: printf "Hello, World!"')
    stdin: t.Optional[str]
    problem_id: t.Optional[str]


class RunRO(pd.BaseModel):
    cpu_time: t.Optional[float] = pd.Field(description='CPU time in seconds')
    memory: t.Optional[int] = pd.Field(description='Memory usage in kilobytes (KB)')
    is_correct: t.Optional[bool]
    stdout: t.Optional[str]
    # stderr: t.Optional[str]
