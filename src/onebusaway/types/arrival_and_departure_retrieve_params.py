# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["ArrivalAndDepartureRetrieveParams"]


class ArrivalAndDepartureRetrieveParams(TypedDict, total=False):
    service_date: Required[Annotated[int, PropertyInfo(alias="serviceDate")]]

    trip_id: Required[Annotated[str, PropertyInfo(alias="tripId")]]

    stop_sequence: Annotated[int, PropertyInfo(alias="stopSequence")]

    time: int

    vehicle_id: Annotated[str, PropertyInfo(alias="vehicleId")]
