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
from ..types.route_retrieve_response import RouteRetrieveResponse

__all__ = ["RouteResource", "AsyncRouteResource"]


class RouteResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> RouteResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/OneBusAway/python-sdk#accessing-raw-response-data-eg-headers
        """
        return RouteResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> RouteResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/OneBusAway/python-sdk#with_streaming_response
        """
        return RouteResourceWithStreamingResponse(self)

    def retrieve(
        self,
        route_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> RouteRetrieveResponse:
        """
        Retrieve information for a specific route identified by its unique ID.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not route_id:
            raise ValueError(f"Expected a non-empty value for `route_id` but received {route_id!r}")
        return self._get(
            f"/api/where/route/{route_id}.json",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RouteRetrieveResponse,
        )


class AsyncRouteResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncRouteResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/OneBusAway/python-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncRouteResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncRouteResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/OneBusAway/python-sdk#with_streaming_response
        """
        return AsyncRouteResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        route_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> RouteRetrieveResponse:
        """
        Retrieve information for a specific route identified by its unique ID.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not route_id:
            raise ValueError(f"Expected a non-empty value for `route_id` but received {route_id!r}")
        return await self._get(
            f"/api/where/route/{route_id}.json",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RouteRetrieveResponse,
        )


class RouteResourceWithRawResponse:
    def __init__(self, route: RouteResource) -> None:
        self._route = route

        self.retrieve = to_raw_response_wrapper(
            route.retrieve,
        )


class AsyncRouteResourceWithRawResponse:
    def __init__(self, route: AsyncRouteResource) -> None:
        self._route = route

        self.retrieve = async_to_raw_response_wrapper(
            route.retrieve,
        )


class RouteResourceWithStreamingResponse:
    def __init__(self, route: RouteResource) -> None:
        self._route = route

        self.retrieve = to_streamed_response_wrapper(
            route.retrieve,
        )


class AsyncRouteResourceWithStreamingResponse:
    def __init__(self, route: AsyncRouteResource) -> None:
        self._route = route

        self.retrieve = async_to_streamed_response_wrapper(
            route.retrieve,
        )
