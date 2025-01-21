# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.stop_ids_for_agency_list_response import StopIDsForAgencyListResponse

__all__ = ["StopIDsForAgencyResource", "AsyncStopIDsForAgencyResource"]


class StopIDsForAgencyResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> StopIDsForAgencyResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/OneBusAway/python-sdk#accessing-raw-response-data-eg-headers
        """
        return StopIDsForAgencyResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> StopIDsForAgencyResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/OneBusAway/python-sdk#with_streaming_response
        """
        return StopIDsForAgencyResourceWithStreamingResponse(self)

    def list(
        self,
        agency_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> StopIDsForAgencyListResponse:
        """
        Get stop IDs for a specific agency

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not agency_id:
            raise ValueError(f"Expected a non-empty value for `agency_id` but received {agency_id!r}")
        return self._get(
            f"/api/where/stop-ids-for-agency/{agency_id}.json",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=StopIDsForAgencyListResponse,
        )


class AsyncStopIDsForAgencyResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncStopIDsForAgencyResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/OneBusAway/python-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncStopIDsForAgencyResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncStopIDsForAgencyResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/OneBusAway/python-sdk#with_streaming_response
        """
        return AsyncStopIDsForAgencyResourceWithStreamingResponse(self)

    async def list(
        self,
        agency_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> StopIDsForAgencyListResponse:
        """
        Get stop IDs for a specific agency

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not agency_id:
            raise ValueError(f"Expected a non-empty value for `agency_id` but received {agency_id!r}")
        return await self._get(
            f"/api/where/stop-ids-for-agency/{agency_id}.json",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=StopIDsForAgencyListResponse,
        )


class StopIDsForAgencyResourceWithRawResponse:
    def __init__(self, stop_ids_for_agency: StopIDsForAgencyResource) -> None:
        self._stop_ids_for_agency = stop_ids_for_agency

        self.list = to_raw_response_wrapper(
            stop_ids_for_agency.list,
        )


class AsyncStopIDsForAgencyResourceWithRawResponse:
    def __init__(self, stop_ids_for_agency: AsyncStopIDsForAgencyResource) -> None:
        self._stop_ids_for_agency = stop_ids_for_agency

        self.list = async_to_raw_response_wrapper(
            stop_ids_for_agency.list,
        )


class StopIDsForAgencyResourceWithStreamingResponse:
    def __init__(self, stop_ids_for_agency: StopIDsForAgencyResource) -> None:
        self._stop_ids_for_agency = stop_ids_for_agency

        self.list = to_streamed_response_wrapper(
            stop_ids_for_agency.list,
        )


class AsyncStopIDsForAgencyResourceWithStreamingResponse:
    def __init__(self, stop_ids_for_agency: AsyncStopIDsForAgencyResource) -> None:
        self._stop_ids_for_agency = stop_ids_for_agency

        self.list = async_to_streamed_response_wrapper(
            stop_ids_for_agency.list,
        )
