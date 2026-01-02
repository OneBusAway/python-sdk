# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import TYPE_CHECKING, Any, Mapping
from typing_extensions import Self, override

import httpx

from . import _exceptions
from ._qs import Querystring
from ._types import (
    Omit,
    Timeout,
    NotGiven,
    Transport,
    ProxiesTypes,
    RequestOptions,
    not_given,
)
from ._utils import is_given, get_async_library
from ._compat import cached_property
from ._version import __version__
from ._streaming import Stream as Stream, AsyncStream as AsyncStream
from ._exceptions import APIStatusError, OnebusawaySDKError
from ._base_client import (
    DEFAULT_MAX_RETRIES,
    SyncAPIClient,
    AsyncAPIClient,
)

if TYPE_CHECKING:
    from .resources import (
        stop,
        trip,
        block,
        route,
        shape,
        agency,
        config,
        current_time,
        trip_details,
        search_for_stop,
        stops_for_route,
        trips_for_route,
        search_for_route,
        stops_for_agency,
        trip_for_vehicle,
        routes_for_agency,
        schedule_for_stop,
        schedule_for_route,
        stops_for_location,
        trips_for_location,
        routes_for_location,
        stop_ids_for_agency,
        vehicles_for_agency,
        route_ids_for_agency,
        arrival_and_departure,
        agencies_with_coverage,
        report_problem_with_stop,
        report_problem_with_trip,
    )
    from .resources.stop import StopResource, AsyncStopResource
    from .resources.trip import TripResource, AsyncTripResource
    from .resources.block import BlockResource, AsyncBlockResource
    from .resources.route import RouteResource, AsyncRouteResource
    from .resources.shape import ShapeResource, AsyncShapeResource
    from .resources.agency import AgencyResource, AsyncAgencyResource
    from .resources.config import ConfigResource, AsyncConfigResource
    from .resources.current_time import CurrentTimeResource, AsyncCurrentTimeResource
    from .resources.trip_details import TripDetailsResource, AsyncTripDetailsResource
    from .resources.search_for_stop import SearchForStopResource, AsyncSearchForStopResource
    from .resources.stops_for_route import StopsForRouteResource, AsyncStopsForRouteResource
    from .resources.trips_for_route import TripsForRouteResource, AsyncTripsForRouteResource
    from .resources.search_for_route import SearchForRouteResource, AsyncSearchForRouteResource
    from .resources.stops_for_agency import StopsForAgencyResource, AsyncStopsForAgencyResource
    from .resources.trip_for_vehicle import TripForVehicleResource, AsyncTripForVehicleResource
    from .resources.routes_for_agency import RoutesForAgencyResource, AsyncRoutesForAgencyResource
    from .resources.schedule_for_stop import ScheduleForStopResource, AsyncScheduleForStopResource
    from .resources.schedule_for_route import ScheduleForRouteResource, AsyncScheduleForRouteResource
    from .resources.stops_for_location import StopsForLocationResource, AsyncStopsForLocationResource
    from .resources.trips_for_location import TripsForLocationResource, AsyncTripsForLocationResource
    from .resources.routes_for_location import RoutesForLocationResource, AsyncRoutesForLocationResource
    from .resources.stop_ids_for_agency import StopIDsForAgencyResource, AsyncStopIDsForAgencyResource
    from .resources.vehicles_for_agency import VehiclesForAgencyResource, AsyncVehiclesForAgencyResource
    from .resources.route_ids_for_agency import RouteIDsForAgencyResource, AsyncRouteIDsForAgencyResource
    from .resources.arrival_and_departure import ArrivalAndDepartureResource, AsyncArrivalAndDepartureResource
    from .resources.agencies_with_coverage import AgenciesWithCoverageResource, AsyncAgenciesWithCoverageResource
    from .resources.report_problem_with_stop import ReportProblemWithStopResource, AsyncReportProblemWithStopResource
    from .resources.report_problem_with_trip import ReportProblemWithTripResource, AsyncReportProblemWithTripResource

__all__ = [
    "Timeout",
    "Transport",
    "ProxiesTypes",
    "RequestOptions",
    "OnebusawaySDK",
    "AsyncOnebusawaySDK",
    "Client",
    "AsyncClient",
]


class OnebusawaySDK(SyncAPIClient):
    # client options
    api_key: str

    def __init__(
        self,
        *,
        api_key: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
        max_retries: int = DEFAULT_MAX_RETRIES,
        default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        # Configure a custom httpx client.
        # We provide a `DefaultHttpxClient` class that you can pass to retain the default values we use for `limits`, `timeout` & `follow_redirects`.
        # See the [httpx documentation](https://www.python-httpx.org/api/#client) for more details.
        http_client: httpx.Client | None = None,
        # Enable or disable schema validation for data returned by the API.
        # When enabled an error APIResponseValidationError is raised
        # if the API responds with invalid data for the expected schema.
        #
        # This parameter may be removed or changed in the future.
        # If you rely on this feature, please open a GitHub issue
        # outlining your use-case to help us decide if it should be
        # part of our public interface in the future.
        _strict_response_validation: bool = False,
    ) -> None:
        """Construct a new synchronous OnebusawaySDK client instance.

        This automatically infers the `api_key` argument from the `ONEBUSAWAY_API_KEY` environment variable if it is not provided.
        """
        if api_key is None:
            api_key = os.environ.get("ONEBUSAWAY_API_KEY")
        if api_key is None:
            raise OnebusawaySDKError(
                "The api_key client option must be set either by passing api_key to the client or by setting the ONEBUSAWAY_API_KEY environment variable"
            )
        self.api_key = api_key

        if base_url is None:
            base_url = os.environ.get("ONEBUSAWAY_SDK_BASE_URL")
        if base_url is None:
            base_url = f"https://api.pugetsound.onebusaway.org"

        super().__init__(
            version=__version__,
            base_url=base_url,
            max_retries=max_retries,
            timeout=timeout,
            http_client=http_client,
            custom_headers=default_headers,
            custom_query=default_query,
            _strict_response_validation=_strict_response_validation,
        )

    @cached_property
    def agencies_with_coverage(self) -> AgenciesWithCoverageResource:
        from .resources.agencies_with_coverage import AgenciesWithCoverageResource

        return AgenciesWithCoverageResource(self)

    @cached_property
    def agency(self) -> AgencyResource:
        from .resources.agency import AgencyResource

        return AgencyResource(self)

    @cached_property
    def vehicles_for_agency(self) -> VehiclesForAgencyResource:
        from .resources.vehicles_for_agency import VehiclesForAgencyResource

        return VehiclesForAgencyResource(self)

    @cached_property
    def config(self) -> ConfigResource:
        from .resources.config import ConfigResource

        return ConfigResource(self)

    @cached_property
    def current_time(self) -> CurrentTimeResource:
        from .resources.current_time import CurrentTimeResource

        return CurrentTimeResource(self)

    @cached_property
    def stops_for_location(self) -> StopsForLocationResource:
        from .resources.stops_for_location import StopsForLocationResource

        return StopsForLocationResource(self)

    @cached_property
    def stops_for_route(self) -> StopsForRouteResource:
        from .resources.stops_for_route import StopsForRouteResource

        return StopsForRouteResource(self)

    @cached_property
    def stops_for_agency(self) -> StopsForAgencyResource:
        from .resources.stops_for_agency import StopsForAgencyResource

        return StopsForAgencyResource(self)

    @cached_property
    def stop(self) -> StopResource:
        from .resources.stop import StopResource

        return StopResource(self)

    @cached_property
    def stop_ids_for_agency(self) -> StopIDsForAgencyResource:
        from .resources.stop_ids_for_agency import StopIDsForAgencyResource

        return StopIDsForAgencyResource(self)

    @cached_property
    def schedule_for_stop(self) -> ScheduleForStopResource:
        from .resources.schedule_for_stop import ScheduleForStopResource

        return ScheduleForStopResource(self)

    @cached_property
    def route(self) -> RouteResource:
        from .resources.route import RouteResource

        return RouteResource(self)

    @cached_property
    def route_ids_for_agency(self) -> RouteIDsForAgencyResource:
        from .resources.route_ids_for_agency import RouteIDsForAgencyResource

        return RouteIDsForAgencyResource(self)

    @cached_property
    def routes_for_location(self) -> RoutesForLocationResource:
        from .resources.routes_for_location import RoutesForLocationResource

        return RoutesForLocationResource(self)

    @cached_property
    def routes_for_agency(self) -> RoutesForAgencyResource:
        from .resources.routes_for_agency import RoutesForAgencyResource

        return RoutesForAgencyResource(self)

    @cached_property
    def schedule_for_route(self) -> ScheduleForRouteResource:
        from .resources.schedule_for_route import ScheduleForRouteResource

        return ScheduleForRouteResource(self)

    @cached_property
    def arrival_and_departure(self) -> ArrivalAndDepartureResource:
        from .resources.arrival_and_departure import ArrivalAndDepartureResource

        return ArrivalAndDepartureResource(self)

    @cached_property
    def trip(self) -> TripResource:
        from .resources.trip import TripResource

        return TripResource(self)

    @cached_property
    def trips_for_location(self) -> TripsForLocationResource:
        from .resources.trips_for_location import TripsForLocationResource

        return TripsForLocationResource(self)

    @cached_property
    def trip_details(self) -> TripDetailsResource:
        from .resources.trip_details import TripDetailsResource

        return TripDetailsResource(self)

    @cached_property
    def trip_for_vehicle(self) -> TripForVehicleResource:
        from .resources.trip_for_vehicle import TripForVehicleResource

        return TripForVehicleResource(self)

    @cached_property
    def trips_for_route(self) -> TripsForRouteResource:
        from .resources.trips_for_route import TripsForRouteResource

        return TripsForRouteResource(self)

    @cached_property
    def report_problem_with_stop(self) -> ReportProblemWithStopResource:
        from .resources.report_problem_with_stop import ReportProblemWithStopResource

        return ReportProblemWithStopResource(self)

    @cached_property
    def report_problem_with_trip(self) -> ReportProblemWithTripResource:
        from .resources.report_problem_with_trip import ReportProblemWithTripResource

        return ReportProblemWithTripResource(self)

    @cached_property
    def search_for_stop(self) -> SearchForStopResource:
        from .resources.search_for_stop import SearchForStopResource

        return SearchForStopResource(self)

    @cached_property
    def search_for_route(self) -> SearchForRouteResource:
        from .resources.search_for_route import SearchForRouteResource

        return SearchForRouteResource(self)

    @cached_property
    def block(self) -> BlockResource:
        from .resources.block import BlockResource

        return BlockResource(self)

    @cached_property
    def shape(self) -> ShapeResource:
        from .resources.shape import ShapeResource

        return ShapeResource(self)

    @cached_property
    def with_raw_response(self) -> OnebusawaySDKWithRawResponse:
        return OnebusawaySDKWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> OnebusawaySDKWithStreamedResponse:
        return OnebusawaySDKWithStreamedResponse(self)

    @property
    @override
    def qs(self) -> Querystring:
        return Querystring(array_format="repeat")

    @property
    @override
    def auth_headers(self) -> dict[str, str]:
        return {}

    @property
    @override
    def default_headers(self) -> dict[str, str | Omit]:
        return {
            **super().default_headers,
            "X-Stainless-Async": "false",
            **self._custom_headers,
        }

    @property
    @override
    def default_query(self) -> dict[str, object]:
        return {
            **super().default_query,
            "key": self.api_key,
            **self._custom_query,
        }

    def copy(
        self,
        *,
        api_key: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
        http_client: httpx.Client | None = None,
        max_retries: int | NotGiven = not_given,
        default_headers: Mapping[str, str] | None = None,
        set_default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        set_default_query: Mapping[str, object] | None = None,
        _extra_kwargs: Mapping[str, Any] = {},
    ) -> Self:
        """
        Create a new client instance re-using the same options given to the current client with optional overriding.
        """
        if default_headers is not None and set_default_headers is not None:
            raise ValueError("The `default_headers` and `set_default_headers` arguments are mutually exclusive")

        if default_query is not None and set_default_query is not None:
            raise ValueError("The `default_query` and `set_default_query` arguments are mutually exclusive")

        headers = self._custom_headers
        if default_headers is not None:
            headers = {**headers, **default_headers}
        elif set_default_headers is not None:
            headers = set_default_headers

        params = self._custom_query
        if default_query is not None:
            params = {**params, **default_query}
        elif set_default_query is not None:
            params = set_default_query

        http_client = http_client or self._client
        return self.__class__(
            api_key=api_key or self.api_key,
            base_url=base_url or self.base_url,
            timeout=self.timeout if isinstance(timeout, NotGiven) else timeout,
            http_client=http_client,
            max_retries=max_retries if is_given(max_retries) else self.max_retries,
            default_headers=headers,
            default_query=params,
            **_extra_kwargs,
        )

    # Alias for `copy` for nicer inline usage, e.g.
    # client.with_options(timeout=10).foo.create(...)
    with_options = copy

    def _get_api_key_query_param(self) -> str | None:
        return self.api_key

    @override
    def _make_status_error(
        self,
        err_msg: str,
        *,
        body: object,
        response: httpx.Response,
    ) -> APIStatusError:
        if response.status_code == 400:
            return _exceptions.BadRequestError(err_msg, response=response, body=body)

        if response.status_code == 401:
            return _exceptions.AuthenticationError(err_msg, response=response, body=body)

        if response.status_code == 403:
            return _exceptions.PermissionDeniedError(err_msg, response=response, body=body)

        if response.status_code == 404:
            return _exceptions.NotFoundError(err_msg, response=response, body=body)

        if response.status_code == 409:
            return _exceptions.ConflictError(err_msg, response=response, body=body)

        if response.status_code == 422:
            return _exceptions.UnprocessableEntityError(err_msg, response=response, body=body)

        if response.status_code == 429:
            return _exceptions.RateLimitError(err_msg, response=response, body=body)

        if response.status_code >= 500:
            return _exceptions.InternalServerError(err_msg, response=response, body=body)
        return APIStatusError(err_msg, response=response, body=body)


class AsyncOnebusawaySDK(AsyncAPIClient):
    # client options
    api_key: str

    def __init__(
        self,
        *,
        api_key: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
        max_retries: int = DEFAULT_MAX_RETRIES,
        default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        # Configure a custom httpx client.
        # We provide a `DefaultAsyncHttpxClient` class that you can pass to retain the default values we use for `limits`, `timeout` & `follow_redirects`.
        # See the [httpx documentation](https://www.python-httpx.org/api/#asyncclient) for more details.
        http_client: httpx.AsyncClient | None = None,
        # Enable or disable schema validation for data returned by the API.
        # When enabled an error APIResponseValidationError is raised
        # if the API responds with invalid data for the expected schema.
        #
        # This parameter may be removed or changed in the future.
        # If you rely on this feature, please open a GitHub issue
        # outlining your use-case to help us decide if it should be
        # part of our public interface in the future.
        _strict_response_validation: bool = False,
    ) -> None:
        """Construct a new async AsyncOnebusawaySDK client instance.

        This automatically infers the `api_key` argument from the `ONEBUSAWAY_API_KEY` environment variable if it is not provided.
        """
        if api_key is None:
            api_key = os.environ.get("ONEBUSAWAY_API_KEY")
        if api_key is None:
            raise OnebusawaySDKError(
                "The api_key client option must be set either by passing api_key to the client or by setting the ONEBUSAWAY_API_KEY environment variable"
            )
        self.api_key = api_key

        if base_url is None:
            base_url = os.environ.get("ONEBUSAWAY_SDK_BASE_URL")
        if base_url is None:
            base_url = f"https://api.pugetsound.onebusaway.org"

        super().__init__(
            version=__version__,
            base_url=base_url,
            max_retries=max_retries,
            timeout=timeout,
            http_client=http_client,
            custom_headers=default_headers,
            custom_query=default_query,
            _strict_response_validation=_strict_response_validation,
        )

    @cached_property
    def agencies_with_coverage(self) -> AsyncAgenciesWithCoverageResource:
        from .resources.agencies_with_coverage import AsyncAgenciesWithCoverageResource

        return AsyncAgenciesWithCoverageResource(self)

    @cached_property
    def agency(self) -> AsyncAgencyResource:
        from .resources.agency import AsyncAgencyResource

        return AsyncAgencyResource(self)

    @cached_property
    def vehicles_for_agency(self) -> AsyncVehiclesForAgencyResource:
        from .resources.vehicles_for_agency import AsyncVehiclesForAgencyResource

        return AsyncVehiclesForAgencyResource(self)

    @cached_property
    def config(self) -> AsyncConfigResource:
        from .resources.config import AsyncConfigResource

        return AsyncConfigResource(self)

    @cached_property
    def current_time(self) -> AsyncCurrentTimeResource:
        from .resources.current_time import AsyncCurrentTimeResource

        return AsyncCurrentTimeResource(self)

    @cached_property
    def stops_for_location(self) -> AsyncStopsForLocationResource:
        from .resources.stops_for_location import AsyncStopsForLocationResource

        return AsyncStopsForLocationResource(self)

    @cached_property
    def stops_for_route(self) -> AsyncStopsForRouteResource:
        from .resources.stops_for_route import AsyncStopsForRouteResource

        return AsyncStopsForRouteResource(self)

    @cached_property
    def stops_for_agency(self) -> AsyncStopsForAgencyResource:
        from .resources.stops_for_agency import AsyncStopsForAgencyResource

        return AsyncStopsForAgencyResource(self)

    @cached_property
    def stop(self) -> AsyncStopResource:
        from .resources.stop import AsyncStopResource

        return AsyncStopResource(self)

    @cached_property
    def stop_ids_for_agency(self) -> AsyncStopIDsForAgencyResource:
        from .resources.stop_ids_for_agency import AsyncStopIDsForAgencyResource

        return AsyncStopIDsForAgencyResource(self)

    @cached_property
    def schedule_for_stop(self) -> AsyncScheduleForStopResource:
        from .resources.schedule_for_stop import AsyncScheduleForStopResource

        return AsyncScheduleForStopResource(self)

    @cached_property
    def route(self) -> AsyncRouteResource:
        from .resources.route import AsyncRouteResource

        return AsyncRouteResource(self)

    @cached_property
    def route_ids_for_agency(self) -> AsyncRouteIDsForAgencyResource:
        from .resources.route_ids_for_agency import AsyncRouteIDsForAgencyResource

        return AsyncRouteIDsForAgencyResource(self)

    @cached_property
    def routes_for_location(self) -> AsyncRoutesForLocationResource:
        from .resources.routes_for_location import AsyncRoutesForLocationResource

        return AsyncRoutesForLocationResource(self)

    @cached_property
    def routes_for_agency(self) -> AsyncRoutesForAgencyResource:
        from .resources.routes_for_agency import AsyncRoutesForAgencyResource

        return AsyncRoutesForAgencyResource(self)

    @cached_property
    def schedule_for_route(self) -> AsyncScheduleForRouteResource:
        from .resources.schedule_for_route import AsyncScheduleForRouteResource

        return AsyncScheduleForRouteResource(self)

    @cached_property
    def arrival_and_departure(self) -> AsyncArrivalAndDepartureResource:
        from .resources.arrival_and_departure import AsyncArrivalAndDepartureResource

        return AsyncArrivalAndDepartureResource(self)

    @cached_property
    def trip(self) -> AsyncTripResource:
        from .resources.trip import AsyncTripResource

        return AsyncTripResource(self)

    @cached_property
    def trips_for_location(self) -> AsyncTripsForLocationResource:
        from .resources.trips_for_location import AsyncTripsForLocationResource

        return AsyncTripsForLocationResource(self)

    @cached_property
    def trip_details(self) -> AsyncTripDetailsResource:
        from .resources.trip_details import AsyncTripDetailsResource

        return AsyncTripDetailsResource(self)

    @cached_property
    def trip_for_vehicle(self) -> AsyncTripForVehicleResource:
        from .resources.trip_for_vehicle import AsyncTripForVehicleResource

        return AsyncTripForVehicleResource(self)

    @cached_property
    def trips_for_route(self) -> AsyncTripsForRouteResource:
        from .resources.trips_for_route import AsyncTripsForRouteResource

        return AsyncTripsForRouteResource(self)

    @cached_property
    def report_problem_with_stop(self) -> AsyncReportProblemWithStopResource:
        from .resources.report_problem_with_stop import AsyncReportProblemWithStopResource

        return AsyncReportProblemWithStopResource(self)

    @cached_property
    def report_problem_with_trip(self) -> AsyncReportProblemWithTripResource:
        from .resources.report_problem_with_trip import AsyncReportProblemWithTripResource

        return AsyncReportProblemWithTripResource(self)

    @cached_property
    def search_for_stop(self) -> AsyncSearchForStopResource:
        from .resources.search_for_stop import AsyncSearchForStopResource

        return AsyncSearchForStopResource(self)

    @cached_property
    def search_for_route(self) -> AsyncSearchForRouteResource:
        from .resources.search_for_route import AsyncSearchForRouteResource

        return AsyncSearchForRouteResource(self)

    @cached_property
    def block(self) -> AsyncBlockResource:
        from .resources.block import AsyncBlockResource

        return AsyncBlockResource(self)

    @cached_property
    def shape(self) -> AsyncShapeResource:
        from .resources.shape import AsyncShapeResource

        return AsyncShapeResource(self)

    @cached_property
    def with_raw_response(self) -> AsyncOnebusawaySDKWithRawResponse:
        return AsyncOnebusawaySDKWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncOnebusawaySDKWithStreamedResponse:
        return AsyncOnebusawaySDKWithStreamedResponse(self)

    @property
    @override
    def qs(self) -> Querystring:
        return Querystring(array_format="repeat")

    @property
    @override
    def auth_headers(self) -> dict[str, str]:
        return {}

    @property
    @override
    def default_headers(self) -> dict[str, str | Omit]:
        return {
            **super().default_headers,
            "X-Stainless-Async": f"async:{get_async_library()}",
            **self._custom_headers,
        }

    @property
    @override
    def default_query(self) -> dict[str, object]:
        return {
            **super().default_query,
            "key": self.api_key,
            **self._custom_query,
        }

    def copy(
        self,
        *,
        api_key: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
        http_client: httpx.AsyncClient | None = None,
        max_retries: int | NotGiven = not_given,
        default_headers: Mapping[str, str] | None = None,
        set_default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        set_default_query: Mapping[str, object] | None = None,
        _extra_kwargs: Mapping[str, Any] = {},
    ) -> Self:
        """
        Create a new client instance re-using the same options given to the current client with optional overriding.
        """
        if default_headers is not None and set_default_headers is not None:
            raise ValueError("The `default_headers` and `set_default_headers` arguments are mutually exclusive")

        if default_query is not None and set_default_query is not None:
            raise ValueError("The `default_query` and `set_default_query` arguments are mutually exclusive")

        headers = self._custom_headers
        if default_headers is not None:
            headers = {**headers, **default_headers}
        elif set_default_headers is not None:
            headers = set_default_headers

        params = self._custom_query
        if default_query is not None:
            params = {**params, **default_query}
        elif set_default_query is not None:
            params = set_default_query

        http_client = http_client or self._client
        return self.__class__(
            api_key=api_key or self.api_key,
            base_url=base_url or self.base_url,
            timeout=self.timeout if isinstance(timeout, NotGiven) else timeout,
            http_client=http_client,
            max_retries=max_retries if is_given(max_retries) else self.max_retries,
            default_headers=headers,
            default_query=params,
            **_extra_kwargs,
        )

    # Alias for `copy` for nicer inline usage, e.g.
    # client.with_options(timeout=10).foo.create(...)
    with_options = copy

    def _get_api_key_query_param(self) -> str | None:
        return self.api_key

    @override
    def _make_status_error(
        self,
        err_msg: str,
        *,
        body: object,
        response: httpx.Response,
    ) -> APIStatusError:
        if response.status_code == 400:
            return _exceptions.BadRequestError(err_msg, response=response, body=body)

        if response.status_code == 401:
            return _exceptions.AuthenticationError(err_msg, response=response, body=body)

        if response.status_code == 403:
            return _exceptions.PermissionDeniedError(err_msg, response=response, body=body)

        if response.status_code == 404:
            return _exceptions.NotFoundError(err_msg, response=response, body=body)

        if response.status_code == 409:
            return _exceptions.ConflictError(err_msg, response=response, body=body)

        if response.status_code == 422:
            return _exceptions.UnprocessableEntityError(err_msg, response=response, body=body)

        if response.status_code == 429:
            return _exceptions.RateLimitError(err_msg, response=response, body=body)

        if response.status_code >= 500:
            return _exceptions.InternalServerError(err_msg, response=response, body=body)
        return APIStatusError(err_msg, response=response, body=body)


class OnebusawaySDKWithRawResponse:
    _client: OnebusawaySDK

    def __init__(self, client: OnebusawaySDK) -> None:
        self._client = client

    @cached_property
    def agencies_with_coverage(self) -> agencies_with_coverage.AgenciesWithCoverageResourceWithRawResponse:
        from .resources.agencies_with_coverage import AgenciesWithCoverageResourceWithRawResponse

        return AgenciesWithCoverageResourceWithRawResponse(self._client.agencies_with_coverage)

    @cached_property
    def agency(self) -> agency.AgencyResourceWithRawResponse:
        from .resources.agency import AgencyResourceWithRawResponse

        return AgencyResourceWithRawResponse(self._client.agency)

    @cached_property
    def vehicles_for_agency(self) -> vehicles_for_agency.VehiclesForAgencyResourceWithRawResponse:
        from .resources.vehicles_for_agency import VehiclesForAgencyResourceWithRawResponse

        return VehiclesForAgencyResourceWithRawResponse(self._client.vehicles_for_agency)

    @cached_property
    def config(self) -> config.ConfigResourceWithRawResponse:
        from .resources.config import ConfigResourceWithRawResponse

        return ConfigResourceWithRawResponse(self._client.config)

    @cached_property
    def current_time(self) -> current_time.CurrentTimeResourceWithRawResponse:
        from .resources.current_time import CurrentTimeResourceWithRawResponse

        return CurrentTimeResourceWithRawResponse(self._client.current_time)

    @cached_property
    def stops_for_location(self) -> stops_for_location.StopsForLocationResourceWithRawResponse:
        from .resources.stops_for_location import StopsForLocationResourceWithRawResponse

        return StopsForLocationResourceWithRawResponse(self._client.stops_for_location)

    @cached_property
    def stops_for_route(self) -> stops_for_route.StopsForRouteResourceWithRawResponse:
        from .resources.stops_for_route import StopsForRouteResourceWithRawResponse

        return StopsForRouteResourceWithRawResponse(self._client.stops_for_route)

    @cached_property
    def stops_for_agency(self) -> stops_for_agency.StopsForAgencyResourceWithRawResponse:
        from .resources.stops_for_agency import StopsForAgencyResourceWithRawResponse

        return StopsForAgencyResourceWithRawResponse(self._client.stops_for_agency)

    @cached_property
    def stop(self) -> stop.StopResourceWithRawResponse:
        from .resources.stop import StopResourceWithRawResponse

        return StopResourceWithRawResponse(self._client.stop)

    @cached_property
    def stop_ids_for_agency(self) -> stop_ids_for_agency.StopIDsForAgencyResourceWithRawResponse:
        from .resources.stop_ids_for_agency import StopIDsForAgencyResourceWithRawResponse

        return StopIDsForAgencyResourceWithRawResponse(self._client.stop_ids_for_agency)

    @cached_property
    def schedule_for_stop(self) -> schedule_for_stop.ScheduleForStopResourceWithRawResponse:
        from .resources.schedule_for_stop import ScheduleForStopResourceWithRawResponse

        return ScheduleForStopResourceWithRawResponse(self._client.schedule_for_stop)

    @cached_property
    def route(self) -> route.RouteResourceWithRawResponse:
        from .resources.route import RouteResourceWithRawResponse

        return RouteResourceWithRawResponse(self._client.route)

    @cached_property
    def route_ids_for_agency(self) -> route_ids_for_agency.RouteIDsForAgencyResourceWithRawResponse:
        from .resources.route_ids_for_agency import RouteIDsForAgencyResourceWithRawResponse

        return RouteIDsForAgencyResourceWithRawResponse(self._client.route_ids_for_agency)

    @cached_property
    def routes_for_location(self) -> routes_for_location.RoutesForLocationResourceWithRawResponse:
        from .resources.routes_for_location import RoutesForLocationResourceWithRawResponse

        return RoutesForLocationResourceWithRawResponse(self._client.routes_for_location)

    @cached_property
    def routes_for_agency(self) -> routes_for_agency.RoutesForAgencyResourceWithRawResponse:
        from .resources.routes_for_agency import RoutesForAgencyResourceWithRawResponse

        return RoutesForAgencyResourceWithRawResponse(self._client.routes_for_agency)

    @cached_property
    def schedule_for_route(self) -> schedule_for_route.ScheduleForRouteResourceWithRawResponse:
        from .resources.schedule_for_route import ScheduleForRouteResourceWithRawResponse

        return ScheduleForRouteResourceWithRawResponse(self._client.schedule_for_route)

    @cached_property
    def arrival_and_departure(self) -> arrival_and_departure.ArrivalAndDepartureResourceWithRawResponse:
        from .resources.arrival_and_departure import ArrivalAndDepartureResourceWithRawResponse

        return ArrivalAndDepartureResourceWithRawResponse(self._client.arrival_and_departure)

    @cached_property
    def trip(self) -> trip.TripResourceWithRawResponse:
        from .resources.trip import TripResourceWithRawResponse

        return TripResourceWithRawResponse(self._client.trip)

    @cached_property
    def trips_for_location(self) -> trips_for_location.TripsForLocationResourceWithRawResponse:
        from .resources.trips_for_location import TripsForLocationResourceWithRawResponse

        return TripsForLocationResourceWithRawResponse(self._client.trips_for_location)

    @cached_property
    def trip_details(self) -> trip_details.TripDetailsResourceWithRawResponse:
        from .resources.trip_details import TripDetailsResourceWithRawResponse

        return TripDetailsResourceWithRawResponse(self._client.trip_details)

    @cached_property
    def trip_for_vehicle(self) -> trip_for_vehicle.TripForVehicleResourceWithRawResponse:
        from .resources.trip_for_vehicle import TripForVehicleResourceWithRawResponse

        return TripForVehicleResourceWithRawResponse(self._client.trip_for_vehicle)

    @cached_property
    def trips_for_route(self) -> trips_for_route.TripsForRouteResourceWithRawResponse:
        from .resources.trips_for_route import TripsForRouteResourceWithRawResponse

        return TripsForRouteResourceWithRawResponse(self._client.trips_for_route)

    @cached_property
    def report_problem_with_stop(self) -> report_problem_with_stop.ReportProblemWithStopResourceWithRawResponse:
        from .resources.report_problem_with_stop import ReportProblemWithStopResourceWithRawResponse

        return ReportProblemWithStopResourceWithRawResponse(self._client.report_problem_with_stop)

    @cached_property
    def report_problem_with_trip(self) -> report_problem_with_trip.ReportProblemWithTripResourceWithRawResponse:
        from .resources.report_problem_with_trip import ReportProblemWithTripResourceWithRawResponse

        return ReportProblemWithTripResourceWithRawResponse(self._client.report_problem_with_trip)

    @cached_property
    def search_for_stop(self) -> search_for_stop.SearchForStopResourceWithRawResponse:
        from .resources.search_for_stop import SearchForStopResourceWithRawResponse

        return SearchForStopResourceWithRawResponse(self._client.search_for_stop)

    @cached_property
    def search_for_route(self) -> search_for_route.SearchForRouteResourceWithRawResponse:
        from .resources.search_for_route import SearchForRouteResourceWithRawResponse

        return SearchForRouteResourceWithRawResponse(self._client.search_for_route)

    @cached_property
    def block(self) -> block.BlockResourceWithRawResponse:
        from .resources.block import BlockResourceWithRawResponse

        return BlockResourceWithRawResponse(self._client.block)

    @cached_property
    def shape(self) -> shape.ShapeResourceWithRawResponse:
        from .resources.shape import ShapeResourceWithRawResponse

        return ShapeResourceWithRawResponse(self._client.shape)


class AsyncOnebusawaySDKWithRawResponse:
    _client: AsyncOnebusawaySDK

    def __init__(self, client: AsyncOnebusawaySDK) -> None:
        self._client = client

    @cached_property
    def agencies_with_coverage(self) -> agencies_with_coverage.AsyncAgenciesWithCoverageResourceWithRawResponse:
        from .resources.agencies_with_coverage import AsyncAgenciesWithCoverageResourceWithRawResponse

        return AsyncAgenciesWithCoverageResourceWithRawResponse(self._client.agencies_with_coverage)

    @cached_property
    def agency(self) -> agency.AsyncAgencyResourceWithRawResponse:
        from .resources.agency import AsyncAgencyResourceWithRawResponse

        return AsyncAgencyResourceWithRawResponse(self._client.agency)

    @cached_property
    def vehicles_for_agency(self) -> vehicles_for_agency.AsyncVehiclesForAgencyResourceWithRawResponse:
        from .resources.vehicles_for_agency import AsyncVehiclesForAgencyResourceWithRawResponse

        return AsyncVehiclesForAgencyResourceWithRawResponse(self._client.vehicles_for_agency)

    @cached_property
    def config(self) -> config.AsyncConfigResourceWithRawResponse:
        from .resources.config import AsyncConfigResourceWithRawResponse

        return AsyncConfigResourceWithRawResponse(self._client.config)

    @cached_property
    def current_time(self) -> current_time.AsyncCurrentTimeResourceWithRawResponse:
        from .resources.current_time import AsyncCurrentTimeResourceWithRawResponse

        return AsyncCurrentTimeResourceWithRawResponse(self._client.current_time)

    @cached_property
    def stops_for_location(self) -> stops_for_location.AsyncStopsForLocationResourceWithRawResponse:
        from .resources.stops_for_location import AsyncStopsForLocationResourceWithRawResponse

        return AsyncStopsForLocationResourceWithRawResponse(self._client.stops_for_location)

    @cached_property
    def stops_for_route(self) -> stops_for_route.AsyncStopsForRouteResourceWithRawResponse:
        from .resources.stops_for_route import AsyncStopsForRouteResourceWithRawResponse

        return AsyncStopsForRouteResourceWithRawResponse(self._client.stops_for_route)

    @cached_property
    def stops_for_agency(self) -> stops_for_agency.AsyncStopsForAgencyResourceWithRawResponse:
        from .resources.stops_for_agency import AsyncStopsForAgencyResourceWithRawResponse

        return AsyncStopsForAgencyResourceWithRawResponse(self._client.stops_for_agency)

    @cached_property
    def stop(self) -> stop.AsyncStopResourceWithRawResponse:
        from .resources.stop import AsyncStopResourceWithRawResponse

        return AsyncStopResourceWithRawResponse(self._client.stop)

    @cached_property
    def stop_ids_for_agency(self) -> stop_ids_for_agency.AsyncStopIDsForAgencyResourceWithRawResponse:
        from .resources.stop_ids_for_agency import AsyncStopIDsForAgencyResourceWithRawResponse

        return AsyncStopIDsForAgencyResourceWithRawResponse(self._client.stop_ids_for_agency)

    @cached_property
    def schedule_for_stop(self) -> schedule_for_stop.AsyncScheduleForStopResourceWithRawResponse:
        from .resources.schedule_for_stop import AsyncScheduleForStopResourceWithRawResponse

        return AsyncScheduleForStopResourceWithRawResponse(self._client.schedule_for_stop)

    @cached_property
    def route(self) -> route.AsyncRouteResourceWithRawResponse:
        from .resources.route import AsyncRouteResourceWithRawResponse

        return AsyncRouteResourceWithRawResponse(self._client.route)

    @cached_property
    def route_ids_for_agency(self) -> route_ids_for_agency.AsyncRouteIDsForAgencyResourceWithRawResponse:
        from .resources.route_ids_for_agency import AsyncRouteIDsForAgencyResourceWithRawResponse

        return AsyncRouteIDsForAgencyResourceWithRawResponse(self._client.route_ids_for_agency)

    @cached_property
    def routes_for_location(self) -> routes_for_location.AsyncRoutesForLocationResourceWithRawResponse:
        from .resources.routes_for_location import AsyncRoutesForLocationResourceWithRawResponse

        return AsyncRoutesForLocationResourceWithRawResponse(self._client.routes_for_location)

    @cached_property
    def routes_for_agency(self) -> routes_for_agency.AsyncRoutesForAgencyResourceWithRawResponse:
        from .resources.routes_for_agency import AsyncRoutesForAgencyResourceWithRawResponse

        return AsyncRoutesForAgencyResourceWithRawResponse(self._client.routes_for_agency)

    @cached_property
    def schedule_for_route(self) -> schedule_for_route.AsyncScheduleForRouteResourceWithRawResponse:
        from .resources.schedule_for_route import AsyncScheduleForRouteResourceWithRawResponse

        return AsyncScheduleForRouteResourceWithRawResponse(self._client.schedule_for_route)

    @cached_property
    def arrival_and_departure(self) -> arrival_and_departure.AsyncArrivalAndDepartureResourceWithRawResponse:
        from .resources.arrival_and_departure import AsyncArrivalAndDepartureResourceWithRawResponse

        return AsyncArrivalAndDepartureResourceWithRawResponse(self._client.arrival_and_departure)

    @cached_property
    def trip(self) -> trip.AsyncTripResourceWithRawResponse:
        from .resources.trip import AsyncTripResourceWithRawResponse

        return AsyncTripResourceWithRawResponse(self._client.trip)

    @cached_property
    def trips_for_location(self) -> trips_for_location.AsyncTripsForLocationResourceWithRawResponse:
        from .resources.trips_for_location import AsyncTripsForLocationResourceWithRawResponse

        return AsyncTripsForLocationResourceWithRawResponse(self._client.trips_for_location)

    @cached_property
    def trip_details(self) -> trip_details.AsyncTripDetailsResourceWithRawResponse:
        from .resources.trip_details import AsyncTripDetailsResourceWithRawResponse

        return AsyncTripDetailsResourceWithRawResponse(self._client.trip_details)

    @cached_property
    def trip_for_vehicle(self) -> trip_for_vehicle.AsyncTripForVehicleResourceWithRawResponse:
        from .resources.trip_for_vehicle import AsyncTripForVehicleResourceWithRawResponse

        return AsyncTripForVehicleResourceWithRawResponse(self._client.trip_for_vehicle)

    @cached_property
    def trips_for_route(self) -> trips_for_route.AsyncTripsForRouteResourceWithRawResponse:
        from .resources.trips_for_route import AsyncTripsForRouteResourceWithRawResponse

        return AsyncTripsForRouteResourceWithRawResponse(self._client.trips_for_route)

    @cached_property
    def report_problem_with_stop(self) -> report_problem_with_stop.AsyncReportProblemWithStopResourceWithRawResponse:
        from .resources.report_problem_with_stop import AsyncReportProblemWithStopResourceWithRawResponse

        return AsyncReportProblemWithStopResourceWithRawResponse(self._client.report_problem_with_stop)

    @cached_property
    def report_problem_with_trip(self) -> report_problem_with_trip.AsyncReportProblemWithTripResourceWithRawResponse:
        from .resources.report_problem_with_trip import AsyncReportProblemWithTripResourceWithRawResponse

        return AsyncReportProblemWithTripResourceWithRawResponse(self._client.report_problem_with_trip)

    @cached_property
    def search_for_stop(self) -> search_for_stop.AsyncSearchForStopResourceWithRawResponse:
        from .resources.search_for_stop import AsyncSearchForStopResourceWithRawResponse

        return AsyncSearchForStopResourceWithRawResponse(self._client.search_for_stop)

    @cached_property
    def search_for_route(self) -> search_for_route.AsyncSearchForRouteResourceWithRawResponse:
        from .resources.search_for_route import AsyncSearchForRouteResourceWithRawResponse

        return AsyncSearchForRouteResourceWithRawResponse(self._client.search_for_route)

    @cached_property
    def block(self) -> block.AsyncBlockResourceWithRawResponse:
        from .resources.block import AsyncBlockResourceWithRawResponse

        return AsyncBlockResourceWithRawResponse(self._client.block)

    @cached_property
    def shape(self) -> shape.AsyncShapeResourceWithRawResponse:
        from .resources.shape import AsyncShapeResourceWithRawResponse

        return AsyncShapeResourceWithRawResponse(self._client.shape)


class OnebusawaySDKWithStreamedResponse:
    _client: OnebusawaySDK

    def __init__(self, client: OnebusawaySDK) -> None:
        self._client = client

    @cached_property
    def agencies_with_coverage(self) -> agencies_with_coverage.AgenciesWithCoverageResourceWithStreamingResponse:
        from .resources.agencies_with_coverage import AgenciesWithCoverageResourceWithStreamingResponse

        return AgenciesWithCoverageResourceWithStreamingResponse(self._client.agencies_with_coverage)

    @cached_property
    def agency(self) -> agency.AgencyResourceWithStreamingResponse:
        from .resources.agency import AgencyResourceWithStreamingResponse

        return AgencyResourceWithStreamingResponse(self._client.agency)

    @cached_property
    def vehicles_for_agency(self) -> vehicles_for_agency.VehiclesForAgencyResourceWithStreamingResponse:
        from .resources.vehicles_for_agency import VehiclesForAgencyResourceWithStreamingResponse

        return VehiclesForAgencyResourceWithStreamingResponse(self._client.vehicles_for_agency)

    @cached_property
    def config(self) -> config.ConfigResourceWithStreamingResponse:
        from .resources.config import ConfigResourceWithStreamingResponse

        return ConfigResourceWithStreamingResponse(self._client.config)

    @cached_property
    def current_time(self) -> current_time.CurrentTimeResourceWithStreamingResponse:
        from .resources.current_time import CurrentTimeResourceWithStreamingResponse

        return CurrentTimeResourceWithStreamingResponse(self._client.current_time)

    @cached_property
    def stops_for_location(self) -> stops_for_location.StopsForLocationResourceWithStreamingResponse:
        from .resources.stops_for_location import StopsForLocationResourceWithStreamingResponse

        return StopsForLocationResourceWithStreamingResponse(self._client.stops_for_location)

    @cached_property
    def stops_for_route(self) -> stops_for_route.StopsForRouteResourceWithStreamingResponse:
        from .resources.stops_for_route import StopsForRouteResourceWithStreamingResponse

        return StopsForRouteResourceWithStreamingResponse(self._client.stops_for_route)

    @cached_property
    def stops_for_agency(self) -> stops_for_agency.StopsForAgencyResourceWithStreamingResponse:
        from .resources.stops_for_agency import StopsForAgencyResourceWithStreamingResponse

        return StopsForAgencyResourceWithStreamingResponse(self._client.stops_for_agency)

    @cached_property
    def stop(self) -> stop.StopResourceWithStreamingResponse:
        from .resources.stop import StopResourceWithStreamingResponse

        return StopResourceWithStreamingResponse(self._client.stop)

    @cached_property
    def stop_ids_for_agency(self) -> stop_ids_for_agency.StopIDsForAgencyResourceWithStreamingResponse:
        from .resources.stop_ids_for_agency import StopIDsForAgencyResourceWithStreamingResponse

        return StopIDsForAgencyResourceWithStreamingResponse(self._client.stop_ids_for_agency)

    @cached_property
    def schedule_for_stop(self) -> schedule_for_stop.ScheduleForStopResourceWithStreamingResponse:
        from .resources.schedule_for_stop import ScheduleForStopResourceWithStreamingResponse

        return ScheduleForStopResourceWithStreamingResponse(self._client.schedule_for_stop)

    @cached_property
    def route(self) -> route.RouteResourceWithStreamingResponse:
        from .resources.route import RouteResourceWithStreamingResponse

        return RouteResourceWithStreamingResponse(self._client.route)

    @cached_property
    def route_ids_for_agency(self) -> route_ids_for_agency.RouteIDsForAgencyResourceWithStreamingResponse:
        from .resources.route_ids_for_agency import RouteIDsForAgencyResourceWithStreamingResponse

        return RouteIDsForAgencyResourceWithStreamingResponse(self._client.route_ids_for_agency)

    @cached_property
    def routes_for_location(self) -> routes_for_location.RoutesForLocationResourceWithStreamingResponse:
        from .resources.routes_for_location import RoutesForLocationResourceWithStreamingResponse

        return RoutesForLocationResourceWithStreamingResponse(self._client.routes_for_location)

    @cached_property
    def routes_for_agency(self) -> routes_for_agency.RoutesForAgencyResourceWithStreamingResponse:
        from .resources.routes_for_agency import RoutesForAgencyResourceWithStreamingResponse

        return RoutesForAgencyResourceWithStreamingResponse(self._client.routes_for_agency)

    @cached_property
    def schedule_for_route(self) -> schedule_for_route.ScheduleForRouteResourceWithStreamingResponse:
        from .resources.schedule_for_route import ScheduleForRouteResourceWithStreamingResponse

        return ScheduleForRouteResourceWithStreamingResponse(self._client.schedule_for_route)

    @cached_property
    def arrival_and_departure(self) -> arrival_and_departure.ArrivalAndDepartureResourceWithStreamingResponse:
        from .resources.arrival_and_departure import ArrivalAndDepartureResourceWithStreamingResponse

        return ArrivalAndDepartureResourceWithStreamingResponse(self._client.arrival_and_departure)

    @cached_property
    def trip(self) -> trip.TripResourceWithStreamingResponse:
        from .resources.trip import TripResourceWithStreamingResponse

        return TripResourceWithStreamingResponse(self._client.trip)

    @cached_property
    def trips_for_location(self) -> trips_for_location.TripsForLocationResourceWithStreamingResponse:
        from .resources.trips_for_location import TripsForLocationResourceWithStreamingResponse

        return TripsForLocationResourceWithStreamingResponse(self._client.trips_for_location)

    @cached_property
    def trip_details(self) -> trip_details.TripDetailsResourceWithStreamingResponse:
        from .resources.trip_details import TripDetailsResourceWithStreamingResponse

        return TripDetailsResourceWithStreamingResponse(self._client.trip_details)

    @cached_property
    def trip_for_vehicle(self) -> trip_for_vehicle.TripForVehicleResourceWithStreamingResponse:
        from .resources.trip_for_vehicle import TripForVehicleResourceWithStreamingResponse

        return TripForVehicleResourceWithStreamingResponse(self._client.trip_for_vehicle)

    @cached_property
    def trips_for_route(self) -> trips_for_route.TripsForRouteResourceWithStreamingResponse:
        from .resources.trips_for_route import TripsForRouteResourceWithStreamingResponse

        return TripsForRouteResourceWithStreamingResponse(self._client.trips_for_route)

    @cached_property
    def report_problem_with_stop(self) -> report_problem_with_stop.ReportProblemWithStopResourceWithStreamingResponse:
        from .resources.report_problem_with_stop import ReportProblemWithStopResourceWithStreamingResponse

        return ReportProblemWithStopResourceWithStreamingResponse(self._client.report_problem_with_stop)

    @cached_property
    def report_problem_with_trip(self) -> report_problem_with_trip.ReportProblemWithTripResourceWithStreamingResponse:
        from .resources.report_problem_with_trip import ReportProblemWithTripResourceWithStreamingResponse

        return ReportProblemWithTripResourceWithStreamingResponse(self._client.report_problem_with_trip)

    @cached_property
    def search_for_stop(self) -> search_for_stop.SearchForStopResourceWithStreamingResponse:
        from .resources.search_for_stop import SearchForStopResourceWithStreamingResponse

        return SearchForStopResourceWithStreamingResponse(self._client.search_for_stop)

    @cached_property
    def search_for_route(self) -> search_for_route.SearchForRouteResourceWithStreamingResponse:
        from .resources.search_for_route import SearchForRouteResourceWithStreamingResponse

        return SearchForRouteResourceWithStreamingResponse(self._client.search_for_route)

    @cached_property
    def block(self) -> block.BlockResourceWithStreamingResponse:
        from .resources.block import BlockResourceWithStreamingResponse

        return BlockResourceWithStreamingResponse(self._client.block)

    @cached_property
    def shape(self) -> shape.ShapeResourceWithStreamingResponse:
        from .resources.shape import ShapeResourceWithStreamingResponse

        return ShapeResourceWithStreamingResponse(self._client.shape)


class AsyncOnebusawaySDKWithStreamedResponse:
    _client: AsyncOnebusawaySDK

    def __init__(self, client: AsyncOnebusawaySDK) -> None:
        self._client = client

    @cached_property
    def agencies_with_coverage(self) -> agencies_with_coverage.AsyncAgenciesWithCoverageResourceWithStreamingResponse:
        from .resources.agencies_with_coverage import AsyncAgenciesWithCoverageResourceWithStreamingResponse

        return AsyncAgenciesWithCoverageResourceWithStreamingResponse(self._client.agencies_with_coverage)

    @cached_property
    def agency(self) -> agency.AsyncAgencyResourceWithStreamingResponse:
        from .resources.agency import AsyncAgencyResourceWithStreamingResponse

        return AsyncAgencyResourceWithStreamingResponse(self._client.agency)

    @cached_property
    def vehicles_for_agency(self) -> vehicles_for_agency.AsyncVehiclesForAgencyResourceWithStreamingResponse:
        from .resources.vehicles_for_agency import AsyncVehiclesForAgencyResourceWithStreamingResponse

        return AsyncVehiclesForAgencyResourceWithStreamingResponse(self._client.vehicles_for_agency)

    @cached_property
    def config(self) -> config.AsyncConfigResourceWithStreamingResponse:
        from .resources.config import AsyncConfigResourceWithStreamingResponse

        return AsyncConfigResourceWithStreamingResponse(self._client.config)

    @cached_property
    def current_time(self) -> current_time.AsyncCurrentTimeResourceWithStreamingResponse:
        from .resources.current_time import AsyncCurrentTimeResourceWithStreamingResponse

        return AsyncCurrentTimeResourceWithStreamingResponse(self._client.current_time)

    @cached_property
    def stops_for_location(self) -> stops_for_location.AsyncStopsForLocationResourceWithStreamingResponse:
        from .resources.stops_for_location import AsyncStopsForLocationResourceWithStreamingResponse

        return AsyncStopsForLocationResourceWithStreamingResponse(self._client.stops_for_location)

    @cached_property
    def stops_for_route(self) -> stops_for_route.AsyncStopsForRouteResourceWithStreamingResponse:
        from .resources.stops_for_route import AsyncStopsForRouteResourceWithStreamingResponse

        return AsyncStopsForRouteResourceWithStreamingResponse(self._client.stops_for_route)

    @cached_property
    def stops_for_agency(self) -> stops_for_agency.AsyncStopsForAgencyResourceWithStreamingResponse:
        from .resources.stops_for_agency import AsyncStopsForAgencyResourceWithStreamingResponse

        return AsyncStopsForAgencyResourceWithStreamingResponse(self._client.stops_for_agency)

    @cached_property
    def stop(self) -> stop.AsyncStopResourceWithStreamingResponse:
        from .resources.stop import AsyncStopResourceWithStreamingResponse

        return AsyncStopResourceWithStreamingResponse(self._client.stop)

    @cached_property
    def stop_ids_for_agency(self) -> stop_ids_for_agency.AsyncStopIDsForAgencyResourceWithStreamingResponse:
        from .resources.stop_ids_for_agency import AsyncStopIDsForAgencyResourceWithStreamingResponse

        return AsyncStopIDsForAgencyResourceWithStreamingResponse(self._client.stop_ids_for_agency)

    @cached_property
    def schedule_for_stop(self) -> schedule_for_stop.AsyncScheduleForStopResourceWithStreamingResponse:
        from .resources.schedule_for_stop import AsyncScheduleForStopResourceWithStreamingResponse

        return AsyncScheduleForStopResourceWithStreamingResponse(self._client.schedule_for_stop)

    @cached_property
    def route(self) -> route.AsyncRouteResourceWithStreamingResponse:
        from .resources.route import AsyncRouteResourceWithStreamingResponse

        return AsyncRouteResourceWithStreamingResponse(self._client.route)

    @cached_property
    def route_ids_for_agency(self) -> route_ids_for_agency.AsyncRouteIDsForAgencyResourceWithStreamingResponse:
        from .resources.route_ids_for_agency import AsyncRouteIDsForAgencyResourceWithStreamingResponse

        return AsyncRouteIDsForAgencyResourceWithStreamingResponse(self._client.route_ids_for_agency)

    @cached_property
    def routes_for_location(self) -> routes_for_location.AsyncRoutesForLocationResourceWithStreamingResponse:
        from .resources.routes_for_location import AsyncRoutesForLocationResourceWithStreamingResponse

        return AsyncRoutesForLocationResourceWithStreamingResponse(self._client.routes_for_location)

    @cached_property
    def routes_for_agency(self) -> routes_for_agency.AsyncRoutesForAgencyResourceWithStreamingResponse:
        from .resources.routes_for_agency import AsyncRoutesForAgencyResourceWithStreamingResponse

        return AsyncRoutesForAgencyResourceWithStreamingResponse(self._client.routes_for_agency)

    @cached_property
    def schedule_for_route(self) -> schedule_for_route.AsyncScheduleForRouteResourceWithStreamingResponse:
        from .resources.schedule_for_route import AsyncScheduleForRouteResourceWithStreamingResponse

        return AsyncScheduleForRouteResourceWithStreamingResponse(self._client.schedule_for_route)

    @cached_property
    def arrival_and_departure(self) -> arrival_and_departure.AsyncArrivalAndDepartureResourceWithStreamingResponse:
        from .resources.arrival_and_departure import AsyncArrivalAndDepartureResourceWithStreamingResponse

        return AsyncArrivalAndDepartureResourceWithStreamingResponse(self._client.arrival_and_departure)

    @cached_property
    def trip(self) -> trip.AsyncTripResourceWithStreamingResponse:
        from .resources.trip import AsyncTripResourceWithStreamingResponse

        return AsyncTripResourceWithStreamingResponse(self._client.trip)

    @cached_property
    def trips_for_location(self) -> trips_for_location.AsyncTripsForLocationResourceWithStreamingResponse:
        from .resources.trips_for_location import AsyncTripsForLocationResourceWithStreamingResponse

        return AsyncTripsForLocationResourceWithStreamingResponse(self._client.trips_for_location)

    @cached_property
    def trip_details(self) -> trip_details.AsyncTripDetailsResourceWithStreamingResponse:
        from .resources.trip_details import AsyncTripDetailsResourceWithStreamingResponse

        return AsyncTripDetailsResourceWithStreamingResponse(self._client.trip_details)

    @cached_property
    def trip_for_vehicle(self) -> trip_for_vehicle.AsyncTripForVehicleResourceWithStreamingResponse:
        from .resources.trip_for_vehicle import AsyncTripForVehicleResourceWithStreamingResponse

        return AsyncTripForVehicleResourceWithStreamingResponse(self._client.trip_for_vehicle)

    @cached_property
    def trips_for_route(self) -> trips_for_route.AsyncTripsForRouteResourceWithStreamingResponse:
        from .resources.trips_for_route import AsyncTripsForRouteResourceWithStreamingResponse

        return AsyncTripsForRouteResourceWithStreamingResponse(self._client.trips_for_route)

    @cached_property
    def report_problem_with_stop(
        self,
    ) -> report_problem_with_stop.AsyncReportProblemWithStopResourceWithStreamingResponse:
        from .resources.report_problem_with_stop import AsyncReportProblemWithStopResourceWithStreamingResponse

        return AsyncReportProblemWithStopResourceWithStreamingResponse(self._client.report_problem_with_stop)

    @cached_property
    def report_problem_with_trip(
        self,
    ) -> report_problem_with_trip.AsyncReportProblemWithTripResourceWithStreamingResponse:
        from .resources.report_problem_with_trip import AsyncReportProblemWithTripResourceWithStreamingResponse

        return AsyncReportProblemWithTripResourceWithStreamingResponse(self._client.report_problem_with_trip)

    @cached_property
    def search_for_stop(self) -> search_for_stop.AsyncSearchForStopResourceWithStreamingResponse:
        from .resources.search_for_stop import AsyncSearchForStopResourceWithStreamingResponse

        return AsyncSearchForStopResourceWithStreamingResponse(self._client.search_for_stop)

    @cached_property
    def search_for_route(self) -> search_for_route.AsyncSearchForRouteResourceWithStreamingResponse:
        from .resources.search_for_route import AsyncSearchForRouteResourceWithStreamingResponse

        return AsyncSearchForRouteResourceWithStreamingResponse(self._client.search_for_route)

    @cached_property
    def block(self) -> block.AsyncBlockResourceWithStreamingResponse:
        from .resources.block import AsyncBlockResourceWithStreamingResponse

        return AsyncBlockResourceWithStreamingResponse(self._client.block)

    @cached_property
    def shape(self) -> shape.AsyncShapeResourceWithStreamingResponse:
        from .resources.shape import AsyncShapeResourceWithStreamingResponse

        return AsyncShapeResourceWithStreamingResponse(self._client.shape)


Client = OnebusawaySDK

AsyncClient = AsyncOnebusawaySDK
