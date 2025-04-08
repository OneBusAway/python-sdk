# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel
from .shared.references import References
from .shared.response_wrapper import ResponseWrapper

__all__ = [
    "ScheduleForStopRetrieveResponse",
    "ScheduleForStopRetrieveResponseData",
    "ScheduleForStopRetrieveResponseDataEntry",
    "ScheduleForStopRetrieveResponseDataEntryStopRouteSchedule",
    "ScheduleForStopRetrieveResponseDataEntryStopRouteScheduleStopRouteDirectionSchedule",
    "ScheduleForStopRetrieveResponseDataEntryStopRouteScheduleStopRouteDirectionScheduleScheduleStopTime",
    "ScheduleForStopRetrieveResponseDataEntryStopRouteScheduleStopRouteDirectionScheduleScheduleFrequency",
]


class ScheduleForStopRetrieveResponseDataEntryStopRouteScheduleStopRouteDirectionScheduleScheduleStopTime(BaseModel):
    arrival_enabled: bool = FieldInfo(alias="arrivalEnabled")

    arrival_time: int = FieldInfo(alias="arrivalTime")

    departure_enabled: bool = FieldInfo(alias="departureEnabled")

    departure_time: int = FieldInfo(alias="departureTime")

    service_id: str = FieldInfo(alias="serviceId")

    trip_id: str = FieldInfo(alias="tripId")

    stop_headsign: Optional[str] = FieldInfo(alias="stopHeadsign", default=None)


class ScheduleForStopRetrieveResponseDataEntryStopRouteScheduleStopRouteDirectionScheduleScheduleFrequency(BaseModel):
    end_time: int = FieldInfo(alias="endTime")

    headway: int

    service_date: int = FieldInfo(alias="serviceDate")

    service_id: str = FieldInfo(alias="serviceId")

    start_time: int = FieldInfo(alias="startTime")

    trip_id: str = FieldInfo(alias="tripId")


class ScheduleForStopRetrieveResponseDataEntryStopRouteScheduleStopRouteDirectionSchedule(BaseModel):
    schedule_stop_times: List[
        ScheduleForStopRetrieveResponseDataEntryStopRouteScheduleStopRouteDirectionScheduleScheduleStopTime
    ] = FieldInfo(alias="scheduleStopTimes")

    trip_headsign: str = FieldInfo(alias="tripHeadsign")

    schedule_frequencies: Optional[
        List[ScheduleForStopRetrieveResponseDataEntryStopRouteScheduleStopRouteDirectionScheduleScheduleFrequency]
    ] = FieldInfo(alias="scheduleFrequencies", default=None)


class ScheduleForStopRetrieveResponseDataEntryStopRouteSchedule(BaseModel):
    route_id: str = FieldInfo(alias="routeId")

    stop_route_direction_schedules: List[
        ScheduleForStopRetrieveResponseDataEntryStopRouteScheduleStopRouteDirectionSchedule
    ] = FieldInfo(alias="stopRouteDirectionSchedules")


class ScheduleForStopRetrieveResponseDataEntry(BaseModel):
    date: int

    stop_id: str = FieldInfo(alias="stopId")

    stop_route_schedules: List[ScheduleForStopRetrieveResponseDataEntryStopRouteSchedule] = FieldInfo(
        alias="stopRouteSchedules"
    )


class ScheduleForStopRetrieveResponseData(BaseModel):
    entry: ScheduleForStopRetrieveResponseDataEntry

    references: References


class ScheduleForStopRetrieveResponse(ResponseWrapper):
    data: ScheduleForStopRetrieveResponseData
