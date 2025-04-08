# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import datetime
from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["ArrivalAndDepartureListParams"]


class ArrivalAndDepartureListParams(TypedDict, total=False):
    minutes_after: Annotated[int, PropertyInfo(alias="minutesAfter")]
    """Include vehicles arriving or departing in the next n minutes."""

    minutes_before: Annotated[int, PropertyInfo(alias="minutesBefore")]
    """Include vehicles having arrived or departed in the previous n minutes."""

    time: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """The specific time for querying the system status."""
