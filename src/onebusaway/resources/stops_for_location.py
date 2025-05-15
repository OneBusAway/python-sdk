# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..types import stops_for_location_list_params
from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from .._utils import maybe_transform, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.stops_for_location_list_response import StopsForLocationListResponse

__all__ = ["StopsForLocationResource", "AsyncStopsForLocationResource"]


class StopsForLocationResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> StopsForLocationResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/OneBusAway/python-sdk#accessing-raw-response-data-eg-headers
        """
        return StopsForLocationResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> StopsForLocationResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/OneBusAway/python-sdk#with_streaming_response
        """
        return StopsForLocationResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        lat: float,
        lon: float,
        lat_span: float | NotGiven = NOT_GIVEN,
        lon_span: float | NotGiven = NOT_GIVEN,
        query: str | NotGiven = NOT_GIVEN,
        radius: float | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> StopsForLocationListResponse:
        """
        stops-for-location

        Args:
          lat_span: An alternative to radius to set the search bounding box (optional)

          lon_span: An alternative to radius to set the search bounding box (optional)

          query: A search query string to filter the results

          radius: The radius in meters to search within

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
                        "lat": lat,
                        "lon": lon,
                        "lat_span": lat_span,
                        "lon_span": lon_span,
                        "query": query,
                        "radius": radius,
                    },
                    stops_for_location_list_params.StopsForLocationListParams,
                ),
            ),
            cast_to=StopsForLocationListResponse,
        )


class AsyncStopsForLocationResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncStopsForLocationResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/OneBusAway/python-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncStopsForLocationResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncStopsForLocationResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/OneBusAway/python-sdk#with_streaming_response
        """
        return AsyncStopsForLocationResourceWithStreamingResponse(self)

    async def list(
        self,
        *,
        lat: float,
        lon: float,
        lat_span: float | NotGiven = NOT_GIVEN,
        lon_span: float | NotGiven = NOT_GIVEN,
        query: str | NotGiven = NOT_GIVEN,
        radius: float | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> StopsForLocationListResponse:
        """
        stops-for-location

        Args:
          lat_span: An alternative to radius to set the search bounding box (optional)

          lon_span: An alternative to radius to set the search bounding box (optional)

          query: A search query string to filter the results

          radius: The radius in meters to search within

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
                        "lat": lat,
                        "lon": lon,
                        "lat_span": lat_span,
                        "lon_span": lon_span,
                        "query": query,
                        "radius": radius,
                    },
                    stops_for_location_list_params.StopsForLocationListParams,
                ),
            ),
            cast_to=StopsForLocationListResponse,
        )


class StopsForLocationResourceWithRawResponse:
    def __init__(self, stops_for_location: StopsForLocationResource) -> None:
        self._stops_for_location = stops_for_location

        self.list = to_raw_response_wrapper(
            stops_for_location.list,
        )


class AsyncStopsForLocationResourceWithRawResponse:
    def __init__(self, stops_for_location: AsyncStopsForLocationResource) -> None:
        self._stops_for_location = stops_for_location

        self.list = async_to_raw_response_wrapper(
            stops_for_location.list,
        )


class StopsForLocationResourceWithStreamingResponse:
    def __init__(self, stops_for_location: StopsForLocationResource) -> None:
        self._stops_for_location = stops_for_location

        self.list = to_streamed_response_wrapper(
            stops_for_location.list,
        )


class AsyncStopsForLocationResourceWithStreamingResponse:
    def __init__(self, stops_for_location: AsyncStopsForLocationResource) -> None:
        self._stops_for_location = stops_for_location

        self.list = async_to_streamed_response_wrapper(
            stops_for_location.list,
        )
