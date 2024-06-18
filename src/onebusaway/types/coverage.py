# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.


from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["Coverage"]


class Coverage(BaseModel):
    agency_id: str = FieldInfo(alias="agencyId")

    lat: float

    lat_span: float = FieldInfo(alias="latSpan")

    lon: float

    lon_span: float = FieldInfo(alias="lonSpan")
