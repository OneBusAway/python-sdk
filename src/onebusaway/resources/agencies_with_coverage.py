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
from ..types.agencies_with_coverage_list_response import AgenciesWithCoverageListResponse

__all__ = ["AgenciesWithCoverageResource", "AsyncAgenciesWithCoverageResource"]


class AgenciesWithCoverageResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AgenciesWithCoverageResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/OneBusAway/python-sdk#accessing-raw-response-data-eg-headers
        """
        return AgenciesWithCoverageResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AgenciesWithCoverageResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/OneBusAway/python-sdk#with_streaming_response
        """
        return AgenciesWithCoverageResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AgenciesWithCoverageListResponse:
        """
        Returns a list of all transit agencies currently supported by OneBusAway along
        with the center of their coverage area.
        """
        return self._get(
            "/api/where/agencies-with-coverage.json",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AgenciesWithCoverageListResponse,
        )


class AsyncAgenciesWithCoverageResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncAgenciesWithCoverageResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/OneBusAway/python-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncAgenciesWithCoverageResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAgenciesWithCoverageResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/OneBusAway/python-sdk#with_streaming_response
        """
        return AsyncAgenciesWithCoverageResourceWithStreamingResponse(self)

    async def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AgenciesWithCoverageListResponse:
        """
        Returns a list of all transit agencies currently supported by OneBusAway along
        with the center of their coverage area.
        """
        return await self._get(
            "/api/where/agencies-with-coverage.json",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AgenciesWithCoverageListResponse,
        )


class AgenciesWithCoverageResourceWithRawResponse:
    def __init__(self, agencies_with_coverage: AgenciesWithCoverageResource) -> None:
        self._agencies_with_coverage = agencies_with_coverage

        self.list = to_raw_response_wrapper(
            agencies_with_coverage.list,
        )


class AsyncAgenciesWithCoverageResourceWithRawResponse:
    def __init__(self, agencies_with_coverage: AsyncAgenciesWithCoverageResource) -> None:
        self._agencies_with_coverage = agencies_with_coverage

        self.list = async_to_raw_response_wrapper(
            agencies_with_coverage.list,
        )


class AgenciesWithCoverageResourceWithStreamingResponse:
    def __init__(self, agencies_with_coverage: AgenciesWithCoverageResource) -> None:
        self._agencies_with_coverage = agencies_with_coverage

        self.list = to_streamed_response_wrapper(
            agencies_with_coverage.list,
        )


class AsyncAgenciesWithCoverageResourceWithStreamingResponse:
    def __init__(self, agencies_with_coverage: AsyncAgenciesWithCoverageResource) -> None:
        self._agencies_with_coverage = agencies_with_coverage

        self.list = async_to_streamed_response_wrapper(
            agencies_with_coverage.list,
        )
