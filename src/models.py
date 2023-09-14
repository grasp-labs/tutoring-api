import typing

from pydantic import BaseModel, validator


class Result(BaseModel):
    total: float


class Attributes(BaseModel):
    operator: str
    val1: typing.Union[int, float]
    val2: typing.Union[int, float]

    @validator("operator")
    def validate_operator(cls, value):
        if value not in ["+", "-", "*", "/"]:
            raise TypeError("Invalid operator. Genius.")
        return value


class ExamineRequest(BaseModel):
    headers: typing.Dict
    body: str
