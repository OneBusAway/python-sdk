# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ...._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._base_client import (
    make_request_options,
)
from ....types.api.where.arrivals_and_departures_for_stop_list_response import ArrivalsAndDeparturesForStopListResponse

__all__ = ["ArrivalsAndDeparturesForStopResource", "AsyncArrivalsAndDeparturesForStopResource"]


class ArrivalsAndDeparturesForStopResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ArrivalsAndDeparturesForStopResourceWithRawResponse:
        return ArrivalsAndDeparturesForStopResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ArrivalsAndDeparturesForStopResourceWithStreamingResponse:
        return ArrivalsAndDeparturesForStopResourceWithStreamingResponse(self)

    def list(
        self,
        stop_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ArrivalsAndDeparturesForStopListResponse:
        """
        arrival-and-departure-for-stop

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not stop_id:
            raise ValueError(f"Expected a non-empty value for `stop_id` but received {stop_id!r}")
        return self._get(
            f"/api/where/arrivals-and-departures-for-stop/stopID.json",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ArrivalsAndDeparturesForStopListResponse,
        )


class AsyncArrivalsAndDeparturesForStopResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncArrivalsAndDeparturesForStopResourceWithRawResponse:
        return AsyncArrivalsAndDeparturesForStopResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncArrivalsAndDeparturesForStopResourceWithStreamingResponse:
        return AsyncArrivalsAndDeparturesForStopResourceWithStreamingResponse(self)

    async def list(
        self,
        stop_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ArrivalsAndDeparturesForStopListResponse:
        """
        arrival-and-departure-for-stop

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not stop_id:
            raise ValueError(f"Expected a non-empty value for `stop_id` but received {stop_id!r}")
        return await self._get(
            f"/api/where/arrivals-and-departures-for-stop/stopID.json",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ArrivalsAndDeparturesForStopListResponse,
        )


class ArrivalsAndDeparturesForStopResourceWithRawResponse:
    def __init__(self, arrivals_and_departures_for_stop: ArrivalsAndDeparturesForStopResource) -> None:
        self._arrivals_and_departures_for_stop = arrivals_and_departures_for_stop

        self.list = to_raw_response_wrapper(
            arrivals_and_departures_for_stop.list,
        )


class AsyncArrivalsAndDeparturesForStopResourceWithRawResponse:
    def __init__(self, arrivals_and_departures_for_stop: AsyncArrivalsAndDeparturesForStopResource) -> None:
        self._arrivals_and_departures_for_stop = arrivals_and_departures_for_stop

        self.list = async_to_raw_response_wrapper(
            arrivals_and_departures_for_stop.list,
        )


class ArrivalsAndDeparturesForStopResourceWithStreamingResponse:
    def __init__(self, arrivals_and_departures_for_stop: ArrivalsAndDeparturesForStopResource) -> None:
        self._arrivals_and_departures_for_stop = arrivals_and_departures_for_stop

        self.list = to_streamed_response_wrapper(
            arrivals_and_departures_for_stop.list,
        )


class AsyncArrivalsAndDeparturesForStopResourceWithStreamingResponse:
    def __init__(self, arrivals_and_departures_for_stop: AsyncArrivalsAndDeparturesForStopResource) -> None:
        self._arrivals_and_departures_for_stop = arrivals_and_departures_for_stop

        self.list = async_to_streamed_response_wrapper(
            arrivals_and_departures_for_stop.list,
        )
