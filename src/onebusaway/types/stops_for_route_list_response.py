# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel
from .shared.references import References
from .shared.response_wrapper import ResponseWrapper

__all__ = [
    "StopsForRouteListResponse",
    "StopsForRouteListResponseData",
    "StopsForRouteListResponseDataData",
    "StopsForRouteListResponseDataDataEntry",
    "StopsForRouteListResponseDataDataEntryPolyline",
    "StopsForRouteListResponseDataDataEntryStopGrouping",
    "StopsForRouteListResponseDataDataEntryStopGroupingName",
    "StopsForRouteListResponseDataDataEntryStopGroupingPolyline",
]


class StopsForRouteListResponseDataDataEntryPolyline(BaseModel):
    length: Optional[int] = None

    levels: Optional[str] = None

    points: Optional[str] = None


class StopsForRouteListResponseDataDataEntryStopGroupingName(BaseModel):
    name: Optional[str] = None

    names: Optional[List[str]] = None

    type: Optional[str] = None


class StopsForRouteListResponseDataDataEntryStopGroupingPolyline(BaseModel):
    length: Optional[int] = None

    levels: Optional[str] = None

    points: Optional[str] = None


class StopsForRouteListResponseDataDataEntryStopGrouping(BaseModel):
    id: Optional[str] = None

    name: Optional[StopsForRouteListResponseDataDataEntryStopGroupingName] = None

    polylines: Optional[List[StopsForRouteListResponseDataDataEntryStopGroupingPolyline]] = None

    stop_ids: Optional[List[str]] = FieldInfo(alias="stopIds", default=None)


class StopsForRouteListResponseDataDataEntry(BaseModel):
    polylines: Optional[List[StopsForRouteListResponseDataDataEntryPolyline]] = None

    route_id: Optional[str] = FieldInfo(alias="routeId", default=None)

    stop_groupings: Optional[List[StopsForRouteListResponseDataDataEntryStopGrouping]] = FieldInfo(
        alias="stopGroupings", default=None
    )

    stop_ids: Optional[List[str]] = FieldInfo(alias="stopIds", default=None)


class StopsForRouteListResponseDataData(BaseModel):
    entry: StopsForRouteListResponseDataDataEntry

    references: References


class StopsForRouteListResponseData(BaseModel):
    data: StopsForRouteListResponseDataData


class StopsForRouteListResponse(ResponseWrapper):
    data: StopsForRouteListResponseData
