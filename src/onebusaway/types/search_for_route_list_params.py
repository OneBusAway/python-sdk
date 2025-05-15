# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict, Required, Annotated

from .._utils import PropertyInfo

from typing_extensions import Literal, TypedDict, Required, Annotated
from .._types import FileTypes
from .._utils import PropertyInfo

__all__ = ["SearchForRouteListParams"]

class SearchForRouteListParams(TypedDict, total=False):
    input: Required[str]
    """The string to search for."""

    max_count: Annotated[int, PropertyInfo(alias="maxCount")]
    """The max number of results to return. Defaults to 20."""