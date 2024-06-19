# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .where import (
    WhereResource,
    AsyncWhereResource,
    WhereResourceWithRawResponse,
    AsyncWhereResourceWithRawResponse,
    WhereResourceWithStreamingResponse,
    AsyncWhereResourceWithStreamingResponse,
)
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from .where.where import WhereResource, AsyncWhereResource

__all__ = ["APIResource", "AsyncAPIResource"]


class APIResource(SyncAPIResource):
    @cached_property
    def where(self) -> WhereResource:
        return WhereResource(self._client)

    @cached_property
    def with_raw_response(self) -> APIResourceWithRawResponse:
        return APIResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> APIResourceWithStreamingResponse:
        return APIResourceWithStreamingResponse(self)


class AsyncAPIResource(AsyncAPIResource):
    @cached_property
    def where(self) -> AsyncWhereResource:
        return AsyncWhereResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncAPIResourceWithRawResponse:
        return AsyncAPIResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAPIResourceWithStreamingResponse:
        return AsyncAPIResourceWithStreamingResponse(self)


class APIResourceWithRawResponse:
    def __init__(self, api: APIResource) -> None:
        self._api = api

    @cached_property
    def where(self) -> WhereResourceWithRawResponse:
        return WhereResourceWithRawResponse(self._api.where)


class AsyncAPIResourceWithRawResponse:
    def __init__(self, api: AsyncAPIResource) -> None:
        self._api = api

    @cached_property
    def where(self) -> AsyncWhereResourceWithRawResponse:
        return AsyncWhereResourceWithRawResponse(self._api.where)


class APIResourceWithStreamingResponse:
    def __init__(self, api: APIResource) -> None:
        self._api = api

    @cached_property
    def where(self) -> WhereResourceWithStreamingResponse:
        return WhereResourceWithStreamingResponse(self._api.where)


class AsyncAPIResourceWithStreamingResponse:
    def __init__(self, api: AsyncAPIResource) -> None:
        self._api = api

    @cached_property
    def where(self) -> AsyncWhereResourceWithStreamingResponse:
        return AsyncWhereResourceWithStreamingResponse(self._api.where)
