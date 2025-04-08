# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["TripsForRouteListParams"]


class TripsForRouteListParams(TypedDict, total=False):
    include_schedule: Annotated[bool, PropertyInfo(alias="includeSchedule")]
    """Determine whether full schedule elements are included. Defaults to false."""

    include_status: Annotated[bool, PropertyInfo(alias="includeStatus")]
    """
    Determine whether full tripStatus elements with real-time information are
    included. Defaults to false.
    """

    time: int
    """Query the system at a specific time. Useful for testing."""
