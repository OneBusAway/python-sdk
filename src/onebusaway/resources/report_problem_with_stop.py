# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from ..types import report_problem_with_stop_retrieve_params
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

__all__ = ["ReportProblemWithStopResource", "AsyncReportProblemWithStopResource"]


class ReportProblemWithStopResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ReportProblemWithStopResourceWithRawResponse:
        return ReportProblemWithStopResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ReportProblemWithStopResourceWithStreamingResponse:
        return ReportProblemWithStopResourceWithStreamingResponse(self)

    def retrieve(
        self,
        stop_id: str,
        *,
        code: Literal["stop_name_wrong", "stop_number_wrong", "stop_location_wrong", "route_or_trip_missing", "other"]
        | NotGiven = NOT_GIVEN,
        user_comment: str | NotGiven = NOT_GIVEN,
        user_lat: float | NotGiven = NOT_GIVEN,
        user_location_accuracy: float | NotGiven = NOT_GIVEN,
        user_lon: float | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ResponseWrapper:
        """
        Submit a user-generated problem report for a stop

        Args:
          code: A string code identifying the nature of the problem

          user_comment: Additional comment text supplied by the user describing the problem

          user_lat: The reporting user’s current latitude

          user_location_accuracy: The reporting user’s location accuracy, in meters

          user_lon: The reporting user’s current longitude

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not stop_id:
            raise ValueError(f"Expected a non-empty value for `stop_id` but received {stop_id!r}")
        return self._get(
            f"/api/where/report-problem-with-stop/{stop_id}.json",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "code": code,
                        "user_comment": user_comment,
                        "user_lat": user_lat,
                        "user_location_accuracy": user_location_accuracy,
                        "user_lon": user_lon,
                    },
                    report_problem_with_stop_retrieve_params.ReportProblemWithStopRetrieveParams,
                ),
            ),
            cast_to=ResponseWrapper,
        )


class AsyncReportProblemWithStopResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncReportProblemWithStopResourceWithRawResponse:
        return AsyncReportProblemWithStopResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncReportProblemWithStopResourceWithStreamingResponse:
        return AsyncReportProblemWithStopResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        stop_id: str,
        *,
        code: Literal["stop_name_wrong", "stop_number_wrong", "stop_location_wrong", "route_or_trip_missing", "other"]
        | NotGiven = NOT_GIVEN,
        user_comment: str | NotGiven = NOT_GIVEN,
        user_lat: float | NotGiven = NOT_GIVEN,
        user_location_accuracy: float | NotGiven = NOT_GIVEN,
        user_lon: float | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> ResponseWrapper:
        """
        Submit a user-generated problem report for a stop

        Args:
          code: A string code identifying the nature of the problem

          user_comment: Additional comment text supplied by the user describing the problem

          user_lat: The reporting user’s current latitude

          user_location_accuracy: The reporting user’s location accuracy, in meters

          user_lon: The reporting user’s current longitude

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not stop_id:
            raise ValueError(f"Expected a non-empty value for `stop_id` but received {stop_id!r}")
        return await self._get(
            f"/api/where/report-problem-with-stop/{stop_id}.json",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "code": code,
                        "user_comment": user_comment,
                        "user_lat": user_lat,
                        "user_location_accuracy": user_location_accuracy,
                        "user_lon": user_lon,
                    },
                    report_problem_with_stop_retrieve_params.ReportProblemWithStopRetrieveParams,
                ),
            ),
            cast_to=ResponseWrapper,
        )


class ReportProblemWithStopResourceWithRawResponse:
    def __init__(self, report_problem_with_stop: ReportProblemWithStopResource) -> None:
        self._report_problem_with_stop = report_problem_with_stop

        self.retrieve = to_raw_response_wrapper(
            report_problem_with_stop.retrieve,
        )


class AsyncReportProblemWithStopResourceWithRawResponse:
    def __init__(self, report_problem_with_stop: AsyncReportProblemWithStopResource) -> None:
        self._report_problem_with_stop = report_problem_with_stop

        self.retrieve = async_to_raw_response_wrapper(
            report_problem_with_stop.retrieve,
        )


class ReportProblemWithStopResourceWithStreamingResponse:
    def __init__(self, report_problem_with_stop: ReportProblemWithStopResource) -> None:
        self._report_problem_with_stop = report_problem_with_stop

        self.retrieve = to_streamed_response_wrapper(
            report_problem_with_stop.retrieve,
        )


class AsyncReportProblemWithStopResourceWithStreamingResponse:
    def __init__(self, report_problem_with_stop: AsyncReportProblemWithStopResource) -> None:
        self._report_problem_with_stop = report_problem_with_stop

        self.retrieve = async_to_streamed_response_wrapper(
            report_problem_with_stop.retrieve,
        )
