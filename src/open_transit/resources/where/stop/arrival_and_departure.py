# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ...._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ...._utils import (
    maybe_transform,
    async_maybe_transform,
)
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
from ....types.where.stop import arrival_and_departure_retrieve_params
from ....types.where.stop.arrival_and_departure_retrieve_response import ArrivalAndDepartureRetrieveResponse

__all__ = ["ArrivalAndDepartureResource", "AsyncArrivalAndDepartureResource"]


class ArrivalAndDepartureResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ArrivalAndDepartureResourceWithRawResponse:
        return ArrivalAndDepartureResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ArrivalAndDepartureResourceWithStreamingResponse:
        return ArrivalAndDepartureResourceWithStreamingResponse(self)

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
    ) -> ArrivalAndDepartureRetrieveResponse:
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
                    arrival_and_departure_retrieve_params.ArrivalAndDepartureRetrieveParams,
                ),
            ),
            cast_to=ArrivalAndDepartureRetrieveResponse,
        )


class AsyncArrivalAndDepartureResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncArrivalAndDepartureResourceWithRawResponse:
        return AsyncArrivalAndDepartureResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncArrivalAndDepartureResourceWithStreamingResponse:
        return AsyncArrivalAndDepartureResourceWithStreamingResponse(self)

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
    ) -> ArrivalAndDepartureRetrieveResponse:
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
                    arrival_and_departure_retrieve_params.ArrivalAndDepartureRetrieveParams,
                ),
            ),
            cast_to=ArrivalAndDepartureRetrieveResponse,
        )


class ArrivalAndDepartureResourceWithRawResponse:
    def __init__(self, arrival_and_departure: ArrivalAndDepartureResource) -> None:
        self._arrival_and_departure = arrival_and_departure

        self.retrieve = to_raw_response_wrapper(
            arrival_and_departure.retrieve,
        )


class AsyncArrivalAndDepartureResourceWithRawResponse:
    def __init__(self, arrival_and_departure: AsyncArrivalAndDepartureResource) -> None:
        self._arrival_and_departure = arrival_and_departure

        self.retrieve = async_to_raw_response_wrapper(
            arrival_and_departure.retrieve,
        )


class ArrivalAndDepartureResourceWithStreamingResponse:
    def __init__(self, arrival_and_departure: ArrivalAndDepartureResource) -> None:
        self._arrival_and_departure = arrival_and_departure

        self.retrieve = to_streamed_response_wrapper(
            arrival_and_departure.retrieve,
        )


class AsyncArrivalAndDepartureResourceWithStreamingResponse:
    def __init__(self, arrival_and_departure: AsyncArrivalAndDepartureResource) -> None:
        self._arrival_and_departure = arrival_and_departure

        self.retrieve = async_to_streamed_response_wrapper(
            arrival_and_departure.retrieve,
        )
