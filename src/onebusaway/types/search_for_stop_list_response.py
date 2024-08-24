# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel
from .shared.references import References
from .shared.response_wrapper import ResponseWrapper

__all__ = ["SearchForStopListResponse", "SearchForStopListResponseData", "SearchForStopListResponseDataList"]


class SearchForStopListResponseDataList(BaseModel):
    id: str

    code: str

    lat: float

    lon: float

    name: str

    direction: Optional[str] = None

    location_type: Optional[int] = FieldInfo(alias="locationType", default=None)

    parent: Optional[str] = None

    route_ids: Optional[List[str]] = FieldInfo(alias="routeIds", default=None)

    static_route_ids: Optional[List[str]] = FieldInfo(alias="staticRouteIds", default=None)

    wheelchair_boarding: Optional[str] = FieldInfo(alias="wheelchairBoarding", default=None)


class SearchForStopListResponseData(BaseModel):
    limit_exceeded: bool = FieldInfo(alias="limitExceeded")

    list: List[SearchForStopListResponseDataList]

    out_of_range: bool = FieldInfo(alias="outOfRange")

    references: References


class SearchForStopListResponse(ResponseWrapper):
    data: Optional[SearchForStopListResponseData] = None
