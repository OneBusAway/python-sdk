# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import datetime

from typing_extensions import TypedDict, Annotated

from typing import Union

from .._utils import PropertyInfo

from typing_extensions import Literal, TypedDict, Required, Annotated
from .._types import FileTypes
from .._utils import PropertyInfo

__all__ = ["ScheduleForStopRetrieveParams"]

class ScheduleForStopRetrieveParams(TypedDict, total=False):
    date: Annotated[Union[str, datetime.date], PropertyInfo(format = "iso8601")]
    """
    The date for which you want to request a schedule in the format YYYY-MM-DD
    (optional, defaults to the current date)
    """