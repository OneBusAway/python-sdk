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
from ..types.block_retrieve_response import BlockRetrieveResponse

__all__ = ["BlockResource", "AsyncBlockResource"]


class BlockResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> BlockResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/OneBusAway/python-sdk#accessing-raw-response-data-eg-headers
        """
        return BlockResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> BlockResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/OneBusAway/python-sdk#with_streaming_response
        """
        return BlockResourceWithStreamingResponse(self)

    def retrieve(
        self,
        block_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> BlockRetrieveResponse:
        """
        Get details of a specific block by ID

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not block_id:
            raise ValueError(f"Expected a non-empty value for `block_id` but received {block_id!r}")
        return self._get(
            f"/api/where/block/{block_id}.json",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BlockRetrieveResponse,
        )


class AsyncBlockResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncBlockResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/OneBusAway/python-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncBlockResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncBlockResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/OneBusAway/python-sdk#with_streaming_response
        """
        return AsyncBlockResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        block_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> BlockRetrieveResponse:
        """
        Get details of a specific block by ID

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not block_id:
            raise ValueError(f"Expected a non-empty value for `block_id` but received {block_id!r}")
        return await self._get(
            f"/api/where/block/{block_id}.json",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BlockRetrieveResponse,
        )


class BlockResourceWithRawResponse:
    def __init__(self, block: BlockResource) -> None:
        self._block = block

        self.retrieve = to_raw_response_wrapper(
            block.retrieve,
        )


class AsyncBlockResourceWithRawResponse:
    def __init__(self, block: AsyncBlockResource) -> None:
        self._block = block

        self.retrieve = async_to_raw_response_wrapper(
            block.retrieve,
        )


class BlockResourceWithStreamingResponse:
    def __init__(self, block: BlockResource) -> None:
        self._block = block

        self.retrieve = to_streamed_response_wrapper(
            block.retrieve,
        )


class AsyncBlockResourceWithStreamingResponse:
    def __init__(self, block: AsyncBlockResource) -> None:
        self._block = block

        self.retrieve = async_to_streamed_response_wrapper(
            block.retrieve,
        )
