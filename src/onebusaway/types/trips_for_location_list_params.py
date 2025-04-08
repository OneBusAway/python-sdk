# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["TripsForLocationListParams"]


class TripsForLocationListParams(TypedDict, total=False):
    lat: Required[float]
    """The latitude coordinate of the search center"""

    lat_span: Required[Annotated[float, PropertyInfo(alias="latSpan")]]
    """Latitude span of the search bounding box"""

    lon: Required[float]
    """The longitude coordinate of the search center"""

    lon_span: Required[Annotated[float, PropertyInfo(alias="lonSpan")]]
    """Longitude span of the search bounding box"""

    include_schedule: Annotated[bool, PropertyInfo(alias="includeSchedule")]
    """Whether to include full schedule elements in the tripDetails section.

    Defaults to false.
    """

    include_trip: Annotated[bool, PropertyInfo(alias="includeTrip")]
    """Whether to include full trip elements in the references section.

    Defaults to false.
    """

    time: int
    """Specific time for the query. Defaults to the current time."""
