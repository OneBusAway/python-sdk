# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..types import arrivals_and_departures_for_stop_retrieve_params
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

__all__ = ["ArrivalsAndDeparturesForStop", "AsyncArrivalsAndDeparturesForStop"]


class ArrivalsAndDeparturesForStop(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ArrivalsAndDeparturesForStopWithRawResponse:
        return ArrivalsAndDeparturesForStopWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ArrivalsAndDeparturesForStopWithStreamingResponse:
        return ArrivalsAndDeparturesForStopWithStreamingResponse(self)

    def retrieve(
        self,
        stop_id_json: str,
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
        arrivals-and-departures-for-stop

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not stop_id_json:
            raise ValueError(f"Expected a non-empty value for `stop_id_json` but received {stop_id_json!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._get(
            f"/api/where/arrivals-and-departures-for-stop/{stop_id_json}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"key": key},
                    arrivals_and_departures_for_stop_retrieve_params.ArrivalsAndDeparturesForStopRetrieveParams,
                ),
            ),
            cast_to=NoneType,
        )


class AsyncArrivalsAndDeparturesForStop(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncArrivalsAndDeparturesForStopWithRawResponse:
        return AsyncArrivalsAndDeparturesForStopWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncArrivalsAndDeparturesForStopWithStreamingResponse:
        return AsyncArrivalsAndDeparturesForStopWithStreamingResponse(self)

    async def retrieve(
        self,
        stop_id_json: str,
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
        arrivals-and-departures-for-stop

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not stop_id_json:
            raise ValueError(f"Expected a non-empty value for `stop_id_json` but received {stop_id_json!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._get(
            f"/api/where/arrivals-and-departures-for-stop/{stop_id_json}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"key": key},
                    arrivals_and_departures_for_stop_retrieve_params.ArrivalsAndDeparturesForStopRetrieveParams,
                ),
            ),
            cast_to=NoneType,
        )


class ArrivalsAndDeparturesForStopWithRawResponse:
    def __init__(self, arrivals_and_departures_for_stop: ArrivalsAndDeparturesForStop) -> None:
        self._arrivals_and_departures_for_stop = arrivals_and_departures_for_stop

        self.retrieve = to_raw_response_wrapper(
            arrivals_and_departures_for_stop.retrieve,
        )


class AsyncArrivalsAndDeparturesForStopWithRawResponse:
    def __init__(self, arrivals_and_departures_for_stop: AsyncArrivalsAndDeparturesForStop) -> None:
        self._arrivals_and_departures_for_stop = arrivals_and_departures_for_stop

        self.retrieve = async_to_raw_response_wrapper(
            arrivals_and_departures_for_stop.retrieve,
        )


class ArrivalsAndDeparturesForStopWithStreamingResponse:
    def __init__(self, arrivals_and_departures_for_stop: ArrivalsAndDeparturesForStop) -> None:
        self._arrivals_and_departures_for_stop = arrivals_and_departures_for_stop

        self.retrieve = to_streamed_response_wrapper(
            arrivals_and_departures_for_stop.retrieve,
        )


class AsyncArrivalsAndDeparturesForStopWithStreamingResponse:
    def __init__(self, arrivals_and_departures_for_stop: AsyncArrivalsAndDeparturesForStop) -> None:
        self._arrivals_and_departures_for_stop = arrivals_and_departures_for_stop

        self.retrieve = async_to_streamed_response_wrapper(
            arrivals_and_departures_for_stop.retrieve,
        )
