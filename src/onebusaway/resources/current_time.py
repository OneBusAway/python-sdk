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
from ..types.current_time_retrieve_response import CurrentTimeRetrieveResponse

__all__ = ["CurrentTimeResource", "AsyncCurrentTimeResource"]


class CurrentTimeResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> CurrentTimeResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/OneBusAway/python-sdk#accessing-raw-response-data-eg-headers
        """
        return CurrentTimeResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CurrentTimeResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/OneBusAway/python-sdk#with_streaming_response
        """
        return CurrentTimeResourceWithStreamingResponse(self)

    def retrieve(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CurrentTimeRetrieveResponse:
        """current-time"""
        return self._get(
            "/api/where/current-time.json",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CurrentTimeRetrieveResponse,
        )


class AsyncCurrentTimeResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncCurrentTimeResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/OneBusAway/python-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncCurrentTimeResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCurrentTimeResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/OneBusAway/python-sdk#with_streaming_response
        """
        return AsyncCurrentTimeResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CurrentTimeRetrieveResponse:
        """current-time"""
        return await self._get(
            "/api/where/current-time.json",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CurrentTimeRetrieveResponse,
        )


class CurrentTimeResourceWithRawResponse:
    def __init__(self, current_time: CurrentTimeResource) -> None:
        self._current_time = current_time

        self.retrieve = to_raw_response_wrapper(
            current_time.retrieve,
        )


class AsyncCurrentTimeResourceWithRawResponse:
    def __init__(self, current_time: AsyncCurrentTimeResource) -> None:
        self._current_time = current_time

        self.retrieve = async_to_raw_response_wrapper(
            current_time.retrieve,
        )


class CurrentTimeResourceWithStreamingResponse:
    def __init__(self, current_time: CurrentTimeResource) -> None:
        self._current_time = current_time

        self.retrieve = to_streamed_response_wrapper(
            current_time.retrieve,
        )


class AsyncCurrentTimeResourceWithStreamingResponse:
    def __init__(self, current_time: AsyncCurrentTimeResource) -> None:
        self._current_time = current_time

        self.retrieve = async_to_streamed_response_wrapper(
            current_time.retrieve,
        )
