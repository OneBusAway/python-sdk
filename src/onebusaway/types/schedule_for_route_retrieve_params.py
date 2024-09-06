# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["ScheduleForRouteRetrieveParams"]


class ScheduleForRouteRetrieveParams(TypedDict, total=False):
    date: str
    """
    The date for which you want to request a schedule in the format YYYY-MM-DD
    (optional, defaults to current date)
    """
