# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["ReportProblemWithStopRetrieveParams"]


class ReportProblemWithStopRetrieveParams(TypedDict, total=False):
    code: Literal["stop_name_wrong", "stop_number_wrong", "stop_location_wrong", "route_or_trip_missing", "other"]
    """A string code identifying the nature of the problem"""

    user_comment: Annotated[str, PropertyInfo(alias="userComment")]
    """Additional comment text supplied by the user describing the problem"""

    user_lat: Annotated[float, PropertyInfo(alias="userLat")]
    """The reporting user’s current latitude"""

    user_location_accuracy: Annotated[float, PropertyInfo(alias="userLocationAccuracy")]
    """The reporting user’s location accuracy, in meters"""

    user_lon: Annotated[float, PropertyInfo(alias="userLon")]
    """The reporting user’s current longitude"""
