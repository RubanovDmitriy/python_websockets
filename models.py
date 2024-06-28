from pydantic import BaseModel


class SumArgs(BaseModel):
    first_arg: int
    second_arg: int
