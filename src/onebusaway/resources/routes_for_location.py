# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..types import routes_for_location_retrieve_params
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
from ..types.routes_for_location_retrieve_response import RoutesForLocationRetrieveResponse

__all__ = ["RoutesForLocationResource", "AsyncRoutesForLocationResource"]


class RoutesForLocationResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> RoutesForLocationResourceWithRawResponse:
        return RoutesForLocationResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> RoutesForLocationResourceWithStreamingResponse:
        return RoutesForLocationResourceWithStreamingResponse(self)

    def retrieve(
        self,
        *,
        lat: float,
        lon: float,
        lat_span: float | NotGiven = NOT_GIVEN,
        lon_span: float | NotGiven = NOT_GIVEN,
        query: str | NotGiven = NOT_GIVEN,
        radius: float | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> RoutesForLocationRetrieveResponse:
        """
        routes-for-location

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/api/where/routes-for-location.json",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "lat": lat,
                        "lon": lon,
                        "lat_span": lat_span,
                        "lon_span": lon_span,
                        "query": query,
                        "radius": radius,
                    },
                    routes_for_location_retrieve_params.RoutesForLocationRetrieveParams,
                ),
            ),
            cast_to=RoutesForLocationRetrieveResponse,
        )


class AsyncRoutesForLocationResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncRoutesForLocationResourceWithRawResponse:
        return AsyncRoutesForLocationResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncRoutesForLocationResourceWithStreamingResponse:
        return AsyncRoutesForLocationResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        *,
        lat: float,
        lon: float,
        lat_span: float | NotGiven = NOT_GIVEN,
        lon_span: float | NotGiven = NOT_GIVEN,
        query: str | NotGiven = NOT_GIVEN,
        radius: float | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> RoutesForLocationRetrieveResponse:
        """
        routes-for-location

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/api/where/routes-for-location.json",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "lat": lat,
                        "lon": lon,
                        "lat_span": lat_span,
                        "lon_span": lon_span,
                        "query": query,
                        "radius": radius,
                    },
                    routes_for_location_retrieve_params.RoutesForLocationRetrieveParams,
                ),
            ),
            cast_to=RoutesForLocationRetrieveResponse,
        )


class RoutesForLocationResourceWithRawResponse:
    def __init__(self, routes_for_location: RoutesForLocationResource) -> None:
        self._routes_for_location = routes_for_location

        self.retrieve = to_raw_response_wrapper(
            routes_for_location.retrieve,
        )


class AsyncRoutesForLocationResourceWithRawResponse:
    def __init__(self, routes_for_location: AsyncRoutesForLocationResource) -> None:
        self._routes_for_location = routes_for_location

        self.retrieve = async_to_raw_response_wrapper(
            routes_for_location.retrieve,
        )


class RoutesForLocationResourceWithStreamingResponse:
    def __init__(self, routes_for_location: RoutesForLocationResource) -> None:
        self._routes_for_location = routes_for_location

        self.retrieve = to_streamed_response_wrapper(
            routes_for_location.retrieve,
        )


class AsyncRoutesForLocationResourceWithStreamingResponse:
    def __init__(self, routes_for_location: AsyncRoutesForLocationResource) -> None:
        self._routes_for_location = routes_for_location

        self.retrieve = async_to_streamed_response_wrapper(
            routes_for_location.retrieve,
        )
