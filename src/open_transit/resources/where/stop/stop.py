# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from .arrival_and_departure import (
    ArrivalAndDepartureResource,
    AsyncArrivalAndDepartureResource,
    ArrivalAndDepartureResourceWithRawResponse,
    AsyncArrivalAndDepartureResourceWithRawResponse,
    ArrivalAndDepartureResourceWithStreamingResponse,
    AsyncArrivalAndDepartureResourceWithStreamingResponse,
)
from .arrivals_and_departures import (
    ArrivalsAndDeparturesResource,
    AsyncArrivalsAndDeparturesResource,
    ArrivalsAndDeparturesResourceWithRawResponse,
    AsyncArrivalsAndDeparturesResourceWithRawResponse,
    ArrivalsAndDeparturesResourceWithStreamingResponse,
    AsyncArrivalsAndDeparturesResourceWithStreamingResponse,
)

__all__ = ["StopResource", "AsyncStopResource"]


class StopResource(SyncAPIResource):
    @cached_property
    def arrival_and_departure(self) -> ArrivalAndDepartureResource:
        return ArrivalAndDepartureResource(self._client)

    @cached_property
    def arrivals_and_departures(self) -> ArrivalsAndDeparturesResource:
        return ArrivalsAndDeparturesResource(self._client)

    @cached_property
    def with_raw_response(self) -> StopResourceWithRawResponse:
        return StopResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> StopResourceWithStreamingResponse:
        return StopResourceWithStreamingResponse(self)


class AsyncStopResource(AsyncAPIResource):
    @cached_property
    def arrival_and_departure(self) -> AsyncArrivalAndDepartureResource:
        return AsyncArrivalAndDepartureResource(self._client)

    @cached_property
    def arrivals_and_departures(self) -> AsyncArrivalsAndDeparturesResource:
        return AsyncArrivalsAndDeparturesResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncStopResourceWithRawResponse:
        return AsyncStopResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncStopResourceWithStreamingResponse:
        return AsyncStopResourceWithStreamingResponse(self)


class StopResourceWithRawResponse:
    def __init__(self, stop: StopResource) -> None:
        self._stop = stop

    @cached_property
    def arrival_and_departure(self) -> ArrivalAndDepartureResourceWithRawResponse:
        return ArrivalAndDepartureResourceWithRawResponse(self._stop.arrival_and_departure)

    @cached_property
    def arrivals_and_departures(self) -> ArrivalsAndDeparturesResourceWithRawResponse:
        return ArrivalsAndDeparturesResourceWithRawResponse(self._stop.arrivals_and_departures)


class AsyncStopResourceWithRawResponse:
    def __init__(self, stop: AsyncStopResource) -> None:
        self._stop = stop

    @cached_property
    def arrival_and_departure(self) -> AsyncArrivalAndDepartureResourceWithRawResponse:
        return AsyncArrivalAndDepartureResourceWithRawResponse(self._stop.arrival_and_departure)

    @cached_property
    def arrivals_and_departures(self) -> AsyncArrivalsAndDeparturesResourceWithRawResponse:
        return AsyncArrivalsAndDeparturesResourceWithRawResponse(self._stop.arrivals_and_departures)


class StopResourceWithStreamingResponse:
    def __init__(self, stop: StopResource) -> None:
        self._stop = stop

    @cached_property
    def arrival_and_departure(self) -> ArrivalAndDepartureResourceWithStreamingResponse:
        return ArrivalAndDepartureResourceWithStreamingResponse(self._stop.arrival_and_departure)

    @cached_property
    def arrivals_and_departures(self) -> ArrivalsAndDeparturesResourceWithStreamingResponse:
        return ArrivalsAndDeparturesResourceWithStreamingResponse(self._stop.arrivals_and_departures)


class AsyncStopResourceWithStreamingResponse:
    def __init__(self, stop: AsyncStopResource) -> None:
        self._stop = stop

    @cached_property
    def arrival_and_departure(self) -> AsyncArrivalAndDepartureResourceWithStreamingResponse:
        return AsyncArrivalAndDepartureResourceWithStreamingResponse(self._stop.arrival_and_departure)

    @cached_property
    def arrivals_and_departures(self) -> AsyncArrivalsAndDeparturesResourceWithStreamingResponse:
        return AsyncArrivalsAndDeparturesResourceWithStreamingResponse(self._stop.arrivals_and_departures)
