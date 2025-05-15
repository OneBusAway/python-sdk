# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["SearchForStopListParams"]


class SearchForStopListParams(TypedDict, total=False):
    input: Required[str]
    """The string to search for."""

    max_count: Annotated[int, PropertyInfo(alias="maxCount")]
    """The max number of results to return. Defaults to 20."""
