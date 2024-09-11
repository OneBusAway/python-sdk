# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import date

import httpx

from ..types import schedule_for_stop_retrieve_params
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
from ..types.schedule_for_stop_retrieve_response import ScheduleForStopRetrieveResponse

__all__ = ["ScheduleForStopResource", "AsyncScheduleForStopResource"]


class ScheduleForStopResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ScheduleForStopResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/OneBusAway/python-sdk#accessing-raw-response-data-eg-headers
        """
        return ScheduleForStopResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ScheduleForStopResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/OneBusAway/python-sdk#with_streaming_response
        """
        return ScheduleForStopResourceWithStreamingResponse(self)

    def retrieve(
        self,
        stop_id: str,
        *,
        date: Union[str, date] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ScheduleForStopRetrieveResponse:
        """
        Get schedule for a specific stop

        Args:
          date: The date for which you want to request a schedule in the format YYYY-MM-DD
              (optional, defaults to the current date)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not stop_id:
            raise ValueError(f"Expected a non-empty value for `stop_id` but received {stop_id!r}")
        return self._get(
            f"/api/where/schedule-for-stop/{stop_id}.json",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"date": date}, schedule_for_stop_retrieve_params.ScheduleForStopRetrieveParams),
            ),
            cast_to=ScheduleForStopRetrieveResponse,
        )


class AsyncScheduleForStopResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncScheduleForStopResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/OneBusAway/python-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncScheduleForStopResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncScheduleForStopResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/OneBusAway/python-sdk#with_streaming_response
        """
        return AsyncScheduleForStopResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        stop_id: str,
        *,
        date: Union[str, date] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ScheduleForStopRetrieveResponse:
        """
        Get schedule for a specific stop

        Args:
          date: The date for which you want to request a schedule in the format YYYY-MM-DD
              (optional, defaults to the current date)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not stop_id:
            raise ValueError(f"Expected a non-empty value for `stop_id` but received {stop_id!r}")
        return await self._get(
            f"/api/where/schedule-for-stop/{stop_id}.json",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"date": date}, schedule_for_stop_retrieve_params.ScheduleForStopRetrieveParams
                ),
            ),
            cast_to=ScheduleForStopRetrieveResponse,
        )


class ScheduleForStopResourceWithRawResponse:
    def __init__(self, schedule_for_stop: ScheduleForStopResource) -> None:
        self._schedule_for_stop = schedule_for_stop

        self.retrieve = to_raw_response_wrapper(
            schedule_for_stop.retrieve,
        )


class AsyncScheduleForStopResourceWithRawResponse:
    def __init__(self, schedule_for_stop: AsyncScheduleForStopResource) -> None:
        self._schedule_for_stop = schedule_for_stop

        self.retrieve = async_to_raw_response_wrapper(
            schedule_for_stop.retrieve,
        )


class ScheduleForStopResourceWithStreamingResponse:
    def __init__(self, schedule_for_stop: ScheduleForStopResource) -> None:
        self._schedule_for_stop = schedule_for_stop

        self.retrieve = to_streamed_response_wrapper(
            schedule_for_stop.retrieve,
        )


class AsyncScheduleForStopResourceWithStreamingResponse:
    def __init__(self, schedule_for_stop: AsyncScheduleForStopResource) -> None:
        self._schedule_for_stop = schedule_for_stop

        self.retrieve = async_to_streamed_response_wrapper(
            schedule_for_stop.retrieve,
        )
