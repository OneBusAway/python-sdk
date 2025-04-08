# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

from typing import Optional, List

from .shared.references import References

from .shared.response_wrapper import ResponseWrapper

from typing_extensions import Literal
from pydantic import Field as FieldInfo

__all__ = ["RoutesForAgencyListResponse", "RoutesForAgencyListResponseData", "RoutesForAgencyListResponseDataList"]

class RoutesForAgencyListResponseDataList(BaseModel):
    id: str

    agency_id: str = FieldInfo(alias = "agencyId")

    type: int

    color: Optional[str] = None

    description: Optional[str] = None

    long_name: Optional[str] = FieldInfo(alias = "longName", default = None)

    null_safe_short_name: Optional[str] = FieldInfo(alias = "nullSafeShortName", default = None)

    short_name: Optional[str] = FieldInfo(alias = "shortName", default = None)

    text_color: Optional[str] = FieldInfo(alias = "textColor", default = None)

    url: Optional[str] = None

class RoutesForAgencyListResponseData(BaseModel):
    limit_exceeded: bool = FieldInfo(alias = "limitExceeded")

    list: List[RoutesForAgencyListResponseDataList]

    references: References

class RoutesForAgencyListResponse(ResponseWrapper):
    data: RoutesForAgencyListResponseData