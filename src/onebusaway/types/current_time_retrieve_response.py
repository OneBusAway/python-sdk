# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel
from .shared.references import References
from .shared.response_wrapper import ResponseWrapper

__all__ = ["CurrentTimeRetrieveResponse", "CurrentTimeRetrieveResponseData", "CurrentTimeRetrieveResponseDataEntry"]


class CurrentTimeRetrieveResponseDataEntry(BaseModel):
    readable_time: Optional[str] = FieldInfo(alias="readableTime", default=None)

    time: Optional[int] = None


class CurrentTimeRetrieveResponseData(BaseModel):
    entry: Optional[CurrentTimeRetrieveResponseDataEntry] = None

    references: Optional[References] = None


class CurrentTimeRetrieveResponse(ResponseWrapper):
    data: Optional[CurrentTimeRetrieveResponseData] = None
