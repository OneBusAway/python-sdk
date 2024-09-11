# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from ..types import report_problem_with_trip_retrieve_params
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
from ..types.shared.response_wrapper import ResponseWrapper

__all__ = ["ReportProblemWithTripResource", "AsyncReportProblemWithTripResource"]


class ReportProblemWithTripResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ReportProblemWithTripResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/OneBusAway/python-sdk#accessing-raw-response-data-eg-headers
        """
        return ReportProblemWithTripResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ReportProblemWithTripResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/OneBusAway/python-sdk#with_streaming_response
        """
        return ReportProblemWithTripResourceWithStreamingResponse(self)

    def retrieve(
        self,
        trip_id: str,
        *,
        code: Literal[
            "vehicle_never_came",
            "vehicle_came_early",
            "vehicle_came_late",
            "wrong_headsign",
            "vehicle_does_not_stop_here",
            "other",
        ]
        | NotGiven = NOT_GIVEN,
        service_date: int | NotGiven = NOT_GIVEN,
        stop_id: str | NotGiven = NOT_GIVEN,
        user_comment: str | NotGiven = NOT_GIVEN,
        user_lat: float | NotGiven = NOT_GIVEN,
        user_location_accuracy: float | NotGiven = NOT_GIVEN,
        user_lon: float | NotGiven = NOT_GIVEN,
        user_on_vehicle: bool | NotGiven = NOT_GIVEN,
        user_vehicle_number: str | NotGiven = NOT_GIVEN,
        vehicle_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ResponseWrapper:
        """
        Submit a user-generated problem report for a particular trip.

        Args:
          code: A string code identifying the nature of the problem

          service_date: The service date of the trip

          stop_id: A stop ID indicating where the user is experiencing the problem

          user_comment: Additional comment text supplied by the user describing the problem

          user_lat: The reporting user’s current latitude

          user_location_accuracy: The reporting user’s location accuracy, in meters

          user_lon: The reporting user’s current longitude

          user_on_vehicle: Indicator if the user is on the transit vehicle experiencing the problem

          user_vehicle_number: The vehicle number, as reported by the user

          vehicle_id: The vehicle actively serving the trip

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not trip_id:
            raise ValueError(f"Expected a non-empty value for `trip_id` but received {trip_id!r}")
        return self._get(
            f"/api/where/report-problem-with-trip/{trip_id}.json",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "code": code,
                        "service_date": service_date,
                        "stop_id": stop_id,
                        "user_comment": user_comment,
                        "user_lat": user_lat,
                        "user_location_accuracy": user_location_accuracy,
                        "user_lon": user_lon,
                        "user_on_vehicle": user_on_vehicle,
                        "user_vehicle_number": user_vehicle_number,
                        "vehicle_id": vehicle_id,
                    },
                    report_problem_with_trip_retrieve_params.ReportProblemWithTripRetrieveParams,
                ),
            ),
            cast_to=ResponseWrapper,
        )


class AsyncReportProblemWithTripResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncReportProblemWithTripResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/OneBusAway/python-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncReportProblemWithTripResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncReportProblemWithTripResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/OneBusAway/python-sdk#with_streaming_response
        """
        return AsyncReportProblemWithTripResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        trip_id: str,
        *,
        code: Literal[
            "vehicle_never_came",
            "vehicle_came_early",
            "vehicle_came_late",
            "wrong_headsign",
            "vehicle_does_not_stop_here",
            "other",
        ]
        | NotGiven = NOT_GIVEN,
        service_date: int | NotGiven = NOT_GIVEN,
        stop_id: str | NotGiven = NOT_GIVEN,
        user_comment: str | NotGiven = NOT_GIVEN,
        user_lat: float | NotGiven = NOT_GIVEN,
        user_location_accuracy: float | NotGiven = NOT_GIVEN,
        user_lon: float | NotGiven = NOT_GIVEN,
        user_on_vehicle: bool | NotGiven = NOT_GIVEN,
        user_vehicle_number: str | NotGiven = NOT_GIVEN,
        vehicle_id: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ResponseWrapper:
        """
        Submit a user-generated problem report for a particular trip.

        Args:
          code: A string code identifying the nature of the problem

          service_date: The service date of the trip

          stop_id: A stop ID indicating where the user is experiencing the problem

          user_comment: Additional comment text supplied by the user describing the problem

          user_lat: The reporting user’s current latitude

          user_location_accuracy: The reporting user’s location accuracy, in meters

          user_lon: The reporting user’s current longitude

          user_on_vehicle: Indicator if the user is on the transit vehicle experiencing the problem

          user_vehicle_number: The vehicle number, as reported by the user

          vehicle_id: The vehicle actively serving the trip

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not trip_id:
            raise ValueError(f"Expected a non-empty value for `trip_id` but received {trip_id!r}")
        return await self._get(
            f"/api/where/report-problem-with-trip/{trip_id}.json",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "code": code,
                        "service_date": service_date,
                        "stop_id": stop_id,
                        "user_comment": user_comment,
                        "user_lat": user_lat,
                        "user_location_accuracy": user_location_accuracy,
                        "user_lon": user_lon,
                        "user_on_vehicle": user_on_vehicle,
                        "user_vehicle_number": user_vehicle_number,
                        "vehicle_id": vehicle_id,
                    },
                    report_problem_with_trip_retrieve_params.ReportProblemWithTripRetrieveParams,
                ),
            ),
            cast_to=ResponseWrapper,
        )


class ReportProblemWithTripResourceWithRawResponse:
    def __init__(self, report_problem_with_trip: ReportProblemWithTripResource) -> None:
        self._report_problem_with_trip = report_problem_with_trip

        self.retrieve = to_raw_response_wrapper(
            report_problem_with_trip.retrieve,
        )


class AsyncReportProblemWithTripResourceWithRawResponse:
    def __init__(self, report_problem_with_trip: AsyncReportProblemWithTripResource) -> None:
        self._report_problem_with_trip = report_problem_with_trip

        self.retrieve = async_to_raw_response_wrapper(
            report_problem_with_trip.retrieve,
        )


class ReportProblemWithTripResourceWithStreamingResponse:
    def __init__(self, report_problem_with_trip: ReportProblemWithTripResource) -> None:
        self._report_problem_with_trip = report_problem_with_trip

        self.retrieve = to_streamed_response_wrapper(
            report_problem_with_trip.retrieve,
        )


class AsyncReportProblemWithTripResourceWithStreamingResponse:
    def __init__(self, report_problem_with_trip: AsyncReportProblemWithTripResource) -> None:
        self._report_problem_with_trip = report_problem_with_trip

        self.retrieve = async_to_streamed_response_wrapper(
            report_problem_with_trip.retrieve,
        )
