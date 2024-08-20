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
from ..types.agency_retrieve_response import AgencyRetrieveResponse

__all__ = ["AgencyResource", "AsyncAgencyResource"]


class AgencyResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AgencyResourceWithRawResponse:
        return AgencyResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AgencyResourceWithStreamingResponse:
        return AgencyResourceWithStreamingResponse(self)

    def retrieve(
        self,
        agency_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AgencyRetrieveResponse:
        """
        Retrieve information for a specific transit agency identified by its unique ID.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not agency_id:
            raise ValueError(f"Expected a non-empty value for `agency_id` but received {agency_id!r}")
        return self._get(
            f"/api/where/agency/{agency_id}.json",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AgencyRetrieveResponse,
        )


class AsyncAgencyResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncAgencyResourceWithRawResponse:
        return AsyncAgencyResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAgencyResourceWithStreamingResponse:
        return AsyncAgencyResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        agency_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AgencyRetrieveResponse:
        """
        Retrieve information for a specific transit agency identified by its unique ID.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not agency_id:
            raise ValueError(f"Expected a non-empty value for `agency_id` but received {agency_id!r}")
        return await self._get(
            f"/api/where/agency/{agency_id}.json",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AgencyRetrieveResponse,
        )


class AgencyResourceWithRawResponse:
    def __init__(self, agency: AgencyResource) -> None:
        self._agency = agency

        self.retrieve = to_raw_response_wrapper(
            agency.retrieve,
        )


class AsyncAgencyResourceWithRawResponse:
    def __init__(self, agency: AsyncAgencyResource) -> None:
        self._agency = agency

        self.retrieve = async_to_raw_response_wrapper(
            agency.retrieve,
        )


class AgencyResourceWithStreamingResponse:
    def __init__(self, agency: AgencyResource) -> None:
        self._agency = agency

        self.retrieve = to_streamed_response_wrapper(
            agency.retrieve,
        )


class AsyncAgencyResourceWithStreamingResponse:
    def __init__(self, agency: AsyncAgencyResource) -> None:
        self._agency = agency

        self.retrieve = async_to_streamed_response_wrapper(
            agency.retrieve,
        )
