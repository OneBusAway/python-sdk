# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["TripDetailRetrieveParams"]


class TripDetailRetrieveParams(TypedDict, total=False):
    include_schedule: Annotated[bool, PropertyInfo(alias="includeSchedule")]
    """
    Whether to include the full schedule element in the tripDetails section
    (defaults to true).
    """

    include_status: Annotated[bool, PropertyInfo(alias="includeStatus")]
    """
    Whether to include the full status element in the tripDetails section (defaults
    to true).
    """

    include_trip: Annotated[bool, PropertyInfo(alias="includeTrip")]
    """
    Whether to include the full trip element in the references section (defaults to
    true).
    """

    service_date: Annotated[int, PropertyInfo(alias="serviceDate")]
    """Service date for the trip as Unix time in milliseconds (optional)."""

    time: int
    """Time parameter to query the system at a specific time (optional)."""
