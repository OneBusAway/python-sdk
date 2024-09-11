# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..types import search_for_stop_list_params
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
from ..types.search_for_stop_list_response import SearchForStopListResponse

__all__ = ["SearchForStopResource", "AsyncSearchForStopResource"]


class SearchForStopResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> SearchForStopResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/OneBusAway/python-sdk#accessing-raw-response-data-eg-headers
        """
        return SearchForStopResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SearchForStopResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/OneBusAway/python-sdk#with_streaming_response
        """
        return SearchForStopResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        input: str,
        max_count: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SearchForStopListResponse:
        """
        Search for a stop based on its name.

        Args:
          input: The string to search for.

          max_count: The max number of results to return. Defaults to 20.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/api/where/search/stop.json",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "input": input,
                        "max_count": max_count,
                    },
                    search_for_stop_list_params.SearchForStopListParams,
                ),
            ),
            cast_to=SearchForStopListResponse,
        )


class AsyncSearchForStopResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncSearchForStopResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/OneBusAway/python-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncSearchForStopResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSearchForStopResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/OneBusAway/python-sdk#with_streaming_response
        """
        return AsyncSearchForStopResourceWithStreamingResponse(self)

    async def list(
        self,
        *,
        input: str,
        max_count: int | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SearchForStopListResponse:
        """
        Search for a stop based on its name.

        Args:
          input: The string to search for.

          max_count: The max number of results to return. Defaults to 20.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/api/where/search/stop.json",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "input": input,
                        "max_count": max_count,
                    },
                    search_for_stop_list_params.SearchForStopListParams,
                ),
            ),
            cast_to=SearchForStopListResponse,
        )


class SearchForStopResourceWithRawResponse:
    def __init__(self, search_for_stop: SearchForStopResource) -> None:
        self._search_for_stop = search_for_stop

        self.list = to_raw_response_wrapper(
            search_for_stop.list,
        )


class AsyncSearchForStopResourceWithRawResponse:
    def __init__(self, search_for_stop: AsyncSearchForStopResource) -> None:
        self._search_for_stop = search_for_stop

        self.list = async_to_raw_response_wrapper(
            search_for_stop.list,
        )


class SearchForStopResourceWithStreamingResponse:
    def __init__(self, search_for_stop: SearchForStopResource) -> None:
        self._search_for_stop = search_for_stop

        self.list = to_streamed_response_wrapper(
            search_for_stop.list,
        )


class AsyncSearchForStopResourceWithStreamingResponse:
    def __init__(self, search_for_stop: AsyncSearchForStopResource) -> None:
        self._search_for_stop = search_for_stop

        self.list = async_to_streamed_response_wrapper(
            search_for_stop.list,
        )
