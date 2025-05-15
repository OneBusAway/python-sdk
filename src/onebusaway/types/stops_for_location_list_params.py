# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["StopsForLocationListParams"]


class StopsForLocationListParams(TypedDict, total=False):
    lat: Required[float]

    lon: Required[float]

    lat_span: Annotated[float, PropertyInfo(alias="latSpan")]
    """An alternative to radius to set the search bounding box (optional)"""

    lon_span: Annotated[float, PropertyInfo(alias="lonSpan")]
    """An alternative to radius to set the search bounding box (optional)"""

    query: str
    """A search query string to filter the results"""

    radius: float
    """The radius in meters to search within"""
