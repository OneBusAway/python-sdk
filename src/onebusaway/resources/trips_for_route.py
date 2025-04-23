# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..types import trips_for_route_list_params
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
from ..types.trips_for_route_list_response import TripsForRouteListResponse

__all__ = ["TripsForRouteResource", "AsyncTripsForRouteResource"]


class TripsForRouteResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> TripsForRouteResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/OneBusAway/python-sdk#accessing-raw-response-data-eg-headers
        """
        return TripsForRouteResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> TripsForRouteResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/OneBusAway/python-sdk#with_streaming_response
        """
        return TripsForRouteResourceWithStreamingResponse(self)

    def list(
        self,
        route_id: str,
        *,
        include_schedule: bool | NotGiven = NOT_GIVEN,
        include_status: bool | NotGiven = NOT_GIVEN,
        time: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TripsForRouteListResponse:
        """
        Search for active trips for a specific route.

        Args:
          include_schedule: Determine whether full schedule elements are included. Defaults to false.

          include_status: Determine whether full tripStatus elements with real-time information are
              included. Defaults to false.

          time: Query the system at a specific time. Useful for testing.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not route_id:
            raise ValueError(f"Expected a non-empty value for `route_id` but received {route_id!r}")
        return self._get(
            f"/api/where/trips-for-route/{route_id}.json",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "include_schedule": include_schedule,
                        "include_status": include_status,
                        "time": time,
                    },
                    trips_for_route_list_params.TripsForRouteListParams,
                ),
            ),
            cast_to=TripsForRouteListResponse,
        )


class AsyncTripsForRouteResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncTripsForRouteResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/OneBusAway/python-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncTripsForRouteResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncTripsForRouteResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/OneBusAway/python-sdk#with_streaming_response
        """
        return AsyncTripsForRouteResourceWithStreamingResponse(self)

    async def list(
        self,
        route_id: str,
        *,
        include_schedule: bool | NotGiven = NOT_GIVEN,
        include_status: bool | NotGiven = NOT_GIVEN,
        time: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TripsForRouteListResponse:
        """
        Search for active trips for a specific route.

        Args:
          include_schedule: Determine whether full schedule elements are included. Defaults to false.

          include_status: Determine whether full tripStatus elements with real-time information are
              included. Defaults to false.

          time: Query the system at a specific time. Useful for testing.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not route_id:
            raise ValueError(f"Expected a non-empty value for `route_id` but received {route_id!r}")
        return await self._get(
            f"/api/where/trips-for-route/{route_id}.json",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "include_schedule": include_schedule,
                        "include_status": include_status,
                        "time": time,
                    },
                    trips_for_route_list_params.TripsForRouteListParams,
                ),
            ),
            cast_to=TripsForRouteListResponse,
        )


class TripsForRouteResourceWithRawResponse:
    def __init__(self, trips_for_route: TripsForRouteResource) -> None:
        self._trips_for_route = trips_for_route

        self.list = to_raw_response_wrapper(
            trips_for_route.list,
        )


class AsyncTripsForRouteResourceWithRawResponse:
    def __init__(self, trips_for_route: AsyncTripsForRouteResource) -> None:
        self._trips_for_route = trips_for_route

        self.list = async_to_raw_response_wrapper(
            trips_for_route.list,
        )


class TripsForRouteResourceWithStreamingResponse:
    def __init__(self, trips_for_route: TripsForRouteResource) -> None:
        self._trips_for_route = trips_for_route

        self.list = to_streamed_response_wrapper(
            trips_for_route.list,
        )


class AsyncTripsForRouteResourceWithStreamingResponse:
    def __init__(self, trips_for_route: AsyncTripsForRouteResource) -> None:
        self._trips_for_route = trips_for_route

        self.list = async_to_streamed_response_wrapper(
            trips_for_route.list,
        )
