# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .config import (
    ConfigResource,
    AsyncConfigResource,
    ConfigResourceWithRawResponse,
    AsyncConfigResourceWithRawResponse,
    ConfigResourceWithStreamingResponse,
    AsyncConfigResourceWithStreamingResponse,
)
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from .current_time import (
    CurrentTimeResource,
    AsyncCurrentTimeResource,
    CurrentTimeResourceWithRawResponse,
    AsyncCurrentTimeResourceWithRawResponse,
    CurrentTimeResourceWithStreamingResponse,
    AsyncCurrentTimeResourceWithStreamingResponse,
)
from .stops_for_location import (
    StopsForLocationResource,
    AsyncStopsForLocationResource,
    StopsForLocationResourceWithRawResponse,
    AsyncStopsForLocationResourceWithRawResponse,
    StopsForLocationResourceWithStreamingResponse,
    AsyncStopsForLocationResourceWithStreamingResponse,
)
from .agencies_with_coverage import (
    AgenciesWithCoverageResource,
    AsyncAgenciesWithCoverageResource,
    AgenciesWithCoverageResourceWithRawResponse,
    AsyncAgenciesWithCoverageResourceWithRawResponse,
    AgenciesWithCoverageResourceWithStreamingResponse,
    AsyncAgenciesWithCoverageResourceWithStreamingResponse,
)
from .arrival_and_departure_for_stop import (
    ArrivalAndDepartureForStopResource,
    AsyncArrivalAndDepartureForStopResource,
    ArrivalAndDepartureForStopResourceWithRawResponse,
    AsyncArrivalAndDepartureForStopResourceWithRawResponse,
    ArrivalAndDepartureForStopResourceWithStreamingResponse,
    AsyncArrivalAndDepartureForStopResourceWithStreamingResponse,
)
from .arrivals_and_departures_for_stop import (
    ArrivalsAndDeparturesForStopResource,
    AsyncArrivalsAndDeparturesForStopResource,
    ArrivalsAndDeparturesForStopResourceWithRawResponse,
    AsyncArrivalsAndDeparturesForStopResourceWithRawResponse,
    ArrivalsAndDeparturesForStopResourceWithStreamingResponse,
    AsyncArrivalsAndDeparturesForStopResourceWithStreamingResponse,
)

__all__ = ["WhereResource", "AsyncWhereResource"]


class WhereResource(SyncAPIResource):
    @cached_property
    def agencies_with_coverage(self) -> AgenciesWithCoverageResource:
        return AgenciesWithCoverageResource(self._client)

    @cached_property
    def config(self) -> ConfigResource:
        return ConfigResource(self._client)

    @cached_property
    def current_time(self) -> CurrentTimeResource:
        return CurrentTimeResource(self._client)

    @cached_property
    def stops_for_location(self) -> StopsForLocationResource:
        return StopsForLocationResource(self._client)

    @cached_property
    def arrival_and_departure_for_stop(self) -> ArrivalAndDepartureForStopResource:
        return ArrivalAndDepartureForStopResource(self._client)

    @cached_property
    def arrivals_and_departures_for_stop(self) -> ArrivalsAndDeparturesForStopResource:
        return ArrivalsAndDeparturesForStopResource(self._client)

    @cached_property
    def with_raw_response(self) -> WhereResourceWithRawResponse:
        return WhereResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> WhereResourceWithStreamingResponse:
        return WhereResourceWithStreamingResponse(self)


class AsyncWhereResource(AsyncAPIResource):
    @cached_property
    def agencies_with_coverage(self) -> AsyncAgenciesWithCoverageResource:
        return AsyncAgenciesWithCoverageResource(self._client)

    @cached_property
    def config(self) -> AsyncConfigResource:
        return AsyncConfigResource(self._client)

    @cached_property
    def current_time(self) -> AsyncCurrentTimeResource:
        return AsyncCurrentTimeResource(self._client)

    @cached_property
    def stops_for_location(self) -> AsyncStopsForLocationResource:
        return AsyncStopsForLocationResource(self._client)

    @cached_property
    def arrival_and_departure_for_stop(self) -> AsyncArrivalAndDepartureForStopResource:
        return AsyncArrivalAndDepartureForStopResource(self._client)

    @cached_property
    def arrivals_and_departures_for_stop(self) -> AsyncArrivalsAndDeparturesForStopResource:
        return AsyncArrivalsAndDeparturesForStopResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncWhereResourceWithRawResponse:
        return AsyncWhereResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncWhereResourceWithStreamingResponse:
        return AsyncWhereResourceWithStreamingResponse(self)


class WhereResourceWithRawResponse:
    def __init__(self, where: WhereResource) -> None:
        self._where = where

    @cached_property
    def agencies_with_coverage(self) -> AgenciesWithCoverageResourceWithRawResponse:
        return AgenciesWithCoverageResourceWithRawResponse(self._where.agencies_with_coverage)

    @cached_property
    def config(self) -> ConfigResourceWithRawResponse:
        return ConfigResourceWithRawResponse(self._where.config)

    @cached_property
    def current_time(self) -> CurrentTimeResourceWithRawResponse:
        return CurrentTimeResourceWithRawResponse(self._where.current_time)

    @cached_property
    def stops_for_location(self) -> StopsForLocationResourceWithRawResponse:
        return StopsForLocationResourceWithRawResponse(self._where.stops_for_location)

    @cached_property
    def arrival_and_departure_for_stop(self) -> ArrivalAndDepartureForStopResourceWithRawResponse:
        return ArrivalAndDepartureForStopResourceWithRawResponse(self._where.arrival_and_departure_for_stop)

    @cached_property
    def arrivals_and_departures_for_stop(self) -> ArrivalsAndDeparturesForStopResourceWithRawResponse:
        return ArrivalsAndDeparturesForStopResourceWithRawResponse(self._where.arrivals_and_departures_for_stop)


class AsyncWhereResourceWithRawResponse:
    def __init__(self, where: AsyncWhereResource) -> None:
        self._where = where

    @cached_property
    def agencies_with_coverage(self) -> AsyncAgenciesWithCoverageResourceWithRawResponse:
        return AsyncAgenciesWithCoverageResourceWithRawResponse(self._where.agencies_with_coverage)

    @cached_property
    def config(self) -> AsyncConfigResourceWithRawResponse:
        return AsyncConfigResourceWithRawResponse(self._where.config)

    @cached_property
    def current_time(self) -> AsyncCurrentTimeResourceWithRawResponse:
        return AsyncCurrentTimeResourceWithRawResponse(self._where.current_time)

    @cached_property
    def stops_for_location(self) -> AsyncStopsForLocationResourceWithRawResponse:
        return AsyncStopsForLocationResourceWithRawResponse(self._where.stops_for_location)

    @cached_property
    def arrival_and_departure_for_stop(self) -> AsyncArrivalAndDepartureForStopResourceWithRawResponse:
        return AsyncArrivalAndDepartureForStopResourceWithRawResponse(self._where.arrival_and_departure_for_stop)

    @cached_property
    def arrivals_and_departures_for_stop(self) -> AsyncArrivalsAndDeparturesForStopResourceWithRawResponse:
        return AsyncArrivalsAndDeparturesForStopResourceWithRawResponse(self._where.arrivals_and_departures_for_stop)


class WhereResourceWithStreamingResponse:
    def __init__(self, where: WhereResource) -> None:
        self._where = where

    @cached_property
    def agencies_with_coverage(self) -> AgenciesWithCoverageResourceWithStreamingResponse:
        return AgenciesWithCoverageResourceWithStreamingResponse(self._where.agencies_with_coverage)

    @cached_property
    def config(self) -> ConfigResourceWithStreamingResponse:
        return ConfigResourceWithStreamingResponse(self._where.config)

    @cached_property
    def current_time(self) -> CurrentTimeResourceWithStreamingResponse:
        return CurrentTimeResourceWithStreamingResponse(self._where.current_time)

    @cached_property
    def stops_for_location(self) -> StopsForLocationResourceWithStreamingResponse:
        return StopsForLocationResourceWithStreamingResponse(self._where.stops_for_location)

    @cached_property
    def arrival_and_departure_for_stop(self) -> ArrivalAndDepartureForStopResourceWithStreamingResponse:
        return ArrivalAndDepartureForStopResourceWithStreamingResponse(self._where.arrival_and_departure_for_stop)

    @cached_property
    def arrivals_and_departures_for_stop(self) -> ArrivalsAndDeparturesForStopResourceWithStreamingResponse:
        return ArrivalsAndDeparturesForStopResourceWithStreamingResponse(self._where.arrivals_and_departures_for_stop)


class AsyncWhereResourceWithStreamingResponse:
    def __init__(self, where: AsyncWhereResource) -> None:
        self._where = where

    @cached_property
    def agencies_with_coverage(self) -> AsyncAgenciesWithCoverageResourceWithStreamingResponse:
        return AsyncAgenciesWithCoverageResourceWithStreamingResponse(self._where.agencies_with_coverage)

    @cached_property
    def config(self) -> AsyncConfigResourceWithStreamingResponse:
        return AsyncConfigResourceWithStreamingResponse(self._where.config)

    @cached_property
    def current_time(self) -> AsyncCurrentTimeResourceWithStreamingResponse:
        return AsyncCurrentTimeResourceWithStreamingResponse(self._where.current_time)

    @cached_property
    def stops_for_location(self) -> AsyncStopsForLocationResourceWithStreamingResponse:
        return AsyncStopsForLocationResourceWithStreamingResponse(self._where.stops_for_location)

    @cached_property
    def arrival_and_departure_for_stop(self) -> AsyncArrivalAndDepartureForStopResourceWithStreamingResponse:
        return AsyncArrivalAndDepartureForStopResourceWithStreamingResponse(self._where.arrival_and_departure_for_stop)

    @cached_property
    def arrivals_and_departures_for_stop(self) -> AsyncArrivalsAndDeparturesForStopResourceWithStreamingResponse:
        return AsyncArrivalsAndDeparturesForStopResourceWithStreamingResponse(
            self._where.arrivals_and_departures_for_stop
        )
