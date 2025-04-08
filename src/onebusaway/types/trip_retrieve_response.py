# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel
from .shared.references import References
from .shared.response_wrapper import ResponseWrapper

__all__ = ["TripRetrieveResponse", "TripRetrieveResponseData", "TripRetrieveResponseDataEntry"]


class TripRetrieveResponseDataEntry(BaseModel):
    id: str

    route_id: str = FieldInfo(alias="routeId")

    service_id: str = FieldInfo(alias="serviceId")

    block_id: Optional[str] = FieldInfo(alias="blockId", default=None)

    direction_id: Optional[str] = FieldInfo(alias="directionId", default=None)

    peak_offpeak: Optional[int] = FieldInfo(alias="peakOffpeak", default=None)

    route_short_name: Optional[str] = FieldInfo(alias="routeShortName", default=None)

    shape_id: Optional[str] = FieldInfo(alias="shapeId", default=None)

    time_zone: Optional[str] = FieldInfo(alias="timeZone", default=None)

    trip_headsign: Optional[str] = FieldInfo(alias="tripHeadsign", default=None)

    trip_short_name: Optional[str] = FieldInfo(alias="tripShortName", default=None)


class TripRetrieveResponseData(BaseModel):
    entry: TripRetrieveResponseDataEntry

    references: References


class TripRetrieveResponse(ResponseWrapper):
    data: TripRetrieveResponseData
