# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

from typing import Optional

from .shared.references import References

from .shared.response_wrapper import ResponseWrapper

from typing_extensions import Literal
from pydantic import Field as FieldInfo

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