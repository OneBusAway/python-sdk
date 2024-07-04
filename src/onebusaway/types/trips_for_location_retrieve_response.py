# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel
from .shared.references import References
from .shared.response_wrapper import ResponseWrapper

__all__ = [
    "TripsForLocationRetrieveResponse",
    "TripsForLocationRetrieveResponseData",
    "TripsForLocationRetrieveResponseDataList",
]


class TripsForLocationRetrieveResponseDataList(BaseModel):
    frequency: Optional[str] = None

    service_date: Optional[int] = FieldInfo(alias="serviceDate", default=None)

    situation_ids: Optional[List[str]] = FieldInfo(alias="situationIds", default=None)

    trip_id: Optional[str] = FieldInfo(alias="tripId", default=None)


class TripsForLocationRetrieveResponseData(BaseModel):
    limit_exceeded: Optional[bool] = FieldInfo(alias="limitExceeded", default=None)
    """Indicates if the limit of trips has been exceeded"""

    list: Optional[List[TripsForLocationRetrieveResponseDataList]] = None

    out_of_range: Optional[bool] = FieldInfo(alias="outOfRange", default=None)
    """Indicates if the search location is out of range"""

    references: Optional[References] = None


class TripsForLocationRetrieveResponse(ResponseWrapper):
    data: Optional[TripsForLocationRetrieveResponseData] = None
