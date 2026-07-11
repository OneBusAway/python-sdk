# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["RoutesForLocationListParams"]


class RoutesForLocationListParams(TypedDict, total=False):
    lat: float
    """If omitted, defaults to 0.0."""

    lat_span: Annotated[float, PropertyInfo(alias="latSpan")]

    lon: float
    """If omitted, defaults to 0.0."""

    lon_span: Annotated[float, PropertyInfo(alias="lonSpan")]

    query: str

    radius: float
