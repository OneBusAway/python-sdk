# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel
from .shared.references import References
from .shared.response_wrapper import ResponseWrapper

__all__ = [
    "RoutesForLocationListResponse",
    "RoutesForLocationListResponseData",
    "RoutesForLocationListResponseDataList",
]


class RoutesForLocationListResponseDataList(BaseModel):
    id: str

    agency_id: str = FieldInfo(alias="agencyId")

    type: int

    color: Optional[str] = None

    description: Optional[str] = None

    long_name: Optional[str] = FieldInfo(alias="longName", default=None)

    null_safe_short_name: Optional[str] = FieldInfo(alias="nullSafeShortName", default=None)

    short_name: Optional[str] = FieldInfo(alias="shortName", default=None)

    text_color: Optional[str] = FieldInfo(alias="textColor", default=None)

    url: Optional[str] = None


class RoutesForLocationListResponseData(BaseModel):
    limit_exceeded: bool = FieldInfo(alias="limitExceeded")

    list: List[RoutesForLocationListResponseDataList]

    out_of_range: bool = FieldInfo(alias="outOfRange")

    references: References


class RoutesForLocationListResponse(ResponseWrapper):
    data: RoutesForLocationListResponseData
