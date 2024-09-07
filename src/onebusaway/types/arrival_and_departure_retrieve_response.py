# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel
from .shared.references import References
from .shared.response_wrapper import ResponseWrapper

__all__ = [
    "ArrivalAndDepartureRetrieveResponse",
    "ArrivalAndDepartureRetrieveResponseData",
    "ArrivalAndDepartureRetrieveResponseDataEntry",
    "ArrivalAndDepartureRetrieveResponseDataEntryTripStatus",
    "ArrivalAndDepartureRetrieveResponseDataEntryTripStatusLastKnownLocation",
    "ArrivalAndDepartureRetrieveResponseDataEntryTripStatusPosition",
]


class ArrivalAndDepartureRetrieveResponseDataEntryTripStatusLastKnownLocation(BaseModel):
    lat: Optional[float] = None
    """Latitude of the last known location of the transit vehicle."""

    lon: Optional[float] = None
    """Longitude of the last known location of the transit vehicle."""


class ArrivalAndDepartureRetrieveResponseDataEntryTripStatusPosition(BaseModel):
    lat: Optional[float] = None
    """Latitude of the current position of the transit vehicle."""

    lon: Optional[float] = None
    """Longitude of the current position of the transit vehicle."""


class ArrivalAndDepartureRetrieveResponseDataEntryTripStatus(BaseModel):
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

    last_known_location: Optional[ArrivalAndDepartureRetrieveResponseDataEntryTripStatusLastKnownLocation] = FieldInfo(
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

    position: Optional[ArrivalAndDepartureRetrieveResponseDataEntryTripStatusPosition] = None
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


class ArrivalAndDepartureRetrieveResponseDataEntry(BaseModel):
    arrival_enabled: bool = FieldInfo(alias="arrivalEnabled")
    """Indicates if riders can arrive on this transit vehicle."""

    block_trip_sequence: int = FieldInfo(alias="blockTripSequence")
    """Index of this arrival’s trip into the sequence of trips for the active block."""

    departure_enabled: bool = FieldInfo(alias="departureEnabled")
    """Indicates if riders can depart from this transit vehicle."""

    number_of_stops_away: int = FieldInfo(alias="numberOfStopsAway")
    """
    Number of stops between the arriving transit vehicle and the current stop
    (excluding the current stop).
    """

    predicted_arrival_time: int = FieldInfo(alias="predictedArrivalTime")
    """
    Predicted arrival time, in milliseconds since Unix epoch (zero if no real-time
    available).
    """

    predicted_departure_time: int = FieldInfo(alias="predictedDepartureTime")
    """
    Predicted departure time, in milliseconds since Unix epoch (zero if no real-time
    available).
    """

    route_id: str = FieldInfo(alias="routeId")
    """The ID of the route for the arriving vehicle."""

    scheduled_arrival_time: int = FieldInfo(alias="scheduledArrivalTime")
    """Scheduled arrival time, in milliseconds since Unix epoch."""

    scheduled_departure_time: int = FieldInfo(alias="scheduledDepartureTime")
    """Scheduled departure time, in milliseconds since Unix epoch."""

    service_date: int = FieldInfo(alias="serviceDate")
    """
    Time, in milliseconds since the Unix epoch, of midnight for the start of the
    service date for the trip.
    """

    stop_id: str = FieldInfo(alias="stopId")
    """The ID of the stop the vehicle is arriving at."""

    stop_sequence: int = FieldInfo(alias="stopSequence")
    """
    Index of the stop into the sequence of stops that make up the trip for this
    arrival.
    """

    total_stops_in_trip: int = FieldInfo(alias="totalStopsInTrip")
    """Total number of stops visited on the trip for this arrival."""

    trip_headsign: str = FieldInfo(alias="tripHeadsign")
    """
    Optional trip headsign that potentially overrides the trip headsign in the
    referenced trip element.
    """

    trip_id: str = FieldInfo(alias="tripId")
    """The ID of the trip for the arriving vehicle."""

    vehicle_id: str = FieldInfo(alias="vehicleId")
    """ID of the transit vehicle serving this trip."""

    actual_track: Optional[str] = FieldInfo(alias="actualTrack", default=None)
    """The actual track information of the arriving transit vehicle."""

    distance_from_stop: Optional[float] = FieldInfo(alias="distanceFromStop", default=None)
    """Distance of the arriving transit vehicle from the stop, in meters."""

    frequency: Optional[str] = None
    """Information about frequency-based scheduling, if applicable to the trip."""

    historical_occupancy: Optional[str] = FieldInfo(alias="historicalOccupancy", default=None)
    """Historical occupancy information of the transit vehicle."""

    last_update_time: Optional[int] = FieldInfo(alias="lastUpdateTime", default=None)
    """Timestamp of the last update time for this arrival."""

    occupancy_status: Optional[str] = FieldInfo(alias="occupancyStatus", default=None)
    """Current occupancy status of the transit vehicle."""

    predicted: Optional[bool] = None
    """Indicates if real-time arrival info is available for this trip."""

    predicted_arrival_interval: Optional[str] = FieldInfo(alias="predictedArrivalInterval", default=None)
    """Interval for predicted arrival time, if available."""

    predicted_departure_interval: Optional[str] = FieldInfo(alias="predictedDepartureInterval", default=None)
    """Interval for predicted departure time, if available."""

    predicted_occupancy: Optional[str] = FieldInfo(alias="predictedOccupancy", default=None)
    """Predicted occupancy status of the transit vehicle."""

    route_long_name: Optional[str] = FieldInfo(alias="routeLongName", default=None)
    """
    Optional route long name that potentially overrides the route long name in the
    referenced route element.
    """

    route_short_name: Optional[str] = FieldInfo(alias="routeShortName", default=None)
    """
    Optional route short name that potentially overrides the route short name in the
    referenced route element.
    """

    scheduled_arrival_interval: Optional[str] = FieldInfo(alias="scheduledArrivalInterval", default=None)
    """Interval for scheduled arrival time."""

    scheduled_departure_interval: Optional[str] = FieldInfo(alias="scheduledDepartureInterval", default=None)
    """Interval for scheduled departure time."""

    scheduled_track: Optional[str] = FieldInfo(alias="scheduledTrack", default=None)
    """Scheduled track information of the arriving transit vehicle."""

    situation_ids: Optional[List[str]] = FieldInfo(alias="situationIds", default=None)
    """References to situation elements (if any) applicable to this arrival."""

    status: Optional[str] = None
    """Current status of the arrival."""

    trip_status: Optional[ArrivalAndDepartureRetrieveResponseDataEntryTripStatus] = FieldInfo(
        alias="tripStatus", default=None
    )
    """Trip-specific status for the arriving transit vehicle."""


class ArrivalAndDepartureRetrieveResponseData(BaseModel):
    entry: ArrivalAndDepartureRetrieveResponseDataEntry

    references: References


class ArrivalAndDepartureRetrieveResponse(ResponseWrapper):
    data: ArrivalAndDepartureRetrieveResponseData
