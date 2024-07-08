# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["StopsForRouteListParams"]


class StopsForRouteListParams(TypedDict, total=False):
    include_polylines: Annotated[bool, PropertyInfo(alias="includePolylines")]
    """Include polyline elements in the response (default true)"""

    time: str
    """Specify service date (YYYY-MM-DD or epoch) (default today)"""
