# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel
from .shared.references import References
from .shared.response_wrapper import ResponseWrapper

__all__ = [
    "StopsForRouteListResponse",
    "StopsForRouteListResponseData",
    "StopsForRouteListResponseDataEntry",
    "StopsForRouteListResponseDataEntryPolyline",
    "StopsForRouteListResponseDataEntryStopGrouping",
    "StopsForRouteListResponseDataEntryStopGroupingName",
    "StopsForRouteListResponseDataEntryStopGroupingPolyline",
]


class StopsForRouteListResponseDataEntryPolyline(BaseModel):
    length: Optional[int] = None

    levels: Optional[str] = None

    points: Optional[str] = None


class StopsForRouteListResponseDataEntryStopGroupingName(BaseModel):
    name: Optional[str] = None

    names: Optional[List[str]] = None

    type: Optional[str] = None


class StopsForRouteListResponseDataEntryStopGroupingPolyline(BaseModel):
    length: Optional[int] = None

    levels: Optional[str] = None

    points: Optional[str] = None


class StopsForRouteListResponseDataEntryStopGrouping(BaseModel):
    id: Optional[str] = None

    name: Optional[StopsForRouteListResponseDataEntryStopGroupingName] = None

    polylines: Optional[List[StopsForRouteListResponseDataEntryStopGroupingPolyline]] = None

    stop_ids: Optional[List[str]] = FieldInfo(alias="stopIds", default=None)


class StopsForRouteListResponseDataEntry(BaseModel):
    polylines: Optional[List[StopsForRouteListResponseDataEntryPolyline]] = None

    route_id: Optional[str] = FieldInfo(alias="routeId", default=None)

    stop_groupings: Optional[List[StopsForRouteListResponseDataEntryStopGrouping]] = FieldInfo(
        alias="stopGroupings", default=None
    )

    stop_ids: Optional[List[str]] = FieldInfo(alias="stopIds", default=None)


class StopsForRouteListResponseData(BaseModel):
    entry: StopsForRouteListResponseDataEntry

    references: References


class StopsForRouteListResponse(ResponseWrapper):
    data: StopsForRouteListResponseData
