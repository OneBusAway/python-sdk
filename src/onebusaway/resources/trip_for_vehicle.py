# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..types import trip_for_vehicle_retrieve_params
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
from ..types.trip_for_vehicle_retrieve_response import TripForVehicleRetrieveResponse

__all__ = ["TripForVehicleResource", "AsyncTripForVehicleResource"]


class TripForVehicleResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> TripForVehicleResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/OneBusAway/python-sdk#accessing-raw-response-data-eg-headers
        """
        return TripForVehicleResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> TripForVehicleResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/OneBusAway/python-sdk#with_streaming_response
        """
        return TripForVehicleResourceWithStreamingResponse(self)

    def retrieve(
        self,
        vehicle_id: str,
        *,
        include_schedule: bool | NotGiven = NOT_GIVEN,
        include_status: bool | NotGiven = NOT_GIVEN,
        include_trip: bool | NotGiven = NOT_GIVEN,
        time: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TripForVehicleRetrieveResponse:
        """
        Retrieve trip for a specific vehicle

        Args:
          include_schedule: Determines whether full <schedule/> element is included in the <tripDetails/>
              section. Defaults to false.

          include_status: Determines whether the full <status/> element is included in the <tripDetails/>
              section. Defaults to true.

          include_trip: Determines whether full <trip/> element is included in the <references/>
              section. Defaults to false.

          time: Time parameter to query the system at a specific time (optional).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not vehicle_id:
            raise ValueError(f"Expected a non-empty value for `vehicle_id` but received {vehicle_id!r}")
        return self._get(
            f"/api/where/trip-for-vehicle/{vehicle_id}.json",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "include_schedule": include_schedule,
                        "include_status": include_status,
                        "include_trip": include_trip,
                        "time": time,
                    },
                    trip_for_vehicle_retrieve_params.TripForVehicleRetrieveParams,
                ),
            ),
            cast_to=TripForVehicleRetrieveResponse,
        )


class AsyncTripForVehicleResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncTripForVehicleResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/OneBusAway/python-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncTripForVehicleResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncTripForVehicleResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/OneBusAway/python-sdk#with_streaming_response
        """
        return AsyncTripForVehicleResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        vehicle_id: str,
        *,
        include_schedule: bool | NotGiven = NOT_GIVEN,
        include_status: bool | NotGiven = NOT_GIVEN,
        include_trip: bool | NotGiven = NOT_GIVEN,
        time: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> TripForVehicleRetrieveResponse:
        """
        Retrieve trip for a specific vehicle

        Args:
          include_schedule: Determines whether full <schedule/> element is included in the <tripDetails/>
              section. Defaults to false.

          include_status: Determines whether the full <status/> element is included in the <tripDetails/>
              section. Defaults to true.

          include_trip: Determines whether full <trip/> element is included in the <references/>
              section. Defaults to false.

          time: Time parameter to query the system at a specific time (optional).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not vehicle_id:
            raise ValueError(f"Expected a non-empty value for `vehicle_id` but received {vehicle_id!r}")
        return await self._get(
            f"/api/where/trip-for-vehicle/{vehicle_id}.json",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "include_schedule": include_schedule,
                        "include_status": include_status,
                        "include_trip": include_trip,
                        "time": time,
                    },
                    trip_for_vehicle_retrieve_params.TripForVehicleRetrieveParams,
                ),
            ),
            cast_to=TripForVehicleRetrieveResponse,
        )


class TripForVehicleResourceWithRawResponse:
    def __init__(self, trip_for_vehicle: TripForVehicleResource) -> None:
        self._trip_for_vehicle = trip_for_vehicle

        self.retrieve = to_raw_response_wrapper(
            trip_for_vehicle.retrieve,
        )


class AsyncTripForVehicleResourceWithRawResponse:
    def __init__(self, trip_for_vehicle: AsyncTripForVehicleResource) -> None:
        self._trip_for_vehicle = trip_for_vehicle

        self.retrieve = async_to_raw_response_wrapper(
            trip_for_vehicle.retrieve,
        )


class TripForVehicleResourceWithStreamingResponse:
    def __init__(self, trip_for_vehicle: TripForVehicleResource) -> None:
        self._trip_for_vehicle = trip_for_vehicle

        self.retrieve = to_streamed_response_wrapper(
            trip_for_vehicle.retrieve,
        )


class AsyncTripForVehicleResourceWithStreamingResponse:
    def __init__(self, trip_for_vehicle: AsyncTripForVehicleResource) -> None:
        self._trip_for_vehicle = trip_for_vehicle

        self.retrieve = async_to_streamed_response_wrapper(
            trip_for_vehicle.retrieve,
        )
