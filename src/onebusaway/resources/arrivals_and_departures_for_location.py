# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..types import arrivals_and_departures_for_location_list_params
from .._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
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
from ..types.arrivals_and_departures_for_location_list_response import ArrivalsAndDeparturesForLocationListResponse

__all__ = ["ArrivalsAndDeparturesForLocationResource", "AsyncArrivalsAndDeparturesForLocationResource"]


class ArrivalsAndDeparturesForLocationResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ArrivalsAndDeparturesForLocationResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/OneBusAway/python-sdk#accessing-raw-response-data-eg-headers
        """
        return ArrivalsAndDeparturesForLocationResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ArrivalsAndDeparturesForLocationResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/OneBusAway/python-sdk#with_streaming_response
        """
        return ArrivalsAndDeparturesForLocationResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        lat: float,
        lon: float,
        empty_returns_not_found: bool | Omit = omit,
        lat_span: float | Omit = omit,
        lon_span: float | Omit = omit,
        max_count: int | Omit = omit,
        minutes_after: int | Omit = omit,
        minutes_before: int | Omit = omit,
        radius: float | Omit = omit,
        route_type: str | Omit = omit,
        time: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ArrivalsAndDeparturesForLocationListResponse:
        """
        Returns real-time arrival and departure data for stops within a bounding box or
        radius centered on a specific location.

        Args:
          lat: The latitude coordinate of the search center.

          lon: The longitude coordinate of the search center.

          empty_returns_not_found: If true, returns a 404 Not Found error instead of an empty result.

          lat_span: Sets the latitude limits of the search bounding box.

          lon_span: Sets the longitude limits of the search bounding box.

          max_count: The max size of the list of nearby stops and arrivals to return. Defaults to
              250, max 1000.

          minutes_after: Include arrivals and departures this many minutes after the query time.

          minutes_before: Include arrivals and departures this many minutes before the query time.

          radius: The search radius in meters.

          route_type: Optional list of GTFS routeTypes to filter by (comma delimited) e.g. "1,2,3".

          time: By default, returns the status right now. Can be queried at a specific time
              (milliseconds since epoch) for testing.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/api/where/arrivals-and-departures-for-location.json",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "lat": lat,
                        "lon": lon,
                        "empty_returns_not_found": empty_returns_not_found,
                        "lat_span": lat_span,
                        "lon_span": lon_span,
                        "max_count": max_count,
                        "minutes_after": minutes_after,
                        "minutes_before": minutes_before,
                        "radius": radius,
                        "route_type": route_type,
                        "time": time,
                    },
                    arrivals_and_departures_for_location_list_params.ArrivalsAndDeparturesForLocationListParams,
                ),
            ),
            cast_to=ArrivalsAndDeparturesForLocationListResponse,
        )


class AsyncArrivalsAndDeparturesForLocationResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncArrivalsAndDeparturesForLocationResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/OneBusAway/python-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncArrivalsAndDeparturesForLocationResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncArrivalsAndDeparturesForLocationResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/OneBusAway/python-sdk#with_streaming_response
        """
        return AsyncArrivalsAndDeparturesForLocationResourceWithStreamingResponse(self)

    async def list(
        self,
        *,
        lat: float,
        lon: float,
        empty_returns_not_found: bool | Omit = omit,
        lat_span: float | Omit = omit,
        lon_span: float | Omit = omit,
        max_count: int | Omit = omit,
        minutes_after: int | Omit = omit,
        minutes_before: int | Omit = omit,
        radius: float | Omit = omit,
        route_type: str | Omit = omit,
        time: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ArrivalsAndDeparturesForLocationListResponse:
        """
        Returns real-time arrival and departure data for stops within a bounding box or
        radius centered on a specific location.

        Args:
          lat: The latitude coordinate of the search center.

          lon: The longitude coordinate of the search center.

          empty_returns_not_found: If true, returns a 404 Not Found error instead of an empty result.

          lat_span: Sets the latitude limits of the search bounding box.

          lon_span: Sets the longitude limits of the search bounding box.

          max_count: The max size of the list of nearby stops and arrivals to return. Defaults to
              250, max 1000.

          minutes_after: Include arrivals and departures this many minutes after the query time.

          minutes_before: Include arrivals and departures this many minutes before the query time.

          radius: The search radius in meters.

          route_type: Optional list of GTFS routeTypes to filter by (comma delimited) e.g. "1,2,3".

          time: By default, returns the status right now. Can be queried at a specific time
              (milliseconds since epoch) for testing.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/api/where/arrivals-and-departures-for-location.json",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "lat": lat,
                        "lon": lon,
                        "empty_returns_not_found": empty_returns_not_found,
                        "lat_span": lat_span,
                        "lon_span": lon_span,
                        "max_count": max_count,
                        "minutes_after": minutes_after,
                        "minutes_before": minutes_before,
                        "radius": radius,
                        "route_type": route_type,
                        "time": time,
                    },
                    arrivals_and_departures_for_location_list_params.ArrivalsAndDeparturesForLocationListParams,
                ),
            ),
            cast_to=ArrivalsAndDeparturesForLocationListResponse,
        )


class ArrivalsAndDeparturesForLocationResourceWithRawResponse:
    def __init__(self, arrivals_and_departures_for_location: ArrivalsAndDeparturesForLocationResource) -> None:
        self._arrivals_and_departures_for_location = arrivals_and_departures_for_location

        self.list = to_raw_response_wrapper(
            arrivals_and_departures_for_location.list,
        )


class AsyncArrivalsAndDeparturesForLocationResourceWithRawResponse:
    def __init__(self, arrivals_and_departures_for_location: AsyncArrivalsAndDeparturesForLocationResource) -> None:
        self._arrivals_and_departures_for_location = arrivals_and_departures_for_location

        self.list = async_to_raw_response_wrapper(
            arrivals_and_departures_for_location.list,
        )


class ArrivalsAndDeparturesForLocationResourceWithStreamingResponse:
    def __init__(self, arrivals_and_departures_for_location: ArrivalsAndDeparturesForLocationResource) -> None:
        self._arrivals_and_departures_for_location = arrivals_and_departures_for_location

        self.list = to_streamed_response_wrapper(
            arrivals_and_departures_for_location.list,
        )


class AsyncArrivalsAndDeparturesForLocationResourceWithStreamingResponse:
    def __init__(self, arrivals_and_departures_for_location: AsyncArrivalsAndDeparturesForLocationResource) -> None:
        self._arrivals_and_departures_for_location = arrivals_and_departures_for_location

        self.list = async_to_streamed_response_wrapper(
            arrivals_and_departures_for_location.list,
        )
