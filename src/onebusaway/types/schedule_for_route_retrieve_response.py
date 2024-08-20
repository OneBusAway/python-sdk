# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel
from .shared.response_wrapper import ResponseWrapper

__all__ = [
    "ScheduleForRouteRetrieveResponse",
    "ScheduleForRouteRetrieveResponseData",
    "ScheduleForRouteRetrieveResponseDataEntry",
    "ScheduleForRouteRetrieveResponseDataEntryStop",
    "ScheduleForRouteRetrieveResponseDataEntryStopTripGrouping",
    "ScheduleForRouteRetrieveResponseDataEntryStopTripGroupingTripsWithStopTime",
    "ScheduleForRouteRetrieveResponseDataEntryStopTripGroupingTripsWithStopTimeStopTime",
    "ScheduleForRouteRetrieveResponseDataEntryTrip",
]


class ScheduleForRouteRetrieveResponseDataEntryStop(BaseModel):
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


class ScheduleForRouteRetrieveResponseDataEntryStopTripGroupingTripsWithStopTimeStopTime(BaseModel):
    arrival_enabled: bool = FieldInfo(alias="arrivalEnabled")

    arrival_time: int = FieldInfo(alias="arrivalTime")

    departure_enabled: bool = FieldInfo(alias="departureEnabled")

    departure_time: int = FieldInfo(alias="departureTime")

    stop_id: str = FieldInfo(alias="stopId")

    trip_id: str = FieldInfo(alias="tripId")

    service_id: Optional[str] = FieldInfo(alias="serviceId", default=None)

    stop_headsign: Optional[str] = FieldInfo(alias="stopHeadsign", default=None)


class ScheduleForRouteRetrieveResponseDataEntryStopTripGroupingTripsWithStopTime(BaseModel):
    stop_times: List[ScheduleForRouteRetrieveResponseDataEntryStopTripGroupingTripsWithStopTimeStopTime] = FieldInfo(
        alias="stopTimes"
    )

    trip_id: str = FieldInfo(alias="tripId")


class ScheduleForRouteRetrieveResponseDataEntryStopTripGrouping(BaseModel):
    direction_id: str = FieldInfo(alias="directionId")

    stop_ids: List[str] = FieldInfo(alias="stopIds")

    trip_headsigns: List[str] = FieldInfo(alias="tripHeadsigns")

    trip_ids: List[str] = FieldInfo(alias="tripIds")

    trips_with_stop_times: Optional[
        List[ScheduleForRouteRetrieveResponseDataEntryStopTripGroupingTripsWithStopTime]
    ] = FieldInfo(alias="tripsWithStopTimes", default=None)


class ScheduleForRouteRetrieveResponseDataEntryTrip(BaseModel):
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


class ScheduleForRouteRetrieveResponseDataEntry(BaseModel):
    route_id: str = FieldInfo(alias="routeId")

    schedule_date: int = FieldInfo(alias="scheduleDate")

    service_ids: List[str] = FieldInfo(alias="serviceIds")

    stops: List[ScheduleForRouteRetrieveResponseDataEntryStop]

    stop_trip_groupings: List[ScheduleForRouteRetrieveResponseDataEntryStopTripGrouping] = FieldInfo(
        alias="stopTripGroupings"
    )

    trips: List[ScheduleForRouteRetrieveResponseDataEntryTrip]


class ScheduleForRouteRetrieveResponseData(BaseModel):
    entry: ScheduleForRouteRetrieveResponseDataEntry


class ScheduleForRouteRetrieveResponse(ResponseWrapper):
    data: ScheduleForRouteRetrieveResponseData
