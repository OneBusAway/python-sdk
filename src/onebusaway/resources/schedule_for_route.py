# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import date

import httpx

from ..types import schedule_for_route_retrieve_params
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
from ..types.schedule_for_route_retrieve_response import ScheduleForRouteRetrieveResponse

__all__ = ["ScheduleForRouteResource", "AsyncScheduleForRouteResource"]


class ScheduleForRouteResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ScheduleForRouteResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/OneBusAway/python-sdk#accessing-raw-response-data-eg-headers
        """
        return ScheduleForRouteResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ScheduleForRouteResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/OneBusAway/python-sdk#with_streaming_response
        """
        return ScheduleForRouteResourceWithStreamingResponse(self)

    def retrieve(
        self,
        route_id: str,
        *,
        date: Union[str, date] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ScheduleForRouteRetrieveResponse:
        """
        Retrieve the full schedule for a route on a particular day

        Args:
          date: The date for which you want to request a schedule in the format YYYY-MM-DD
              (optional, defaults to current date)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not route_id:
            raise ValueError(f"Expected a non-empty value for `route_id` but received {route_id!r}")
        return self._get(
            f"/api/where/schedule-for-route/{route_id}.json",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"date": date}, schedule_for_route_retrieve_params.ScheduleForRouteRetrieveParams
                ),
            ),
            cast_to=ScheduleForRouteRetrieveResponse,
        )


class AsyncScheduleForRouteResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncScheduleForRouteResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/OneBusAway/python-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncScheduleForRouteResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncScheduleForRouteResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/OneBusAway/python-sdk#with_streaming_response
        """
        return AsyncScheduleForRouteResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        route_id: str,
        *,
        date: Union[str, date] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ScheduleForRouteRetrieveResponse:
        """
        Retrieve the full schedule for a route on a particular day

        Args:
          date: The date for which you want to request a schedule in the format YYYY-MM-DD
              (optional, defaults to current date)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not route_id:
            raise ValueError(f"Expected a non-empty value for `route_id` but received {route_id!r}")
        return await self._get(
            f"/api/where/schedule-for-route/{route_id}.json",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"date": date}, schedule_for_route_retrieve_params.ScheduleForRouteRetrieveParams
                ),
            ),
            cast_to=ScheduleForRouteRetrieveResponse,
        )


class ScheduleForRouteResourceWithRawResponse:
    def __init__(self, schedule_for_route: ScheduleForRouteResource) -> None:
        self._schedule_for_route = schedule_for_route

        self.retrieve = to_raw_response_wrapper(
            schedule_for_route.retrieve,
        )


class AsyncScheduleForRouteResourceWithRawResponse:
    def __init__(self, schedule_for_route: AsyncScheduleForRouteResource) -> None:
        self._schedule_for_route = schedule_for_route

        self.retrieve = async_to_raw_response_wrapper(
            schedule_for_route.retrieve,
        )


class ScheduleForRouteResourceWithStreamingResponse:
    def __init__(self, schedule_for_route: ScheduleForRouteResource) -> None:
        self._schedule_for_route = schedule_for_route

        self.retrieve = to_streamed_response_wrapper(
            schedule_for_route.retrieve,
        )


class AsyncScheduleForRouteResourceWithStreamingResponse:
    def __init__(self, schedule_for_route: AsyncScheduleForRouteResource) -> None:
        self._schedule_for_route = schedule_for_route

        self.retrieve = async_to_streamed_response_wrapper(
            schedule_for_route.retrieve,
        )
