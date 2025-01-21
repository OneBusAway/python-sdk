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
from ..types.routes_for_agency_list_response import RoutesForAgencyListResponse

__all__ = ["RoutesForAgencyResource", "AsyncRoutesForAgencyResource"]


class RoutesForAgencyResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> RoutesForAgencyResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/OneBusAway/python-sdk#accessing-raw-response-data-eg-headers
        """
        return RoutesForAgencyResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> RoutesForAgencyResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/OneBusAway/python-sdk#with_streaming_response
        """
        return RoutesForAgencyResourceWithStreamingResponse(self)

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
    ) -> RoutesForAgencyListResponse:
        """
        Retrieve the list of all routes for a particular agency by id

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not agency_id:
            raise ValueError(f"Expected a non-empty value for `agency_id` but received {agency_id!r}")
        return self._get(
            f"/api/where/routes-for-agency/{agency_id}.json",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RoutesForAgencyListResponse,
        )


class AsyncRoutesForAgencyResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncRoutesForAgencyResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/OneBusAway/python-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncRoutesForAgencyResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncRoutesForAgencyResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/OneBusAway/python-sdk#with_streaming_response
        """
        return AsyncRoutesForAgencyResourceWithStreamingResponse(self)

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
    ) -> RoutesForAgencyListResponse:
        """
        Retrieve the list of all routes for a particular agency by id

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not agency_id:
            raise ValueError(f"Expected a non-empty value for `agency_id` but received {agency_id!r}")
        return await self._get(
            f"/api/where/routes-for-agency/{agency_id}.json",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RoutesForAgencyListResponse,
        )


class RoutesForAgencyResourceWithRawResponse:
    def __init__(self, routes_for_agency: RoutesForAgencyResource) -> None:
        self._routes_for_agency = routes_for_agency

        self.list = to_raw_response_wrapper(
            routes_for_agency.list,
        )


class AsyncRoutesForAgencyResourceWithRawResponse:
    def __init__(self, routes_for_agency: AsyncRoutesForAgencyResource) -> None:
        self._routes_for_agency = routes_for_agency

        self.list = async_to_raw_response_wrapper(
            routes_for_agency.list,
        )


class RoutesForAgencyResourceWithStreamingResponse:
    def __init__(self, routes_for_agency: RoutesForAgencyResource) -> None:
        self._routes_for_agency = routes_for_agency

        self.list = to_streamed_response_wrapper(
            routes_for_agency.list,
        )


class AsyncRoutesForAgencyResourceWithStreamingResponse:
    def __init__(self, routes_for_agency: AsyncRoutesForAgencyResource) -> None:
        self._routes_for_agency = routes_for_agency

        self.list = async_to_streamed_response_wrapper(
            routes_for_agency.list,
        )
