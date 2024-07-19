# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel
from .shared.references import References
from .shared.response_wrapper import ResponseWrapper

__all__ = [
    "TripForVehicleRetrieveResponse",
    "TripForVehicleRetrieveResponseData",
    "TripForVehicleRetrieveResponseDataEntry",
    "TripForVehicleRetrieveResponseDataEntrySchedule",
    "TripForVehicleRetrieveResponseDataEntryScheduleStopTime",
    "TripForVehicleRetrieveResponseDataEntryStatus",
    "TripForVehicleRetrieveResponseDataEntryStatusLastKnownLocation",
    "TripForVehicleRetrieveResponseDataEntryStatusPosition",
]


class TripForVehicleRetrieveResponseDataEntryScheduleStopTime(BaseModel):
    arrival_time: Optional[int] = FieldInfo(alias="arrivalTime", default=None)

    departure_time: Optional[int] = FieldInfo(alias="departureTime", default=None)

    distance_along_trip: Optional[float] = FieldInfo(alias="distanceAlongTrip", default=None)

    historical_occupancy: Optional[str] = FieldInfo(alias="historicalOccupancy", default=None)

    stop_headsign: Optional[str] = FieldInfo(alias="stopHeadsign", default=None)

    stop_id: Optional[str] = FieldInfo(alias="stopId", default=None)


class TripForVehicleRetrieveResponseDataEntrySchedule(BaseModel):
    frequency: Optional[str] = None

    next_trip_id: Optional[str] = FieldInfo(alias="nextTripId", default=None)

    previous_trip_id: Optional[str] = FieldInfo(alias="previousTripId", default=None)

    stop_times: Optional[List[TripForVehicleRetrieveResponseDataEntryScheduleStopTime]] = FieldInfo(
        alias="stopTimes", default=None
    )

    time_zone: Optional[str] = FieldInfo(alias="timeZone", default=None)


class TripForVehicleRetrieveResponseDataEntryStatusLastKnownLocation(BaseModel):
    lat: Optional[float] = None
    """Latitude of the last known location of the transit vehicle."""

    lon: Optional[float] = None
    """Longitude of the last known location of the transit vehicle."""


class TripForVehicleRetrieveResponseDataEntryStatusPosition(BaseModel):
    lat: Optional[float] = None
    """Latitude of the current position of the transit vehicle."""

    lon: Optional[float] = None
    """Longitude of the current position of the transit vehicle."""


class TripForVehicleRetrieveResponseDataEntryStatus(BaseModel):
    active_trip_id: Optional[str] = FieldInfo(alias="activeTripId", default=None)
    """Trip ID of the trip the vehicle is actively serving."""

    block_trip_sequence: Optional[int] = FieldInfo(alias="blockTripSequence", default=None)
    """Index of the active trip into the sequence of trips for the active block."""

    closest_stop: Optional[str] = FieldInfo(alias="closestStop", default=None)
    """ID of the closest stop to the current location of the transit vehicle."""

    closest_stop_time_offset: Optional[int] = FieldInfo(alias="closestStopTimeOffset", default=None)
    """
    Time offset from the closest stop to the current position of the transit vehicle
    (in seconds).
    """

    distance_along_trip: Optional[float] = FieldInfo(alias="distanceAlongTrip", default=None)
    """Distance, in meters, the transit vehicle has progressed along the active trip."""

    frequency: Optional[str] = None
    """Information about frequency-based scheduling, if applicable to the trip."""

    last_known_distance_along_trip: Optional[float] = FieldInfo(alias="lastKnownDistanceAlongTrip", default=None)
    """
    Last known distance along the trip received in real-time from the transit
    vehicle.
    """

    last_known_location: Optional[TripForVehicleRetrieveResponseDataEntryStatusLastKnownLocation] = FieldInfo(
        alias="lastKnownLocation", default=None
    )
    """Last known location of the transit vehicle."""

    last_known_orientation: Optional[float] = FieldInfo(alias="lastKnownOrientation", default=None)
    """Last known orientation value received in real-time from the transit vehicle."""

    last_location_update_time: Optional[int] = FieldInfo(alias="lastLocationUpdateTime", default=None)
    """Timestamp of the last known real-time location update from the transit vehicle."""

    last_update_time: Optional[int] = FieldInfo(alias="lastUpdateTime", default=None)
    """Timestamp of the last known real-time update from the transit vehicle."""

    next_stop: Optional[str] = FieldInfo(alias="nextStop", default=None)
    """ID of the next stop the transit vehicle is scheduled to arrive at."""

    next_stop_time_offset: Optional[int] = FieldInfo(alias="nextStopTimeOffset", default=None)
    """
    Time offset from the next stop to the current position of the transit vehicle
    (in seconds).
    """

    occupancy_capacity: Optional[int] = FieldInfo(alias="occupancyCapacity", default=None)
    """Capacity of the transit vehicle in terms of occupancy."""

    occupancy_count: Optional[int] = FieldInfo(alias="occupancyCount", default=None)
    """Current count of occupants in the transit vehicle."""

    occupancy_status: Optional[str] = FieldInfo(alias="occupancyStatus", default=None)
    """Current occupancy status of the transit vehicle."""

    orientation: Optional[float] = None
    """Orientation of the transit vehicle, represented as an angle in degrees."""

    phase: Optional[str] = None
    """Current journey phase of the trip."""

    position: Optional[TripForVehicleRetrieveResponseDataEntryStatusPosition] = None
    """Current position of the transit vehicle."""

    predicted: Optional[bool] = None
    """Indicates if real-time arrival info is available for this trip."""

    scheduled_distance_along_trip: Optional[float] = FieldInfo(alias="scheduledDistanceAlongTrip", default=None)
    """
    Distance, in meters, the transit vehicle is scheduled to have progressed along
    the active trip.
    """

    schedule_deviation: Optional[int] = FieldInfo(alias="scheduleDeviation", default=None)
    """Deviation from the schedule in seconds (positive for late, negative for early)."""

    service_date: Optional[int] = FieldInfo(alias="serviceDate", default=None)
    """
    Time, in milliseconds since the Unix epoch, of midnight for the start of the
    service date for the trip.
    """

    situation_ids: Optional[List[str]] = FieldInfo(alias="situationIds", default=None)
    """References to situation elements (if any) applicable to this trip."""

    status: Optional[str] = None
    """Current status modifiers for the trip."""

    total_distance_along_trip: Optional[float] = FieldInfo(alias="totalDistanceAlongTrip", default=None)
    """Total length of the trip, in meters."""

    vehicle_id: Optional[str] = FieldInfo(alias="vehicleId", default=None)
    """ID of the transit vehicle currently serving the trip."""


class TripForVehicleRetrieveResponseDataEntry(BaseModel):
    frequency: Optional[str] = None

    schedule: Optional[TripForVehicleRetrieveResponseDataEntrySchedule] = None

    service_date: Optional[int] = FieldInfo(alias="serviceDate", default=None)

    situation_ids: Optional[List[str]] = FieldInfo(alias="situationIds", default=None)

    status: Optional[TripForVehicleRetrieveResponseDataEntryStatus] = None

    trip_id: Optional[str] = FieldInfo(alias="tripId", default=None)


class TripForVehicleRetrieveResponseData(BaseModel):
    entry: Optional[TripForVehicleRetrieveResponseDataEntry] = None

    references: Optional[References] = None


class TripForVehicleRetrieveResponse(ResponseWrapper):
    data: Optional[TripForVehicleRetrieveResponseData] = None
