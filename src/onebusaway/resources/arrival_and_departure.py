# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import datetime

import httpx

from ..types import arrival_and_departure_list_params, arrival_and_departure_retrieve_params
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
from ..types.arrival_and_departure_list_response import ArrivalAndDepartureListResponse
from ..types.arrival_and_departure_retrieve_response import ArrivalAndDepartureRetrieveResponse

__all__ = ["ArrivalAndDepartureResource", "AsyncArrivalAndDepartureResource"]


class ArrivalAndDepartureResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ArrivalAndDepartureResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/OneBusAway/python-sdk#accessing-raw-response-data-eg-headers
        """
        return ArrivalAndDepartureResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ArrivalAndDepartureResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/OneBusAway/python-sdk#with_streaming_response
        """
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
            f"/api/where/arrival-and-departure-for-stop/{stop_id}.json",
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

    def list(
        self,
        stop_id: str,
        *,
        minutes_after: int | NotGiven = NOT_GIVEN,
        minutes_before: int | NotGiven = NOT_GIVEN,
        time: Union[str, datetime] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ArrivalAndDepartureListResponse:
        """
        arrivals-and-departures-for-stop

        Args:
          minutes_after: Include vehicles arriving or departing in the next n minutes.

          minutes_before: Include vehicles having arrived or departed in the previous n minutes.

          time: The specific time for querying the system status.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not stop_id:
            raise ValueError(f"Expected a non-empty value for `stop_id` but received {stop_id!r}")
        return self._get(
            f"/api/where/arrivals-and-departures-for-stop/{stop_id}.json",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "minutes_after": minutes_after,
                        "minutes_before": minutes_before,
                        "time": time,
                    },
                    arrival_and_departure_list_params.ArrivalAndDepartureListParams,
                ),
            ),
            cast_to=ArrivalAndDepartureListResponse,
        )


class AsyncArrivalAndDepartureResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncArrivalAndDepartureResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/OneBusAway/python-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncArrivalAndDepartureResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncArrivalAndDepartureResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/OneBusAway/python-sdk#with_streaming_response
        """
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
            f"/api/where/arrival-and-departure-for-stop/{stop_id}.json",
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

    async def list(
        self,
        stop_id: str,
        *,
        minutes_after: int | NotGiven = NOT_GIVEN,
        minutes_before: int | NotGiven = NOT_GIVEN,
        time: Union[str, datetime] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ArrivalAndDepartureListResponse:
        """
        arrivals-and-departures-for-stop

        Args:
          minutes_after: Include vehicles arriving or departing in the next n minutes.

          minutes_before: Include vehicles having arrived or departed in the previous n minutes.

          time: The specific time for querying the system status.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not stop_id:
            raise ValueError(f"Expected a non-empty value for `stop_id` but received {stop_id!r}")
        return await self._get(
            f"/api/where/arrivals-and-departures-for-stop/{stop_id}.json",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "minutes_after": minutes_after,
                        "minutes_before": minutes_before,
                        "time": time,
                    },
                    arrival_and_departure_list_params.ArrivalAndDepartureListParams,
                ),
            ),
            cast_to=ArrivalAndDepartureListResponse,
        )


class ArrivalAndDepartureResourceWithRawResponse:
    def __init__(self, arrival_and_departure: ArrivalAndDepartureResource) -> None:
        self._arrival_and_departure = arrival_and_departure

        self.retrieve = to_raw_response_wrapper(
            arrival_and_departure.retrieve,
        )
        self.list = to_raw_response_wrapper(
            arrival_and_departure.list,
        )


class AsyncArrivalAndDepartureResourceWithRawResponse:
    def __init__(self, arrival_and_departure: AsyncArrivalAndDepartureResource) -> None:
        self._arrival_and_departure = arrival_and_departure

        self.retrieve = async_to_raw_response_wrapper(
            arrival_and_departure.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            arrival_and_departure.list,
        )


class ArrivalAndDepartureResourceWithStreamingResponse:
    def __init__(self, arrival_and_departure: ArrivalAndDepartureResource) -> None:
        self._arrival_and_departure = arrival_and_departure

        self.retrieve = to_streamed_response_wrapper(
            arrival_and_departure.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            arrival_and_departure.list,
        )


class AsyncArrivalAndDepartureResourceWithStreamingResponse:
    def __init__(self, arrival_and_departure: AsyncArrivalAndDepartureResource) -> None:
        self._arrival_and_departure = arrival_and_departure

        self.retrieve = async_to_streamed_response_wrapper(
            arrival_and_departure.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            arrival_and_departure.list,
        )
