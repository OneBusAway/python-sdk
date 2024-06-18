# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..types import arrivals_and_departures_for_stop_retrieve_params
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
from .._base_client import (
    make_request_options,
)
from ..types.arrivals_and_departures_for_stop_retrieve_response import ArrivalsAndDeparturesForStopRetrieveResponse

__all__ = ["ArrivalsAndDeparturesForStopResource", "AsyncArrivalsAndDeparturesForStopResource"]


class ArrivalsAndDeparturesForStopResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ArrivalsAndDeparturesForStopResourceWithRawResponse:
        return ArrivalsAndDeparturesForStopResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ArrivalsAndDeparturesForStopResourceWithStreamingResponse:
        return ArrivalsAndDeparturesForStopResourceWithStreamingResponse(self)

    def retrieve(
        self,
        stop_id: str,
        *,
        service_date: int,
        trip_id: str,
        stop_sequence: int | NotGiven = NOT_GIVEN,
        time: int | NotGiven = NOT_GIVEN,
        vehicle_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ArrivalsAndDeparturesForStopRetrieveResponse:
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
            f"/api/where/arrival-and-departure-for-stop/stopID.json",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "service_date": service_date,
                        "trip_id": trip_id,
                        "stop_sequence": stop_sequence,
                        "time": time,
                        "vehicle_id": vehicle_id,
                    },
                    arrivals_and_departures_for_stop_retrieve_params.ArrivalsAndDeparturesForStopRetrieveParams,
                ),
            ),
            cast_to=ArrivalsAndDeparturesForStopRetrieveResponse,
        )


class AsyncArrivalsAndDeparturesForStopResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncArrivalsAndDeparturesForStopResourceWithRawResponse:
        return AsyncArrivalsAndDeparturesForStopResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncArrivalsAndDeparturesForStopResourceWithStreamingResponse:
        return AsyncArrivalsAndDeparturesForStopResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        stop_id: str,
        *,
        service_date: int,
        trip_id: str,
        stop_sequence: int | NotGiven = NOT_GIVEN,
        time: int | NotGiven = NOT_GIVEN,
        vehicle_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ArrivalsAndDeparturesForStopRetrieveResponse:
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
            f"/api/where/arrival-and-departure-for-stop/stopID.json",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "service_date": service_date,
                        "trip_id": trip_id,
                        "stop_sequence": stop_sequence,
                        "time": time,
                        "vehicle_id": vehicle_id,
                    },
                    arrivals_and_departures_for_stop_retrieve_params.ArrivalsAndDeparturesForStopRetrieveParams,
                ),
            ),
            cast_to=ArrivalsAndDeparturesForStopRetrieveResponse,
        )


class ArrivalsAndDeparturesForStopResourceWithRawResponse:
    def __init__(self, arrivals_and_departures_for_stop: ArrivalsAndDeparturesForStopResource) -> None:
        self._arrivals_and_departures_for_stop = arrivals_and_departures_for_stop

        self.retrieve = to_raw_response_wrapper(
            arrivals_and_departures_for_stop.retrieve,
        )


class AsyncArrivalsAndDeparturesForStopResourceWithRawResponse:
    def __init__(self, arrivals_and_departures_for_stop: AsyncArrivalsAndDeparturesForStopResource) -> None:
        self._arrivals_and_departures_for_stop = arrivals_and_departures_for_stop

        self.retrieve = async_to_raw_response_wrapper(
            arrivals_and_departures_for_stop.retrieve,
        )


class ArrivalsAndDeparturesForStopResourceWithStreamingResponse:
    def __init__(self, arrivals_and_departures_for_stop: ArrivalsAndDeparturesForStopResource) -> None:
        self._arrivals_and_departures_for_stop = arrivals_and_departures_for_stop

        self.retrieve = to_streamed_response_wrapper(
            arrivals_and_departures_for_stop.retrieve,
        )


class AsyncArrivalsAndDeparturesForStopResourceWithStreamingResponse:
    def __init__(self, arrivals_and_departures_for_stop: AsyncArrivalsAndDeparturesForStopResource) -> None:
        self._arrivals_and_departures_for_stop = arrivals_and_departures_for_stop

        self.retrieve = async_to_streamed_response_wrapper(
            arrivals_and_departures_for_stop.retrieve,
        )
