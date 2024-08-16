# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel
from .shared.references import References
from .shared.response_wrapper import ResponseWrapper

__all__ = ["StopsForLocationListResponse", "StopsForLocationListResponseData", "StopsForLocationListResponseDataList"]


class StopsForLocationListResponseDataList(BaseModel):
    id: str

    lat: float

    lon: float

    name: str

    parent: str

    route_ids: List[str] = FieldInfo(alias="routeIds")

    static_route_ids: List[str] = FieldInfo(alias="staticRouteIds")

    code: Optional[str] = None

    direction: Optional[str] = None

    location_type: Optional[int] = FieldInfo(alias="locationType", default=None)

    wheelchair_boarding: Optional[str] = FieldInfo(alias="wheelchairBoarding", default=None)


class StopsForLocationListResponseData(BaseModel):
    limit_exceeded: bool = FieldInfo(alias="limitExceeded")

    list: List[StopsForLocationListResponseDataList]

    references: References


class StopsForLocationListResponse(ResponseWrapper):
    data: StopsForLocationListResponseData
