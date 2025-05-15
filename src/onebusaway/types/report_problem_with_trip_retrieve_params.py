# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["ReportProblemWithTripRetrieveParams"]


class ReportProblemWithTripRetrieveParams(TypedDict, total=False):
    code: Literal[
        "vehicle_never_came",
        "vehicle_came_early",
        "vehicle_came_late",
        "wrong_headsign",
        "vehicle_does_not_stop_here",
        "other",
    ]
    """A string code identifying the nature of the problem"""

    service_date: Annotated[int, PropertyInfo(alias="serviceDate")]
    """The service date of the trip"""

    stop_id: Annotated[str, PropertyInfo(alias="stopID")]
    """A stop ID indicating where the user is experiencing the problem"""

    user_comment: Annotated[str, PropertyInfo(alias="userComment")]
    """Additional comment text supplied by the user describing the problem"""

    user_lat: Annotated[float, PropertyInfo(alias="userLat")]
    """The reporting user’s current latitude"""

    user_location_accuracy: Annotated[float, PropertyInfo(alias="userLocationAccuracy")]
    """The reporting user’s location accuracy, in meters"""

    user_lon: Annotated[float, PropertyInfo(alias="userLon")]
    """The reporting user’s current longitude"""

    user_on_vehicle: Annotated[bool, PropertyInfo(alias="userOnVehicle")]
    """Indicator if the user is on the transit vehicle experiencing the problem"""

    user_vehicle_number: Annotated[str, PropertyInfo(alias="userVehicleNumber")]
    """The vehicle number, as reported by the user"""

    vehicle_id: Annotated[str, PropertyInfo(alias="vehicleID")]
    """The vehicle actively serving the trip"""
