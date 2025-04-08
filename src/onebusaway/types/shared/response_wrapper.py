# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.


from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["ResponseWrapper"]


class ResponseWrapper(BaseModel):
    code: int

    current_time: int = FieldInfo(alias="currentTime")

    text: str

    version: int
