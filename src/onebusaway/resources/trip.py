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
from ..types.trip_retrieve_response import TripRetrieveResponse

__all__ = ["TripResource", "AsyncTripResource"]


class TripResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> TripResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/OneBusAway/python-sdk#accessing-raw-response-data-eg-headers
        """
        return TripResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> TripResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/OneBusAway/python-sdk#with_streaming_response
        """
        return TripResourceWithStreamingResponse(self)

    def retrieve(
        self,
        trip_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TripRetrieveResponse:
        """
        Get details of a specific trip

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not trip_id:
            raise ValueError(f"Expected a non-empty value for `trip_id` but received {trip_id!r}")
        return self._get(
            f"/api/where/trip/{trip_id}.json",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TripRetrieveResponse,
        )


class AsyncTripResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncTripResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/OneBusAway/python-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncTripResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncTripResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/OneBusAway/python-sdk#with_streaming_response
        """
        return AsyncTripResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        trip_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TripRetrieveResponse:
        """
        Get details of a specific trip

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not trip_id:
            raise ValueError(f"Expected a non-empty value for `trip_id` but received {trip_id!r}")
        return await self._get(
            f"/api/where/trip/{trip_id}.json",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=TripRetrieveResponse,
        )


class TripResourceWithRawResponse:
    def __init__(self, trip: TripResource) -> None:
        self._trip = trip

        self.retrieve = to_raw_response_wrapper(
            trip.retrieve,
        )


class AsyncTripResourceWithRawResponse:
    def __init__(self, trip: AsyncTripResource) -> None:
        self._trip = trip

        self.retrieve = async_to_raw_response_wrapper(
            trip.retrieve,
        )


class TripResourceWithStreamingResponse:
    def __init__(self, trip: TripResource) -> None:
        self._trip = trip

        self.retrieve = to_streamed_response_wrapper(
            trip.retrieve,
        )


class AsyncTripResourceWithStreamingResponse:
    def __init__(self, trip: AsyncTripResource) -> None:
        self._trip = trip

        self.retrieve = async_to_streamed_response_wrapper(
            trip.retrieve,
        )
