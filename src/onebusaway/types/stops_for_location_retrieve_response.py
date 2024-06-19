# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel
from .shared.references import References
from .shared.response_wrapper import ResponseWrapper

__all__ = [
    "StopsForLocationRetrieveResponse",
    "StopsForLocationRetrieveResponseData",
    "StopsForLocationRetrieveResponseDataList",
]


class StopsForLocationRetrieveResponseDataList(BaseModel):
    id: Optional[str] = None

    code: Optional[str] = None

    direction: Optional[str] = None

    lat: Optional[float] = None

    location_type: Optional[int] = FieldInfo(alias="locationType", default=None)

    lon: Optional[float] = None

    name: Optional[str] = None

    parent: Optional[str] = None

    route_ids: Optional[List[str]] = FieldInfo(alias="routeIds", default=None)

    static_route_ids: Optional[List[str]] = FieldInfo(alias="staticRouteIds", default=None)

    wheelchair_boarding: Optional[str] = FieldInfo(alias="wheelchairBoarding", default=None)


class StopsForLocationRetrieveResponseData(BaseModel):
    limit_exceeded: Optional[bool] = FieldInfo(alias="limitExceeded", default=None)

    list: Optional[List[StopsForLocationRetrieveResponseDataList]] = None

    references: Optional[References] = None


class StopsForLocationRetrieveResponse(ResponseWrapper):
    data: Optional[StopsForLocationRetrieveResponseData] = None
