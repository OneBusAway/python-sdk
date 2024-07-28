# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel
from .shared.references import References
from .shared.response_wrapper import ResponseWrapper

__all__ = ["StopIDsForAgencyListResponse", "StopIDsForAgencyListResponseData"]


class StopIDsForAgencyListResponseData(BaseModel):
    limit_exceeded: Optional[bool] = FieldInfo(alias="limitExceeded", default=None)

    list: Optional[List[str]] = None

    references: Optional[References] = None


class StopIDsForAgencyListResponse(ResponseWrapper):
    data: Optional[StopIDsForAgencyListResponseData] = None
