# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel
from .shared.references import References
from .shared.response_wrapper import ResponseWrapper

__all__ = ["RouteRetrieveResponse", "RouteRetrieveResponseData", "RouteRetrieveResponseDataEntry"]


class RouteRetrieveResponseDataEntry(BaseModel):
    id: Optional[str] = None

    agency_id: Optional[str] = FieldInfo(alias="agencyId", default=None)

    color: Optional[str] = None

    description: Optional[str] = None

    long_name: Optional[str] = FieldInfo(alias="longName", default=None)

    short_name: Optional[str] = FieldInfo(alias="shortName", default=None)

    text_color: Optional[str] = FieldInfo(alias="textColor", default=None)

    type: Optional[int] = None

    url: Optional[str] = None


class RouteRetrieveResponseData(BaseModel):
    entry: Optional[RouteRetrieveResponseDataEntry] = None

    references: Optional[References] = None


class RouteRetrieveResponse(ResponseWrapper):
    data: Optional[RouteRetrieveResponseData] = None
