# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..types import stops_for_route_list_params
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
from ..types.stops_for_route_list_response import StopsForRouteListResponse

__all__ = ["StopsForRouteResource", "AsyncStopsForRouteResource"]


class StopsForRouteResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> StopsForRouteResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/OneBusAway/python-sdk#accessing-raw-response-data-eg-headers
        """
        return StopsForRouteResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> StopsForRouteResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/OneBusAway/python-sdk#with_streaming_response
        """
        return StopsForRouteResourceWithStreamingResponse(self)

    def list(
        self,
        route_id: str,
        *,
        include_polylines: bool | NotGiven = NOT_GIVEN,
        time: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> StopsForRouteListResponse:
        """
        Get stops for a specific route

        Args:
          include_polylines: Include polyline elements in the response (default true)

          time: Specify service date (YYYY-MM-DD or epoch) (default today)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not route_id:
            raise ValueError(f"Expected a non-empty value for `route_id` but received {route_id!r}")
        return self._get(
            f"/api/where/stops-for-route/{route_id}.json",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "include_polylines": include_polylines,
                        "time": time,
                    },
                    stops_for_route_list_params.StopsForRouteListParams,
                ),
            ),
            cast_to=StopsForRouteListResponse,
        )


class AsyncStopsForRouteResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncStopsForRouteResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/OneBusAway/python-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncStopsForRouteResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncStopsForRouteResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/OneBusAway/python-sdk#with_streaming_response
        """
        return AsyncStopsForRouteResourceWithStreamingResponse(self)

    async def list(
        self,
        route_id: str,
        *,
        include_polylines: bool | NotGiven = NOT_GIVEN,
        time: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> StopsForRouteListResponse:
        """
        Get stops for a specific route

        Args:
          include_polylines: Include polyline elements in the response (default true)

          time: Specify service date (YYYY-MM-DD or epoch) (default today)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not route_id:
            raise ValueError(f"Expected a non-empty value for `route_id` but received {route_id!r}")
        return await self._get(
            f"/api/where/stops-for-route/{route_id}.json",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "include_polylines": include_polylines,
                        "time": time,
                    },
                    stops_for_route_list_params.StopsForRouteListParams,
                ),
            ),
            cast_to=StopsForRouteListResponse,
        )


class StopsForRouteResourceWithRawResponse:
    def __init__(self, stops_for_route: StopsForRouteResource) -> None:
        self._stops_for_route = stops_for_route

        self.list = to_raw_response_wrapper(
            stops_for_route.list,
        )


class AsyncStopsForRouteResourceWithRawResponse:
    def __init__(self, stops_for_route: AsyncStopsForRouteResource) -> None:
        self._stops_for_route = stops_for_route

        self.list = async_to_raw_response_wrapper(
            stops_for_route.list,
        )


class StopsForRouteResourceWithStreamingResponse:
    def __init__(self, stops_for_route: StopsForRouteResource) -> None:
        self._stops_for_route = stops_for_route

        self.list = to_streamed_response_wrapper(
            stops_for_route.list,
        )


class AsyncStopsForRouteResourceWithStreamingResponse:
    def __init__(self, stops_for_route: AsyncStopsForRouteResource) -> None:
        self._stops_for_route = stops_for_route

        self.list = async_to_streamed_response_wrapper(
            stops_for_route.list,
        )
