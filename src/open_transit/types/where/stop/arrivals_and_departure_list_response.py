# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = [
    "ArrivalsAndDepartureListResponse",
    "Data",
    "DataEntry",
    "DataEntryArrivalsAndDeparture",
    "DataEntryArrivalsAndDepartureTripStatus",
    "DataEntryArrivalsAndDepartureTripStatusLastKnownLocation",
    "DataEntryArrivalsAndDepartureTripStatusPosition",
    "DataEntryReferences",
    "DataEntryReferencesAgency",
    "DataEntryReferencesRoute",
    "DataEntryReferencesStop",
    "DataEntryReferencesTrip",
]


class DataEntryArrivalsAndDepartureTripStatusLastKnownLocation(BaseModel):
    lat: Optional[float] = None

    lon: Optional[float] = None


class DataEntryArrivalsAndDepartureTripStatusPosition(BaseModel):
    lat: Optional[float] = None

    lon: Optional[float] = None


class DataEntryArrivalsAndDepartureTripStatus(BaseModel):
    active_trip_id: Optional[str] = FieldInfo(alias="activeTripId", default=None)

    block_trip_sequence: Optional[int] = FieldInfo(alias="blockTripSequence", default=None)

    closest_stop: Optional[str] = FieldInfo(alias="closestStop", default=None)

    closest_stop_time_offset: Optional[int] = FieldInfo(alias="closestStopTimeOffset", default=None)

    distance_along_trip: Optional[float] = FieldInfo(alias="distanceAlongTrip", default=None)

    frequency: Optional[str] = None

    last_known_distance_along_trip: Optional[float] = FieldInfo(alias="lastKnownDistanceAlongTrip", default=None)

    last_known_location: Optional[DataEntryArrivalsAndDepartureTripStatusLastKnownLocation] = FieldInfo(
        alias="lastKnownLocation", default=None
    )

    last_known_orientation: Optional[float] = FieldInfo(alias="lastKnownOrientation", default=None)

    last_location_update_time: Optional[int] = FieldInfo(alias="lastLocationUpdateTime", default=None)

    last_update_time: Optional[int] = FieldInfo(alias="lastUpdateTime", default=None)

    next_stop: Optional[str] = FieldInfo(alias="nextStop", default=None)

    next_stop_time_offset: Optional[int] = FieldInfo(alias="nextStopTimeOffset", default=None)

    occupancy_capacity: Optional[int] = FieldInfo(alias="occupancyCapacity", default=None)

    occupancy_count: Optional[int] = FieldInfo(alias="occupancyCount", default=None)

    occupancy_status: Optional[str] = FieldInfo(alias="occupancyStatus", default=None)

    orientation: Optional[float] = None

    phase: Optional[str] = None

    position: Optional[DataEntryArrivalsAndDepartureTripStatusPosition] = None

    predicted: Optional[bool] = None

    scheduled_distance_along_trip: Optional[float] = FieldInfo(alias="scheduledDistanceAlongTrip", default=None)

    schedule_deviation: Optional[int] = FieldInfo(alias="scheduleDeviation", default=None)

    service_date: Optional[int] = FieldInfo(alias="serviceDate", default=None)

    situation_ids: Optional[List[str]] = FieldInfo(alias="situationIds", default=None)

    status: Optional[str] = None

    total_distance_along_trip: Optional[float] = FieldInfo(alias="totalDistanceAlongTrip", default=None)

    vehicle_id: Optional[str] = FieldInfo(alias="vehicleId", default=None)


class DataEntryArrivalsAndDeparture(BaseModel):
    actual_track: Optional[str] = FieldInfo(alias="actualTrack", default=None)

    arrival_enabled: Optional[bool] = FieldInfo(alias="arrivalEnabled", default=None)

    block_trip_sequence: Optional[int] = FieldInfo(alias="blockTripSequence", default=None)

    departure_enabled: Optional[bool] = FieldInfo(alias="departureEnabled", default=None)

    distance_from_stop: Optional[float] = FieldInfo(alias="distanceFromStop", default=None)

    frequency: Optional[str] = None

    historical_occupancy: Optional[str] = FieldInfo(alias="historicalOccupancy", default=None)

    last_update_time: Optional[int] = FieldInfo(alias="lastUpdateTime", default=None)

    number_of_stops_away: Optional[int] = FieldInfo(alias="numberOfStopsAway", default=None)

    occupancy_status: Optional[str] = FieldInfo(alias="occupancyStatus", default=None)

    predicted: Optional[bool] = None

    predicted_arrival_interval: Optional[str] = FieldInfo(alias="predictedArrivalInterval", default=None)

    predicted_arrival_time: Optional[int] = FieldInfo(alias="predictedArrivalTime", default=None)

    predicted_departure_interval: Optional[str] = FieldInfo(alias="predictedDepartureInterval", default=None)

    predicted_departure_time: Optional[int] = FieldInfo(alias="predictedDepartureTime", default=None)

    predicted_occupancy: Optional[str] = FieldInfo(alias="predictedOccupancy", default=None)

    route_id: Optional[str] = FieldInfo(alias="routeId", default=None)

    route_long_name: Optional[str] = FieldInfo(alias="routeLongName", default=None)

    route_short_name: Optional[str] = FieldInfo(alias="routeShortName", default=None)

    scheduled_arrival_interval: Optional[str] = FieldInfo(alias="scheduledArrivalInterval", default=None)

    scheduled_arrival_time: Optional[int] = FieldInfo(alias="scheduledArrivalTime", default=None)

    scheduled_departure_interval: Optional[str] = FieldInfo(alias="scheduledDepartureInterval", default=None)

    scheduled_departure_time: Optional[int] = FieldInfo(alias="scheduledDepartureTime", default=None)

    scheduled_track: Optional[str] = FieldInfo(alias="scheduledTrack", default=None)

    service_date: Optional[int] = FieldInfo(alias="serviceDate", default=None)

    situation_ids: Optional[List[str]] = FieldInfo(alias="situationIds", default=None)

    status: Optional[str] = None

    stop_id: Optional[str] = FieldInfo(alias="stopId", default=None)

    stop_sequence: Optional[int] = FieldInfo(alias="stopSequence", default=None)

    total_stops_in_trip: Optional[int] = FieldInfo(alias="totalStopsInTrip", default=None)

    trip_headsign: Optional[str] = FieldInfo(alias="tripHeadsign", default=None)

    trip_id: Optional[str] = FieldInfo(alias="tripId", default=None)

    trip_status: Optional[DataEntryArrivalsAndDepartureTripStatus] = FieldInfo(alias="tripStatus", default=None)

    vehicle_id: Optional[str] = FieldInfo(alias="vehicleId", default=None)


class DataEntryReferencesAgency(BaseModel):
    id: str

    name: str

    timezone: str

    url: str

    disclaimer: Optional[str] = None

    email: Optional[str] = None

    fare_url: Optional[str] = FieldInfo(alias="fareUrl", default=None)

    lang: Optional[str] = None

    phone: Optional[str] = None

    private_service: Optional[bool] = FieldInfo(alias="privateService", default=None)


class DataEntryReferencesRoute(BaseModel):
    id: Optional[str] = None

    agency_id: Optional[str] = FieldInfo(alias="agencyId", default=None)

    color: Optional[str] = None

    description: Optional[str] = None

    long_name: Optional[str] = FieldInfo(alias="longName", default=None)

    null_safe_short_name: Optional[str] = FieldInfo(alias="nullSafeShortName", default=None)

    short_name: Optional[str] = FieldInfo(alias="shortName", default=None)

    text_color: Optional[str] = FieldInfo(alias="textColor", default=None)

    type: Optional[int] = None

    url: Optional[str] = None


class DataEntryReferencesStop(BaseModel):
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


class DataEntryReferencesTrip(BaseModel):
    id: str

    route_id: str = FieldInfo(alias="routeId")

    block_id: Optional[str] = FieldInfo(alias="blockId", default=None)

    direction_id: Optional[str] = FieldInfo(alias="directionId", default=None)

    peak_offpeak: Optional[int] = FieldInfo(alias="peakOffpeak", default=None)

    route_short_name: Optional[str] = FieldInfo(alias="routeShortName", default=None)

    service_id: Optional[str] = FieldInfo(alias="serviceId", default=None)

    shape_id: Optional[str] = FieldInfo(alias="shapeId", default=None)

    time_zone: Optional[str] = FieldInfo(alias="timeZone", default=None)

    trip_headsign: Optional[str] = FieldInfo(alias="tripHeadsign", default=None)

    trip_short_name: Optional[str] = FieldInfo(alias="tripShortName", default=None)


class DataEntryReferences(BaseModel):
    agencies: Optional[List[DataEntryReferencesAgency]] = None

    routes: Optional[List[DataEntryReferencesRoute]] = None

    situations: Optional[List[object]] = None

    stops: Optional[List[DataEntryReferencesStop]] = None

    stop_times: Optional[List[object]] = FieldInfo(alias="stopTimes", default=None)

    trips: Optional[List[DataEntryReferencesTrip]] = None


class DataEntry(BaseModel):
    arrivals_and_departures: Optional[List[DataEntryArrivalsAndDeparture]] = FieldInfo(
        alias="arrivalsAndDepartures", default=None
    )

    references: Optional[DataEntryReferences] = None


class Data(BaseModel):
    entry: Optional[DataEntry] = None


class ArrivalsAndDepartureListResponse(BaseModel):
    code: int

    current_time: int = FieldInfo(alias="currentTime")

    text: str

    version: int

    data: Optional[Data] = None
