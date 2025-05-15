# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict, Required, Annotated

from .._utils import PropertyInfo

from typing_extensions import Literal, TypedDict, Required, Annotated
from .._types import FileTypes
from .._utils import PropertyInfo

__all__ = ["RoutesForLocationListParams"]

class RoutesForLocationListParams(TypedDict, total=False):
    lat: Required[float]

    lon: Required[float]

    lat_span: Annotated[float, PropertyInfo(alias="latSpan")]

    lon_span: Annotated[float, PropertyInfo(alias="lonSpan")]

    query: str

    radius: float