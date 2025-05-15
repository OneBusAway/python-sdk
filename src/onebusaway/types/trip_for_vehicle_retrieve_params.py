# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["TripForVehicleRetrieveParams"]


class TripForVehicleRetrieveParams(TypedDict, total=False):
    include_schedule: Annotated[bool, PropertyInfo(alias="includeSchedule")]
    """
    Determines whether full <schedule/> element is included in the <tripDetails/>
    section. Defaults to false.
    """

    include_status: Annotated[bool, PropertyInfo(alias="includeStatus")]
    """
    Determines whether the full <status/> element is included in the <tripDetails/>
    section. Defaults to true.
    """

    include_trip: Annotated[bool, PropertyInfo(alias="includeTrip")]
    """Determines whether full <trip/> element is included in the <references/>
    section.

    Defaults to false.
    """

    time: int
    """Time parameter to query the system at a specific time (optional)."""
