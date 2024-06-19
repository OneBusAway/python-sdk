# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel
from .shared.response_wrapper import ResponseWrapper

__all__ = [
    "StopsForLocationListResponse",
    "StopsForLocationListResponseData",
    "StopsForLocationListResponseDataList",
    "StopsForLocationListResponseDataReferences",
    "StopsForLocationListResponseDataReferencesAgency",
    "StopsForLocationListResponseDataReferencesRoute",
    "StopsForLocationListResponseDataReferencesStop",
    "StopsForLocationListResponseDataReferencesTrip",
]


class StopsForLocationListResponseDataList(BaseModel):
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


class StopsForLocationListResponseDataReferencesAgency(BaseModel):
    id: str

    name: str

    timezone: str

    url: str

    disclaimer: Optional[str] = None

    email: Optional[str] = None

    fare_url: Optional[str] = FieldInfo(alias="fareUrl", default=None)

    lang: Optional[str] = None

    phone: Optional[str] = None

    private_service: Optional[bool] = FieldInfo(alias="privateService", default=None)


class StopsForLocationListResponseDataReferencesRoute(BaseModel):
    id: Optional[str] = None

    agency_id: Optional[str] = FieldInfo(alias="agencyId", default=None)

    color: Optional[str] = None

    description: Optional[str] = None

    long_name: Optional[str] = FieldInfo(alias="longName", default=None)

    null_safe_short_name: Optional[str] = FieldInfo(alias="nullSafeShortName", default=None)

    short_name: Optional[str] = FieldInfo(alias="shortName", default=None)

    text_color: Optional[str] = FieldInfo(alias="textColor", default=None)

    type: Optional[int] = None

    url: Optional[str] = None


class StopsForLocationListResponseDataReferencesStop(BaseModel):
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


class StopsForLocationListResponseDataReferencesTrip(BaseModel):
    id: str

    route_id: str = FieldInfo(alias="routeId")

    block_id: Optional[str] = FieldInfo(alias="blockId", default=None)

    direction_id: Optional[str] = FieldInfo(alias="directionId", default=None)

    peak_offpeak: Optional[int] = FieldInfo(alias="peakOffpeak", default=None)

    route_short_name: Optional[str] = FieldInfo(alias="routeShortName", default=None)

    service_id: Optional[str] = FieldInfo(alias="serviceId", default=None)

    shape_id: Optional[str] = FieldInfo(alias="shapeId", default=None)

    time_zone: Optional[str] = FieldInfo(alias="timeZone", default=None)

    trip_headsign: Optional[str] = FieldInfo(alias="tripHeadsign", default=None)

    trip_short_name: Optional[str] = FieldInfo(alias="tripShortName", default=None)


class StopsForLocationListResponseDataReferences(BaseModel):
    agencies: Optional[List[StopsForLocationListResponseDataReferencesAgency]] = None

    routes: Optional[List[StopsForLocationListResponseDataReferencesRoute]] = None

    situations: Optional[List[object]] = None

    stops: Optional[List[StopsForLocationListResponseDataReferencesStop]] = None

    stop_times: Optional[List[object]] = FieldInfo(alias="stopTimes", default=None)

    trips: Optional[List[StopsForLocationListResponseDataReferencesTrip]] = None


class StopsForLocationListResponseData(BaseModel):
    limit_exceeded: Optional[bool] = FieldInfo(alias="limitExceeded", default=None)

    list: Optional[List[StopsForLocationListResponseDataList]] = None

    references: Optional[StopsForLocationListResponseDataReferences] = None


class StopsForLocationListResponse(ResponseWrapper):
    data: Optional[StopsForLocationListResponseData] = None
