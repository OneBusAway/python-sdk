# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

from typing import Optional

from .shared.references import References

from .shared.response_wrapper import ResponseWrapper

from typing_extensions import Literal
from pydantic import Field as FieldInfo

__all__ = ["AgencyRetrieveResponse", "AgencyRetrieveResponseData", "AgencyRetrieveResponseDataEntry"]

class AgencyRetrieveResponseDataEntry(BaseModel):
    id: str

    name: str

    timezone: str

    url: str

    disclaimer: Optional[str] = None

    email: Optional[str] = None

    fare_url: Optional[str] = FieldInfo(alias = "fareUrl", default = None)

    lang: Optional[str] = None

    phone: Optional[str] = None

    private_service: Optional[bool] = FieldInfo(alias = "privateService", default = None)

class AgencyRetrieveResponseData(BaseModel):
    entry: AgencyRetrieveResponseDataEntry

    limit_exceeded: bool = FieldInfo(alias = "limitExceeded")

    references: References

class AgencyRetrieveResponse(ResponseWrapper):
    data: AgencyRetrieveResponseData