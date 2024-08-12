# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel
from .shared.references import References
from .shared.response_wrapper import ResponseWrapper

__all__ = ["ShapeRetrieveResponse", "ShapeRetrieveResponseData", "ShapeRetrieveResponseDataEntry"]


class ShapeRetrieveResponseDataEntry(BaseModel):
    length: int

    points: str
    """Encoded polyline format representing the shape of the path"""

    levels: Optional[str] = None


class ShapeRetrieveResponseData(BaseModel):
    entry: ShapeRetrieveResponseDataEntry

    references: References


class ShapeRetrieveResponse(ResponseWrapper):
    data: ShapeRetrieveResponseData
