# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .stop import (
    StopResource,
    AsyncStopResource,
    StopResourceWithRawResponse,
    AsyncStopResourceWithRawResponse,
    StopResourceWithStreamingResponse,
    AsyncStopResourceWithStreamingResponse,
)
from .config import (
    ConfigResource,
    AsyncConfigResource,
    ConfigResourceWithRawResponse,
    AsyncConfigResourceWithRawResponse,
    ConfigResourceWithStreamingResponse,
    AsyncConfigResourceWithStreamingResponse,
)
from ..._compat import cached_property
from .stop.stop import StopResource, AsyncStopResource
from ..._resource import SyncAPIResource, AsyncAPIResource
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
    def stop(self) -> StopResource:
        return StopResource(self._client)

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
    def stop(self) -> AsyncStopResource:
        return AsyncStopResource(self._client)

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
    def stop(self) -> StopResourceWithRawResponse:
        return StopResourceWithRawResponse(self._where.stop)


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
    def stop(self) -> AsyncStopResourceWithRawResponse:
        return AsyncStopResourceWithRawResponse(self._where.stop)


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
    def stop(self) -> StopResourceWithStreamingResponse:
        return StopResourceWithStreamingResponse(self._where.stop)


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
    def stop(self) -> AsyncStopResourceWithStreamingResponse:
        return AsyncStopResourceWithStreamingResponse(self._where.stop)
