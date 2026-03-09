# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel
from .shared.response_wrapper import ResponseWrapper

__all__ = [
    "ScheduleForRouteRetrieveResponse",
    "ScheduleForRouteRetrieveResponseData",
    "ScheduleForRouteRetrieveResponseDataEntry",
    "ScheduleForRouteRetrieveResponseDataEntryStopTripGrouping",
    "ScheduleForRouteRetrieveResponseDataEntryStopTripGroupingTripsWithStopTime",
    "ScheduleForRouteRetrieveResponseDataEntryStopTripGroupingTripsWithStopTimeStopTime",
]


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


class ScheduleForRouteRetrieveResponseDataEntry(BaseModel):
    route_id: str = FieldInfo(alias="routeId")

    schedule_date: int = FieldInfo(alias="scheduleDate")

    service_ids: List[str] = FieldInfo(alias="serviceIds")

    stop_trip_groupings: List[ScheduleForRouteRetrieveResponseDataEntryStopTripGrouping] = FieldInfo(
        alias="stopTripGroupings"
    )


class ScheduleForRouteRetrieveResponseData(BaseModel):
    entry: ScheduleForRouteRetrieveResponseDataEntry


class ScheduleForRouteRetrieveResponse(ResponseWrapper):
    data: ScheduleForRouteRetrieveResponseData
