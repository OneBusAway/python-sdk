# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

from typing import List

from .shared.references import References

from .shared.response_wrapper import ResponseWrapper

from typing_extensions import Literal
from pydantic import Field as FieldInfo

__all__ = ["StopIDsForAgencyListResponse", "StopIDsForAgencyListResponseData"]

class StopIDsForAgencyListResponseData(BaseModel):
    limit_exceeded: bool = FieldInfo(alias = "limitExceeded")

    list: List[str]

    references: References

class StopIDsForAgencyListResponse(ResponseWrapper):
    data: StopIDsForAgencyListResponseData