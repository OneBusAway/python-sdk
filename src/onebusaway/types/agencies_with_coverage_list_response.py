# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from pydantic import Field as FieldInfo

from .._models import BaseModel
from .shared.references import References
from .shared.response_wrapper import ResponseWrapper

__all__ = [
    "AgenciesWithCoverageListResponse",
    "AgenciesWithCoverageListResponseData",
    "AgenciesWithCoverageListResponseDataList",
]


class AgenciesWithCoverageListResponseDataList(BaseModel):
    agency_id: str = FieldInfo(alias="agencyId")

    lat: float

    lat_span: float = FieldInfo(alias="latSpan")

    lon: float

    lon_span: float = FieldInfo(alias="lonSpan")


class AgenciesWithCoverageListResponseData(BaseModel):
    limit_exceeded: bool = FieldInfo(alias="limitExceeded")

    list: List[AgenciesWithCoverageListResponseDataList]

    references: References


class AgenciesWithCoverageListResponse(ResponseWrapper):
    data: AgenciesWithCoverageListResponseData
