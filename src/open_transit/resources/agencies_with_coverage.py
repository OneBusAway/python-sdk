# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..types import agencies_with_coverage_list_params
from .._types import NOT_GIVEN, Body, Query, Headers, NoneType, NotGiven
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
from .._base_client import (
    make_request_options,
)

__all__ = ["AgenciesWithCoverage", "AsyncAgenciesWithCoverage"]


class AgenciesWithCoverage(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AgenciesWithCoverageWithRawResponse:
        return AgenciesWithCoverageWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AgenciesWithCoverageWithStreamingResponse:
        return AgenciesWithCoverageWithStreamingResponse(self)

    def list(
        self,
        *,
        key: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        agencies-with-coverage

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._get(
            "/api/where/agencies-with-coverage.json",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"key": key}, agencies_with_coverage_list_params.AgenciesWithCoverageListParams),
            ),
            cast_to=NoneType,
        )


class AsyncAgenciesWithCoverage(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncAgenciesWithCoverageWithRawResponse:
        return AsyncAgenciesWithCoverageWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAgenciesWithCoverageWithStreamingResponse:
        return AsyncAgenciesWithCoverageWithStreamingResponse(self)

    async def list(
        self,
        *,
        key: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        agencies-with-coverage

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._get(
            "/api/where/agencies-with-coverage.json",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"key": key}, agencies_with_coverage_list_params.AgenciesWithCoverageListParams
                ),
            ),
            cast_to=NoneType,
        )


class AgenciesWithCoverageWithRawResponse:
    def __init__(self, agencies_with_coverage: AgenciesWithCoverage) -> None:
        self._agencies_with_coverage = agencies_with_coverage

        self.list = to_raw_response_wrapper(
            agencies_with_coverage.list,
        )


class AsyncAgenciesWithCoverageWithRawResponse:
    def __init__(self, agencies_with_coverage: AsyncAgenciesWithCoverage) -> None:
        self._agencies_with_coverage = agencies_with_coverage

        self.list = async_to_raw_response_wrapper(
            agencies_with_coverage.list,
        )


class AgenciesWithCoverageWithStreamingResponse:
    def __init__(self, agencies_with_coverage: AgenciesWithCoverage) -> None:
        self._agencies_with_coverage = agencies_with_coverage

        self.list = to_streamed_response_wrapper(
            agencies_with_coverage.list,
        )


class AsyncAgenciesWithCoverageWithStreamingResponse:
    def __init__(self, agencies_with_coverage: AsyncAgenciesWithCoverage) -> None:
        self._agencies_with_coverage = agencies_with_coverage

        self.list = async_to_streamed_response_wrapper(
            agencies_with_coverage.list,
        )
