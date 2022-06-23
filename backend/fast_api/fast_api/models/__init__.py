import pydantic as pd


class FormatDTO(pd.BaseModel):
    code: str
