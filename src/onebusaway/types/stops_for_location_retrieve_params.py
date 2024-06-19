# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["StopsForLocationRetrieveParams"]


class StopsForLocationRetrieveParams(TypedDict, total=False):
    key: Required[str]

    lat: float

    lon: float
