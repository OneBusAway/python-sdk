# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

from typing_extensions import Literal

from pydantic import Field as FieldInfo

__all__ = ["ResponseWrapper"]

class ResponseWrapper(BaseModel):
    code: int

    current_time: int = FieldInfo(alias = "currentTime")

    text: str

    version: int