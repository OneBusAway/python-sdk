# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["ArrivalsAndDeparturesForLocationListParams"]


class ArrivalsAndDeparturesForLocationListParams(TypedDict, total=False):
    lat: Required[float]
    """The latitude coordinate of the search center."""

    lon: Required[float]
    """The longitude coordinate of the search center."""

    empty_returns_not_found: Annotated[bool, PropertyInfo(alias="emptyReturnsNotFound")]
    """If true, returns a 404 Not Found error instead of an empty result."""

    lat_span: Annotated[float, PropertyInfo(alias="latSpan")]
    """Sets the latitude limits of the search bounding box."""

    lon_span: Annotated[float, PropertyInfo(alias="lonSpan")]
    """Sets the longitude limits of the search bounding box."""

    max_count: Annotated[int, PropertyInfo(alias="maxCount")]
    """The max size of the list of nearby stops and arrivals to return.

    Defaults to 250, max 1000.
    """

    minutes_after: Annotated[int, PropertyInfo(alias="minutesAfter")]
    """Include arrivals and departures this many minutes after the query time."""

    minutes_before: Annotated[int, PropertyInfo(alias="minutesBefore")]
    """Include arrivals and departures this many minutes before the query time."""

    radius: float
    """The search radius in meters."""

    route_type: Annotated[str, PropertyInfo(alias="routeType")]
    """Optional list of GTFS routeTypes to filter by (comma delimited) e.g. "1,2,3"."""

    time: int
    """By default, returns the status right now.

    Can be queried at a specific time (milliseconds since epoch) for testing.
    """
