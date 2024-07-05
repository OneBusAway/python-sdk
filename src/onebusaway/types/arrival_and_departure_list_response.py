# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel
from .shared.references import References
from .shared.response_wrapper import ResponseWrapper

__all__ = [
    "ArrivalAndDepartureListResponse",
    "ArrivalAndDepartureListResponseData",
    "ArrivalAndDepartureListResponseDataEntry",
    "ArrivalAndDepartureListResponseDataEntryArrivalsAndDeparture",
    "ArrivalAndDepartureListResponseDataEntryArrivalsAndDepartureTripStatus",
    "ArrivalAndDepartureListResponseDataEntryArrivalsAndDepartureTripStatusLastKnownLocation",
    "ArrivalAndDepartureListResponseDataEntryArrivalsAndDepartureTripStatusPosition",
]


class ArrivalAndDepartureListResponseDataEntryArrivalsAndDepartureTripStatusLastKnownLocation(BaseModel):
    lat: Optional[float] = None
    """Latitude of the last known location of the transit vehicle."""

    lon: Optional[float] = None
    """Longitude of the last known location of the transit vehicle."""


class ArrivalAndDepartureListResponseDataEntryArrivalsAndDepartureTripStatusPosition(BaseModel):
    lat: Optional[float] = None
    """Latitude of the current position of the transit vehicle."""

    lon: Optional[float] = None
    """Longitude of the current position of the transit vehicle."""


class ArrivalAndDepartureListResponseDataEntryArrivalsAndDepartureTripStatus(BaseModel):
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

    last_known_location: Optional[
        ArrivalAndDepartureListResponseDataEntryArrivalsAndDepartureTripStatusLastKnownLocation
    ] = FieldInfo(alias="lastKnownLocation", default=None)
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

    position: Optional[ArrivalAndDepartureListResponseDataEntryArrivalsAndDepartureTripStatusPosition] = None
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


class ArrivalAndDepartureListResponseDataEntryArrivalsAndDeparture(BaseModel):
    actual_track: Optional[str] = FieldInfo(alias="actualTrack", default=None)
    """The actual track information of the arriving transit vehicle."""

    arrival_enabled: Optional[bool] = FieldInfo(alias="arrivalEnabled", default=None)
    """Indicates if riders can arrive on this transit vehicle."""

    block_trip_sequence: Optional[int] = FieldInfo(alias="blockTripSequence", default=None)
    """Index of this arrival’s trip into the sequence of trips for the active block."""

    departure_enabled: Optional[bool] = FieldInfo(alias="departureEnabled", default=None)
    """Indicates if riders can depart from this transit vehicle."""

    distance_from_stop: Optional[float] = FieldInfo(alias="distanceFromStop", default=None)
    """Distance of the arriving transit vehicle from the stop, in meters."""

    frequency: Optional[str] = None
    """Information about frequency-based scheduling, if applicable to the trip."""

    historical_occupancy: Optional[str] = FieldInfo(alias="historicalOccupancy", default=None)
    """Historical occupancy information of the transit vehicle."""

    last_update_time: Optional[int] = FieldInfo(alias="lastUpdateTime", default=None)
    """Timestamp of the last update time for this arrival."""

    number_of_stops_away: Optional[int] = FieldInfo(alias="numberOfStopsAway", default=None)
    """
    Number of stops between the arriving transit vehicle and the current stop
    (excluding the current stop).
    """

    occupancy_status: Optional[str] = FieldInfo(alias="occupancyStatus", default=None)
    """Current occupancy status of the transit vehicle."""

    predicted: Optional[bool] = None
    """Indicates if real-time arrival info is available for this trip."""

    predicted_arrival_interval: Optional[str] = FieldInfo(alias="predictedArrivalInterval", default=None)
    """Interval for predicted arrival time, if available."""

    predicted_arrival_time: Optional[int] = FieldInfo(alias="predictedArrivalTime", default=None)
    """
    Predicted arrival time, in milliseconds since Unix epoch (zero if no real-time
    available).
    """

    predicted_departure_interval: Optional[str] = FieldInfo(alias="predictedDepartureInterval", default=None)
    """Interval for predicted departure time, if available."""

    predicted_departure_time: Optional[int] = FieldInfo(alias="predictedDepartureTime", default=None)
    """
    Predicted departure time, in milliseconds since Unix epoch (zero if no real-time
    available).
    """

    predicted_occupancy: Optional[str] = FieldInfo(alias="predictedOccupancy", default=None)
    """Predicted occupancy status of the transit vehicle."""

    route_id: Optional[str] = FieldInfo(alias="routeId", default=None)
    """The ID of the route for the arriving vehicle."""

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

    scheduled_arrival_time: Optional[int] = FieldInfo(alias="scheduledArrivalTime", default=None)
    """Scheduled arrival time, in milliseconds since Unix epoch."""

    scheduled_departure_interval: Optional[str] = FieldInfo(alias="scheduledDepartureInterval", default=None)
    """Interval for scheduled departure time."""

    scheduled_departure_time: Optional[int] = FieldInfo(alias="scheduledDepartureTime", default=None)
    """Scheduled departure time, in milliseconds since Unix epoch."""

    scheduled_track: Optional[str] = FieldInfo(alias="scheduledTrack", default=None)
    """Scheduled track information of the arriving transit vehicle."""

    service_date: Optional[int] = FieldInfo(alias="serviceDate", default=None)
    """
    Time, in milliseconds since the Unix epoch, of midnight for the start of the
    service date for the trip.
    """

    situation_ids: Optional[List[str]] = FieldInfo(alias="situationIds", default=None)
    """References to situation elements (if any) applicable to this arrival."""

    status: Optional[str] = None
    """Current status of the arrival."""

    stop_id: Optional[str] = FieldInfo(alias="stopId", default=None)
    """The ID of the stop the vehicle is arriving at."""

    stop_sequence: Optional[int] = FieldInfo(alias="stopSequence", default=None)
    """
    Index of the stop into the sequence of stops that make up the trip for this
    arrival.
    """

    total_stops_in_trip: Optional[int] = FieldInfo(alias="totalStopsInTrip", default=None)
    """Total number of stops visited on the trip for this arrival."""

    trip_headsign: Optional[str] = FieldInfo(alias="tripHeadsign", default=None)
    """
    Optional trip headsign that potentially overrides the trip headsign in the
    referenced trip element.
    """

    trip_id: Optional[str] = FieldInfo(alias="tripId", default=None)
    """The ID of the trip for the arriving vehicle."""

    trip_status: Optional[ArrivalAndDepartureListResponseDataEntryArrivalsAndDepartureTripStatus] = FieldInfo(
        alias="tripStatus", default=None
    )
    """Trip-specific status for the arriving transit vehicle."""

    vehicle_id: Optional[str] = FieldInfo(alias="vehicleId", default=None)
    """ID of the transit vehicle serving this trip."""


class ArrivalAndDepartureListResponseDataEntry(BaseModel):
    arrivals_and_departures: Optional[List[ArrivalAndDepartureListResponseDataEntryArrivalsAndDeparture]] = FieldInfo(
        alias="arrivalsAndDepartures", default=None
    )


class ArrivalAndDepartureListResponseData(BaseModel):
    entry: Optional[ArrivalAndDepartureListResponseDataEntry] = None

    references: Optional[References] = None


class ArrivalAndDepartureListResponse(ResponseWrapper):
    data: Optional[ArrivalAndDepartureListResponseData] = None
