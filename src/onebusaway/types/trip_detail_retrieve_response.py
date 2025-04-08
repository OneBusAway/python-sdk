# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel
from .shared.references import References
from .shared.response_wrapper import ResponseWrapper

__all__ = [
    "TripDetailRetrieveResponse",
    "TripDetailRetrieveResponseData",
    "TripDetailRetrieveResponseDataEntry",
    "TripDetailRetrieveResponseDataEntrySchedule",
    "TripDetailRetrieveResponseDataEntryScheduleStopTime",
    "TripDetailRetrieveResponseDataEntryStatus",
    "TripDetailRetrieveResponseDataEntryStatusLastKnownLocation",
    "TripDetailRetrieveResponseDataEntryStatusPosition",
]


class TripDetailRetrieveResponseDataEntryScheduleStopTime(BaseModel):
    arrival_time: Optional[int] = FieldInfo(alias="arrivalTime", default=None)

    departure_time: Optional[int] = FieldInfo(alias="departureTime", default=None)

    distance_along_trip: Optional[float] = FieldInfo(alias="distanceAlongTrip", default=None)

    historical_occupancy: Optional[str] = FieldInfo(alias="historicalOccupancy", default=None)

    stop_headsign: Optional[str] = FieldInfo(alias="stopHeadsign", default=None)

    stop_id: Optional[str] = FieldInfo(alias="stopId", default=None)


class TripDetailRetrieveResponseDataEntrySchedule(BaseModel):
    next_trip_id: str = FieldInfo(alias="nextTripId")

    previous_trip_id: str = FieldInfo(alias="previousTripId")

    stop_times: List[TripDetailRetrieveResponseDataEntryScheduleStopTime] = FieldInfo(alias="stopTimes")

    time_zone: str = FieldInfo(alias="timeZone")

    frequency: Optional[str] = None


class TripDetailRetrieveResponseDataEntryStatusLastKnownLocation(BaseModel):
    lat: Optional[float] = None
    """Latitude of the last known location of the transit vehicle."""

    lon: Optional[float] = None
    """Longitude of the last known location of the transit vehicle."""


class TripDetailRetrieveResponseDataEntryStatusPosition(BaseModel):
    lat: Optional[float] = None
    """Latitude of the current position of the transit vehicle."""

    lon: Optional[float] = None
    """Longitude of the current position of the transit vehicle."""


class TripDetailRetrieveResponseDataEntryStatus(BaseModel):
    active_trip_id: str = FieldInfo(alias="activeTripId")
    """Trip ID of the trip the vehicle is actively serving."""

    block_trip_sequence: int = FieldInfo(alias="blockTripSequence")
    """Index of the active trip into the sequence of trips for the active block."""

    closest_stop: str = FieldInfo(alias="closestStop")
    """ID of the closest stop to the current location of the transit vehicle."""

    distance_along_trip: float = FieldInfo(alias="distanceAlongTrip")
    """Distance, in meters, the transit vehicle has progressed along the active trip."""

    last_known_distance_along_trip: float = FieldInfo(alias="lastKnownDistanceAlongTrip")
    """
    Last known distance along the trip received in real-time from the transit
    vehicle.
    """

    last_location_update_time: int = FieldInfo(alias="lastLocationUpdateTime")
    """Timestamp of the last known real-time location update from the transit vehicle."""

    last_update_time: int = FieldInfo(alias="lastUpdateTime")
    """Timestamp of the last known real-time update from the transit vehicle."""

    occupancy_capacity: int = FieldInfo(alias="occupancyCapacity")
    """Capacity of the transit vehicle in terms of occupancy."""

    occupancy_count: int = FieldInfo(alias="occupancyCount")
    """Current count of occupants in the transit vehicle."""

    occupancy_status: str = FieldInfo(alias="occupancyStatus")
    """Current occupancy status of the transit vehicle."""

    phase: str
    """Current journey phase of the trip."""

    predicted: bool
    """Indicates if real-time arrival info is available for this trip."""

    schedule_deviation: int = FieldInfo(alias="scheduleDeviation")
    """Deviation from the schedule in seconds (positive for late, negative for early)."""

    service_date: int = FieldInfo(alias="serviceDate")
    """
    Time, in milliseconds since the Unix epoch, of midnight for the start of the
    service date for the trip.
    """

    status: str
    """Current status modifiers for the trip."""

    total_distance_along_trip: float = FieldInfo(alias="totalDistanceAlongTrip")
    """Total length of the trip, in meters."""

    closest_stop_time_offset: Optional[int] = FieldInfo(alias="closestStopTimeOffset", default=None)
    """
    Time offset from the closest stop to the current position of the transit vehicle
    (in seconds).
    """

    frequency: Optional[str] = None
    """Information about frequency-based scheduling, if applicable to the trip."""

    last_known_location: Optional[TripDetailRetrieveResponseDataEntryStatusLastKnownLocation] = FieldInfo(
        alias="lastKnownLocation", default=None
    )
    """Last known location of the transit vehicle."""

    last_known_orientation: Optional[float] = FieldInfo(alias="lastKnownOrientation", default=None)
    """Last known orientation value received in real-time from the transit vehicle."""

    next_stop: Optional[str] = FieldInfo(alias="nextStop", default=None)
    """ID of the next stop the transit vehicle is scheduled to arrive at."""

    next_stop_time_offset: Optional[int] = FieldInfo(alias="nextStopTimeOffset", default=None)
    """
    Time offset from the next stop to the current position of the transit vehicle
    (in seconds).
    """

    orientation: Optional[float] = None
    """Orientation of the transit vehicle, represented as an angle in degrees."""

    position: Optional[TripDetailRetrieveResponseDataEntryStatusPosition] = None
    """Current position of the transit vehicle."""

    scheduled_distance_along_trip: Optional[float] = FieldInfo(alias="scheduledDistanceAlongTrip", default=None)
    """
    Distance, in meters, the transit vehicle is scheduled to have progressed along
    the active trip.
    """

    situation_ids: Optional[List[str]] = FieldInfo(alias="situationIds", default=None)
    """References to situation elements (if any) applicable to this trip."""

    vehicle_id: Optional[str] = FieldInfo(alias="vehicleId", default=None)
    """ID of the transit vehicle currently serving the trip."""


class TripDetailRetrieveResponseDataEntry(BaseModel):
    trip_id: str = FieldInfo(alias="tripId")

    frequency: Optional[str] = None

    schedule: Optional[TripDetailRetrieveResponseDataEntrySchedule] = None

    service_date: Optional[int] = FieldInfo(alias="serviceDate", default=None)

    situation_ids: Optional[List[str]] = FieldInfo(alias="situationIds", default=None)

    status: Optional[TripDetailRetrieveResponseDataEntryStatus] = None


class TripDetailRetrieveResponseData(BaseModel):
    entry: TripDetailRetrieveResponseDataEntry

    references: References


class TripDetailRetrieveResponse(ResponseWrapper):
    data: TripDetailRetrieveResponseData
