# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..types import current_time_retrieve_params
from .._types import NOT_GIVEN, Body, Query, Headers, NoneType, NotGiven
from .._utils import (
    maybe_transform,
    async_maybe_transform,
)
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import (
    make_request_options,
)

__all__ = ["CurrentTime", "AsyncCurrentTime"]


class CurrentTime(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> CurrentTimeWithRawResponse:
        return CurrentTimeWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CurrentTimeWithStreamingResponse:
        return CurrentTimeWithStreamingResponse(self)

    def retrieve(
        self,
        *,
        key: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        current-time

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._get(
            "/api/where/current-time.json",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"key": key}, current_time_retrieve_params.CurrentTimeRetrieveParams),
            ),
            cast_to=NoneType,
        )


class AsyncCurrentTime(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncCurrentTimeWithRawResponse:
        return AsyncCurrentTimeWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCurrentTimeWithStreamingResponse:
        return AsyncCurrentTimeWithStreamingResponse(self)

    async def retrieve(
        self,
        *,
        key: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        current-time

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._get(
            "/api/where/current-time.json",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"key": key}, current_time_retrieve_params.CurrentTimeRetrieveParams),
            ),
            cast_to=NoneType,
        )


class CurrentTimeWithRawResponse:
    def __init__(self, current_time: CurrentTime) -> None:
        self._current_time = current_time

        self.retrieve = to_raw_response_wrapper(
            current_time.retrieve,
        )


class AsyncCurrentTimeWithRawResponse:
    def __init__(self, current_time: AsyncCurrentTime) -> None:
        self._current_time = current_time

        self.retrieve = async_to_raw_response_wrapper(
            current_time.retrieve,
        )


class CurrentTimeWithStreamingResponse:
    def __init__(self, current_time: CurrentTime) -> None:
        self._current_time = current_time

        self.retrieve = to_streamed_response_wrapper(
            current_time.retrieve,
        )


class AsyncCurrentTimeWithStreamingResponse:
    def __init__(self, current_time: AsyncCurrentTime) -> None:
        self._current_time = current_time

        self.retrieve = async_to_streamed_response_wrapper(
            current_time.retrieve,
        )
