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
from ..types.stop_retrieve_response import StopRetrieveResponse

__all__ = ["StopResource", "AsyncStopResource"]


class StopResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> StopResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/OneBusAway/python-sdk#accessing-raw-response-data-eg-headers
        """
        return StopResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> StopResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/OneBusAway/python-sdk#with_streaming_response
        """
        return StopResourceWithStreamingResponse(self)

    def retrieve(
        self,
        stop_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> StopRetrieveResponse:
        """
        Get details of a specific stop

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not stop_id:
            raise ValueError(f"Expected a non-empty value for `stop_id` but received {stop_id!r}")
        return self._get(
            f"/api/where/stop/{stop_id}.json",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=StopRetrieveResponse,
        )


class AsyncStopResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncStopResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/OneBusAway/python-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncStopResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncStopResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/OneBusAway/python-sdk#with_streaming_response
        """
        return AsyncStopResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        stop_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> StopRetrieveResponse:
        """
        Get details of a specific stop

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not stop_id:
            raise ValueError(f"Expected a non-empty value for `stop_id` but received {stop_id!r}")
        return await self._get(
            f"/api/where/stop/{stop_id}.json",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=StopRetrieveResponse,
        )


class StopResourceWithRawResponse:
    def __init__(self, stop: StopResource) -> None:
        self._stop = stop

        self.retrieve = to_raw_response_wrapper(
            stop.retrieve,
        )


class AsyncStopResourceWithRawResponse:
    def __init__(self, stop: AsyncStopResource) -> None:
        self._stop = stop

        self.retrieve = async_to_raw_response_wrapper(
            stop.retrieve,
        )


class StopResourceWithStreamingResponse:
    def __init__(self, stop: StopResource) -> None:
        self._stop = stop

        self.retrieve = to_streamed_response_wrapper(
            stop.retrieve,
        )


class AsyncStopResourceWithStreamingResponse:
    def __init__(self, stop: AsyncStopResource) -> None:
        self._stop = stop

        self.retrieve = async_to_streamed_response_wrapper(
            stop.retrieve,
        )
