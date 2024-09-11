# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import datetime
from typing import Union
from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["ScheduleForRouteRetrieveParams"]


class ScheduleForRouteRetrieveParams(TypedDict, total=False):
    date: Annotated[Union[str, datetime.date], PropertyInfo(format="iso8601")]
    """
    The date for which you want to request a schedule in the format YYYY-MM-DD
    (optional, defaults to current date)
    """
