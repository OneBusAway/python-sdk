# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.shape_retrieve_response import ShapeRetrieveResponse

__all__ = ["ShapeResource", "AsyncShapeResource"]


class ShapeResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ShapeResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/OneBusAway/python-sdk#accessing-raw-response-data-eg-headers
        """
        return ShapeResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ShapeResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/OneBusAway/python-sdk#with_streaming_response
        """
        return ShapeResourceWithStreamingResponse(self)

    def retrieve(
        self,
        shape_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ShapeRetrieveResponse:
        """
        Retrieve a shape (the path traveled by a transit vehicle) by ID.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not shape_id:
            raise ValueError(f"Expected a non-empty value for `shape_id` but received {shape_id!r}")
        return self._get(
            f"/api/where/shape/{shape_id}.json",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ShapeRetrieveResponse,
        )


class AsyncShapeResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncShapeResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/OneBusAway/python-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncShapeResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncShapeResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/OneBusAway/python-sdk#with_streaming_response
        """
        return AsyncShapeResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        shape_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ShapeRetrieveResponse:
        """
        Retrieve a shape (the path traveled by a transit vehicle) by ID.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not shape_id:
            raise ValueError(f"Expected a non-empty value for `shape_id` but received {shape_id!r}")
        return await self._get(
            f"/api/where/shape/{shape_id}.json",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ShapeRetrieveResponse,
        )


class ShapeResourceWithRawResponse:
    def __init__(self, shape: ShapeResource) -> None:
        self._shape = shape

        self.retrieve = to_raw_response_wrapper(
            shape.retrieve,
        )


class AsyncShapeResourceWithRawResponse:
    def __init__(self, shape: AsyncShapeResource) -> None:
        self._shape = shape

        self.retrieve = async_to_raw_response_wrapper(
            shape.retrieve,
        )


class ShapeResourceWithStreamingResponse:
    def __init__(self, shape: ShapeResource) -> None:
        self._shape = shape

        self.retrieve = to_streamed_response_wrapper(
            shape.retrieve,
        )


class AsyncShapeResourceWithStreamingResponse:
    def __init__(self, shape: AsyncShapeResource) -> None:
        self._shape = shape

        self.retrieve = async_to_streamed_response_wrapper(
            shape.retrieve,
        )
