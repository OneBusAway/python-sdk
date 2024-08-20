# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = [
    "References",
    "Agency",
    "Route",
    "Situation",
    "SituationActiveWindow",
    "SituationAllAffect",
    "SituationConsequence",
    "SituationConsequenceConditionDetails",
    "SituationConsequenceConditionDetailsDiversionPath",
    "SituationDescription",
    "SituationPublicationWindow",
    "SituationSummary",
    "SituationURL",
    "Stop",
    "StopTime",
    "Trip",
]


class Agency(BaseModel):
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


class Route(BaseModel):
    id: str

    agency_id: str = FieldInfo(alias="agencyId")

    type: int

    color: Optional[str] = None

    description: Optional[str] = None

    long_name: Optional[str] = FieldInfo(alias="longName", default=None)

    null_safe_short_name: Optional[str] = FieldInfo(alias="nullSafeShortName", default=None)

    short_name: Optional[str] = FieldInfo(alias="shortName", default=None)

    text_color: Optional[str] = FieldInfo(alias="textColor", default=None)

    url: Optional[str] = None


class SituationActiveWindow(BaseModel):
    from_: Optional[int] = FieldInfo(alias="from", default=None)
    """Start time of the active window as a Unix timestamp."""

    to: Optional[int] = None
    """End time of the active window as a Unix timestamp."""


class SituationAllAffect(BaseModel):
    agency_id: Optional[str] = FieldInfo(alias="agencyId", default=None)
    """Identifier for the agency."""

    application_id: Optional[str] = FieldInfo(alias="applicationId", default=None)
    """Identifier for the application."""

    direction_id: Optional[str] = FieldInfo(alias="directionId", default=None)
    """Identifier for the direction."""

    route_id: Optional[str] = FieldInfo(alias="routeId", default=None)
    """Identifier for the route."""

    stop_id: Optional[str] = FieldInfo(alias="stopId", default=None)
    """Identifier for the stop."""

    trip_id: Optional[str] = FieldInfo(alias="tripId", default=None)
    """Identifier for the trip."""


class SituationConsequenceConditionDetailsDiversionPath(BaseModel):
    length: Optional[int] = None
    """Length of the diversion path."""

    levels: Optional[str] = None
    """Levels of the diversion path."""

    points: Optional[str] = None
    """Points of the diversion path."""


class SituationConsequenceConditionDetails(BaseModel):
    diversion_path: Optional[SituationConsequenceConditionDetailsDiversionPath] = FieldInfo(
        alias="diversionPath", default=None
    )

    diversion_stop_ids: Optional[List[str]] = FieldInfo(alias="diversionStopIds", default=None)


class SituationConsequence(BaseModel):
    condition: Optional[str] = None
    """Condition of the consequence."""

    condition_details: Optional[SituationConsequenceConditionDetails] = FieldInfo(
        alias="conditionDetails", default=None
    )


class SituationDescription(BaseModel):
    lang: Optional[str] = None
    """Language of the description."""

    value: Optional[str] = None
    """Longer description of the situation."""


class SituationPublicationWindow(BaseModel):
    from_: int = FieldInfo(alias="from")
    """Start time of the time window as a Unix timestamp."""

    to: int
    """End time of the time window as a Unix timestamp."""


class SituationSummary(BaseModel):
    lang: Optional[str] = None
    """Language of the summary."""

    value: Optional[str] = None
    """Short summary of the situation."""


class SituationURL(BaseModel):
    lang: Optional[str] = None
    """Language of the URL."""

    value: Optional[str] = None
    """URL for more information about the situation."""


class Situation(BaseModel):
    id: str
    """Unique identifier for the situation."""

    creation_time: int = FieldInfo(alias="creationTime")
    """Unix timestamp of when this situation was created."""

    active_windows: Optional[List[SituationActiveWindow]] = FieldInfo(alias="activeWindows", default=None)

    all_affects: Optional[List[SituationAllAffect]] = FieldInfo(alias="allAffects", default=None)

    consequence_message: Optional[str] = FieldInfo(alias="consequenceMessage", default=None)
    """Message regarding the consequence of the situation."""

    consequences: Optional[List[SituationConsequence]] = None

    description: Optional[SituationDescription] = None

    publication_windows: Optional[List[SituationPublicationWindow]] = FieldInfo(
        alias="publicationWindows", default=None
    )

    reason: Optional[
        Literal["equipmentReason", "environmentReason", "personnelReason", "miscellaneousReason", "securityAlert"]
    ] = None
    """Reason for the service alert, taken from TPEG codes."""

    severity: Optional[str] = None
    """Severity of the situation."""

    summary: Optional[SituationSummary] = None

    url: Optional[SituationURL] = None


class Stop(BaseModel):
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


class StopTime(BaseModel):
    arrival_time: Optional[int] = FieldInfo(alias="arrivalTime", default=None)

    departure_time: Optional[int] = FieldInfo(alias="departureTime", default=None)

    distance_along_trip: Optional[float] = FieldInfo(alias="distanceAlongTrip", default=None)

    historical_occupancy: Optional[str] = FieldInfo(alias="historicalOccupancy", default=None)

    stop_headsign: Optional[str] = FieldInfo(alias="stopHeadsign", default=None)

    stop_id: Optional[str] = FieldInfo(alias="stopId", default=None)


class Trip(BaseModel):
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


class References(BaseModel):
    agencies: List[Agency]

    routes: List[Route]

    situations: List[Situation]

    stops: List[Stop]

    stop_times: List[StopTime] = FieldInfo(alias="stopTimes")

    trips: List[Trip]
