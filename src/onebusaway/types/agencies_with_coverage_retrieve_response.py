# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel
from .shared.references import References
from .shared.response_wrapper import ResponseWrapper

__all__ = [
    "AgenciesWithCoverageRetrieveResponse",
    "AgenciesWithCoverageRetrieveResponseData",
    "AgenciesWithCoverageRetrieveResponseDataList",
]


class AgenciesWithCoverageRetrieveResponseDataList(BaseModel):
    agency_id: str = FieldInfo(alias="agencyId")

    lat: float

    lat_span: float = FieldInfo(alias="latSpan")

    lon: float

    lon_span: float = FieldInfo(alias="lonSpan")


class AgenciesWithCoverageRetrieveResponseData(BaseModel):
    limit_exceeded: Optional[bool] = FieldInfo(alias="limitExceeded", default=None)

    list: Optional[List[AgenciesWithCoverageRetrieveResponseDataList]] = None

    references: Optional[References] = None


class AgenciesWithCoverageRetrieveResponse(ResponseWrapper):
    data: Optional[AgenciesWithCoverageRetrieveResponseData] = None
