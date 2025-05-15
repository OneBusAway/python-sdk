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
from ..types.stops_for_agency_list_response import StopsForAgencyListResponse

__all__ = ["StopsForAgencyResource", "AsyncStopsForAgencyResource"]


class StopsForAgencyResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> StopsForAgencyResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/OneBusAway/python-sdk#accessing-raw-response-data-eg-headers
        """
        return StopsForAgencyResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> StopsForAgencyResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/OneBusAway/python-sdk#with_streaming_response
        """
        return StopsForAgencyResourceWithStreamingResponse(self)

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
    ) -> StopsForAgencyListResponse:
        """
        Get stops for a specific agency

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not agency_id:
            raise ValueError(f"Expected a non-empty value for `agency_id` but received {agency_id!r}")
        return self._get(
            f"/api/where/stops-for-agency/{agency_id}.json",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=StopsForAgencyListResponse,
        )


class AsyncStopsForAgencyResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncStopsForAgencyResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/OneBusAway/python-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncStopsForAgencyResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncStopsForAgencyResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/OneBusAway/python-sdk#with_streaming_response
        """
        return AsyncStopsForAgencyResourceWithStreamingResponse(self)

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
    ) -> StopsForAgencyListResponse:
        """
        Get stops for a specific agency

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not agency_id:
            raise ValueError(f"Expected a non-empty value for `agency_id` but received {agency_id!r}")
        return await self._get(
            f"/api/where/stops-for-agency/{agency_id}.json",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=StopsForAgencyListResponse,
        )


class StopsForAgencyResourceWithRawResponse:
    def __init__(self, stops_for_agency: StopsForAgencyResource) -> None:
        self._stops_for_agency = stops_for_agency

        self.list = to_raw_response_wrapper(
            stops_for_agency.list,
        )


class AsyncStopsForAgencyResourceWithRawResponse:
    def __init__(self, stops_for_agency: AsyncStopsForAgencyResource) -> None:
        self._stops_for_agency = stops_for_agency

        self.list = async_to_raw_response_wrapper(
            stops_for_agency.list,
        )


class StopsForAgencyResourceWithStreamingResponse:
    def __init__(self, stops_for_agency: StopsForAgencyResource) -> None:
        self._stops_for_agency = stops_for_agency

        self.list = to_streamed_response_wrapper(
            stops_for_agency.list,
        )


class AsyncStopsForAgencyResourceWithStreamingResponse:
    def __init__(self, stops_for_agency: AsyncStopsForAgencyResource) -> None:
        self._stops_for_agency = stops_for_agency

        self.list = async_to_streamed_response_wrapper(
            stops_for_agency.list,
        )
