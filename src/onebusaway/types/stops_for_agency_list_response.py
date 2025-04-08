# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

from typing import List, Optional

from .shared.response_wrapper import ResponseWrapper

from .shared.references import References

from typing_extensions import Literal
from pydantic import Field as FieldInfo

__all__ = ["StopsForAgencyListResponse", "StopsForAgencyListResponseList"]

class StopsForAgencyListResponseList(BaseModel):
    id: str

    lat: float

    lon: float

    name: str

    parent: str

    route_ids: List[str] = FieldInfo(alias = "routeIds")

    static_route_ids: List[str] = FieldInfo(alias = "staticRouteIds")

    code: Optional[str] = None

    direction: Optional[str] = None

    location_type: Optional[int] = FieldInfo(alias = "locationType", default = None)

    wheelchair_boarding: Optional[str] = FieldInfo(alias = "wheelchairBoarding", default = None)

class StopsForAgencyListResponse(ResponseWrapper):
    limit_exceeded: bool = FieldInfo(alias = "limitExceeded")

    list: List[StopsForAgencyListResponseList]

    references: References

    out_of_range: Optional[bool] = FieldInfo(alias = "outOfRange", default = None)