# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..types import trips_for_location_list_params
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
from ..types.trips_for_location_list_response import TripsForLocationListResponse

__all__ = ["TripsForLocationResource", "AsyncTripsForLocationResource"]


class TripsForLocationResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> TripsForLocationResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/OneBusAway/python-sdk#accessing-raw-response-data-eg-headers
        """
        return TripsForLocationResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> TripsForLocationResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/OneBusAway/python-sdk#with_streaming_response
        """
        return TripsForLocationResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        lat: float,
        lat_span: float,
        lon: float,
        lon_span: float,
        include_schedule: bool | NotGiven = NOT_GIVEN,
        include_trip: bool | NotGiven = NOT_GIVEN,
        time: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TripsForLocationListResponse:
        """
        Retrieve trips for a given location

        Args:
          lat: The latitude coordinate of the search center

          lat_span: Latitude span of the search bounding box

          lon: The longitude coordinate of the search center

          lon_span: Longitude span of the search bounding box

          include_schedule: Whether to include full schedule elements in the tripDetails section. Defaults
              to false.

          include_trip: Whether to include full trip elements in the references section. Defaults to
              false.

          time: Specific time for the query. Defaults to the current time.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/api/where/trips-for-location.json",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "lat": lat,
                        "lat_span": lat_span,
                        "lon": lon,
                        "lon_span": lon_span,
                        "include_schedule": include_schedule,
                        "include_trip": include_trip,
                        "time": time,
                    },
                    trips_for_location_list_params.TripsForLocationListParams,
                ),
            ),
            cast_to=TripsForLocationListResponse,
        )


class AsyncTripsForLocationResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncTripsForLocationResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/OneBusAway/python-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncTripsForLocationResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncTripsForLocationResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/OneBusAway/python-sdk#with_streaming_response
        """
        return AsyncTripsForLocationResourceWithStreamingResponse(self)

    async def list(
        self,
        *,
        lat: float,
        lat_span: float,
        lon: float,
        lon_span: float,
        include_schedule: bool | NotGiven = NOT_GIVEN,
        include_trip: bool | NotGiven = NOT_GIVEN,
        time: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TripsForLocationListResponse:
        """
        Retrieve trips for a given location

        Args:
          lat: The latitude coordinate of the search center

          lat_span: Latitude span of the search bounding box

          lon: The longitude coordinate of the search center

          lon_span: Longitude span of the search bounding box

          include_schedule: Whether to include full schedule elements in the tripDetails section. Defaults
              to false.

          include_trip: Whether to include full trip elements in the references section. Defaults to
              false.

          time: Specific time for the query. Defaults to the current time.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/api/where/trips-for-location.json",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "lat": lat,
                        "lat_span": lat_span,
                        "lon": lon,
                        "lon_span": lon_span,
                        "include_schedule": include_schedule,
                        "include_trip": include_trip,
                        "time": time,
                    },
                    trips_for_location_list_params.TripsForLocationListParams,
                ),
            ),
            cast_to=TripsForLocationListResponse,
        )


class TripsForLocationResourceWithRawResponse:
    def __init__(self, trips_for_location: TripsForLocationResource) -> None:
        self._trips_for_location = trips_for_location

        self.list = to_raw_response_wrapper(
            trips_for_location.list,
        )


class AsyncTripsForLocationResourceWithRawResponse:
    def __init__(self, trips_for_location: AsyncTripsForLocationResource) -> None:
        self._trips_for_location = trips_for_location

        self.list = async_to_raw_response_wrapper(
            trips_for_location.list,
        )


class TripsForLocationResourceWithStreamingResponse:
    def __init__(self, trips_for_location: TripsForLocationResource) -> None:
        self._trips_for_location = trips_for_location

        self.list = to_streamed_response_wrapper(
            trips_for_location.list,
        )


class AsyncTripsForLocationResourceWithStreamingResponse:
    def __init__(self, trips_for_location: AsyncTripsForLocationResource) -> None:
        self._trips_for_location = trips_for_location

        self.list = async_to_streamed_response_wrapper(
            trips_for_location.list,
        )
