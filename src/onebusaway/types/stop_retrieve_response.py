# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel
from .shared.references import References
from .shared.response_wrapper import ResponseWrapper

__all__ = ["StopRetrieveResponse", "StopRetrieveResponseData", "StopRetrieveResponseDataEntry"]


class StopRetrieveResponseDataEntry(BaseModel):
    id: str

    lat: float

    location_type: int = FieldInfo(alias="locationType")

    lon: float

    name: str

    parent: str

    route_ids: List[str] = FieldInfo(alias="routeIds")

    static_route_ids: List[str] = FieldInfo(alias="staticRouteIds")

    code: Optional[str] = None

    direction: Optional[str] = None

    wheelchair_boarding: Optional[str] = FieldInfo(alias="wheelchairBoarding", default=None)


class StopRetrieveResponseData(BaseModel):
    entry: StopRetrieveResponseDataEntry

    references: References


class StopRetrieveResponse(ResponseWrapper):
    data: StopRetrieveResponseData
