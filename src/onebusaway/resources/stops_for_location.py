# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..types import stops_for_location_retrieve_params
from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven
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
from .._base_client import make_request_options
from ..types.stops_for_location_retrieve_response import StopsForLocationRetrieveResponse

__all__ = ["StopsForLocationResource", "AsyncStopsForLocationResource"]


class StopsForLocationResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> StopsForLocationResourceWithRawResponse:
        return StopsForLocationResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> StopsForLocationResourceWithStreamingResponse:
        return StopsForLocationResourceWithStreamingResponse(self)

    def retrieve(
        self,
        *,
        key: str,
        lat: float | NotGiven = NOT_GIVEN,
        lon: float | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> StopsForLocationRetrieveResponse:
        """
        stops-for-location

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/api/where/stops-for-location.json",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "key": key,
                        "lat": lat,
                        "lon": lon,
                    },
                    stops_for_location_retrieve_params.StopsForLocationRetrieveParams,
                ),
            ),
            cast_to=StopsForLocationRetrieveResponse,
        )


class AsyncStopsForLocationResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncStopsForLocationResourceWithRawResponse:
        return AsyncStopsForLocationResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncStopsForLocationResourceWithStreamingResponse:
        return AsyncStopsForLocationResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        *,
        key: str,
        lat: float | NotGiven = NOT_GIVEN,
        lon: float | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> StopsForLocationRetrieveResponse:
        """
        stops-for-location

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/api/where/stops-for-location.json",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "key": key,
                        "lat": lat,
                        "lon": lon,
                    },
                    stops_for_location_retrieve_params.StopsForLocationRetrieveParams,
                ),
            ),
            cast_to=StopsForLocationRetrieveResponse,
        )


class StopsForLocationResourceWithRawResponse:
    def __init__(self, stops_for_location: StopsForLocationResource) -> None:
        self._stops_for_location = stops_for_location

        self.retrieve = to_raw_response_wrapper(
            stops_for_location.retrieve,
        )


class AsyncStopsForLocationResourceWithRawResponse:
    def __init__(self, stops_for_location: AsyncStopsForLocationResource) -> None:
        self._stops_for_location = stops_for_location

        self.retrieve = async_to_raw_response_wrapper(
            stops_for_location.retrieve,
        )


class StopsForLocationResourceWithStreamingResponse:
    def __init__(self, stops_for_location: StopsForLocationResource) -> None:
        self._stops_for_location = stops_for_location

        self.retrieve = to_streamed_response_wrapper(
            stops_for_location.retrieve,
        )


class AsyncStopsForLocationResourceWithStreamingResponse:
    def __init__(self, stops_for_location: AsyncStopsForLocationResource) -> None:
        self._stops_for_location = stops_for_location

        self.retrieve = async_to_streamed_response_wrapper(
            stops_for_location.retrieve,
        )
