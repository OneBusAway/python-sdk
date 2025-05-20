# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, Union, Mapping
from typing_extensions import Self, override

import httpx

from . import _exceptions
from ._qs import Querystring
from ._types import (
    NOT_GIVEN,
    Omit,
    Timeout,
    NotGiven,
    Transport,
    ProxiesTypes,
    RequestOptions,
)
from ._utils import is_given, get_async_library
from ._version import __version__
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
from ._streaming import Stream as Stream, AsyncStream as AsyncStream
from ._exceptions import APIStatusError, OnebusawaySDKError
from ._base_client import (
    DEFAULT_MAX_RETRIES,
    SyncAPIClient,
    AsyncAPIClient,
)

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
    agencies_with_coverage: agencies_with_coverage.AgenciesWithCoverageResource
    agency: agency.AgencyResource
    vehicles_for_agency: vehicles_for_agency.VehiclesForAgencyResource
    config: config.ConfigResource
    current_time: current_time.CurrentTimeResource
    stops_for_location: stops_for_location.StopsForLocationResource
    stops_for_route: stops_for_route.StopsForRouteResource
    stops_for_agency: stops_for_agency.StopsForAgencyResource
    stop: stop.StopResource
    stop_ids_for_agency: stop_ids_for_agency.StopIDsForAgencyResource
    schedule_for_stop: schedule_for_stop.ScheduleForStopResource
    route: route.RouteResource
    route_ids_for_agency: route_ids_for_agency.RouteIDsForAgencyResource
    routes_for_location: routes_for_location.RoutesForLocationResource
    routes_for_agency: routes_for_agency.RoutesForAgencyResource
    schedule_for_route: schedule_for_route.ScheduleForRouteResource
    arrival_and_departure: arrival_and_departure.ArrivalAndDepartureResource
    trip: trip.TripResource
    trips_for_location: trips_for_location.TripsForLocationResource
    trip_details: trip_details.TripDetailsResource
    trip_for_vehicle: trip_for_vehicle.TripForVehicleResource
    trips_for_route: trips_for_route.TripsForRouteResource
    report_problem_with_stop: report_problem_with_stop.ReportProblemWithStopResource
    report_problem_with_trip: report_problem_with_trip.ReportProblemWithTripResource
    search_for_stop: search_for_stop.SearchForStopResource
    search_for_route: search_for_route.SearchForRouteResource
    block: block.BlockResource
    shape: shape.ShapeResource
    with_raw_response: OnebusawaySDKWithRawResponse
    with_streaming_response: OnebusawaySDKWithStreamedResponse

    # client options
    api_key: str

    def __init__(
        self,
        *,
        api_key: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
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

        self.agencies_with_coverage = agencies_with_coverage.AgenciesWithCoverageResource(self)
        self.agency = agency.AgencyResource(self)
        self.vehicles_for_agency = vehicles_for_agency.VehiclesForAgencyResource(self)
        self.config = config.ConfigResource(self)
        self.current_time = current_time.CurrentTimeResource(self)
        self.stops_for_location = stops_for_location.StopsForLocationResource(self)
        self.stops_for_route = stops_for_route.StopsForRouteResource(self)
        self.stops_for_agency = stops_for_agency.StopsForAgencyResource(self)
        self.stop = stop.StopResource(self)
        self.stop_ids_for_agency = stop_ids_for_agency.StopIDsForAgencyResource(self)
        self.schedule_for_stop = schedule_for_stop.ScheduleForStopResource(self)
        self.route = route.RouteResource(self)
        self.route_ids_for_agency = route_ids_for_agency.RouteIDsForAgencyResource(self)
        self.routes_for_location = routes_for_location.RoutesForLocationResource(self)
        self.routes_for_agency = routes_for_agency.RoutesForAgencyResource(self)
        self.schedule_for_route = schedule_for_route.ScheduleForRouteResource(self)
        self.arrival_and_departure = arrival_and_departure.ArrivalAndDepartureResource(self)
        self.trip = trip.TripResource(self)
        self.trips_for_location = trips_for_location.TripsForLocationResource(self)
        self.trip_details = trip_details.TripDetailsResource(self)
        self.trip_for_vehicle = trip_for_vehicle.TripForVehicleResource(self)
        self.trips_for_route = trips_for_route.TripsForRouteResource(self)
        self.report_problem_with_stop = report_problem_with_stop.ReportProblemWithStopResource(self)
        self.report_problem_with_trip = report_problem_with_trip.ReportProblemWithTripResource(self)
        self.search_for_stop = search_for_stop.SearchForStopResource(self)
        self.search_for_route = search_for_route.SearchForRouteResource(self)
        self.block = block.BlockResource(self)
        self.shape = shape.ShapeResource(self)
        self.with_raw_response = OnebusawaySDKWithRawResponse(self)
        self.with_streaming_response = OnebusawaySDKWithStreamedResponse(self)

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
        timeout: float | Timeout | None | NotGiven = NOT_GIVEN,
        http_client: httpx.Client | None = None,
        max_retries: int | NotGiven = NOT_GIVEN,
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
    agencies_with_coverage: agencies_with_coverage.AsyncAgenciesWithCoverageResource
    agency: agency.AsyncAgencyResource
    vehicles_for_agency: vehicles_for_agency.AsyncVehiclesForAgencyResource
    config: config.AsyncConfigResource
    current_time: current_time.AsyncCurrentTimeResource
    stops_for_location: stops_for_location.AsyncStopsForLocationResource
    stops_for_route: stops_for_route.AsyncStopsForRouteResource
    stops_for_agency: stops_for_agency.AsyncStopsForAgencyResource
    stop: stop.AsyncStopResource
    stop_ids_for_agency: stop_ids_for_agency.AsyncStopIDsForAgencyResource
    schedule_for_stop: schedule_for_stop.AsyncScheduleForStopResource
    route: route.AsyncRouteResource
    route_ids_for_agency: route_ids_for_agency.AsyncRouteIDsForAgencyResource
    routes_for_location: routes_for_location.AsyncRoutesForLocationResource
    routes_for_agency: routes_for_agency.AsyncRoutesForAgencyResource
    schedule_for_route: schedule_for_route.AsyncScheduleForRouteResource
    arrival_and_departure: arrival_and_departure.AsyncArrivalAndDepartureResource
    trip: trip.AsyncTripResource
    trips_for_location: trips_for_location.AsyncTripsForLocationResource
    trip_details: trip_details.AsyncTripDetailsResource
    trip_for_vehicle: trip_for_vehicle.AsyncTripForVehicleResource
    trips_for_route: trips_for_route.AsyncTripsForRouteResource
    report_problem_with_stop: report_problem_with_stop.AsyncReportProblemWithStopResource
    report_problem_with_trip: report_problem_with_trip.AsyncReportProblemWithTripResource
    search_for_stop: search_for_stop.AsyncSearchForStopResource
    search_for_route: search_for_route.AsyncSearchForRouteResource
    block: block.AsyncBlockResource
    shape: shape.AsyncShapeResource
    with_raw_response: AsyncOnebusawaySDKWithRawResponse
    with_streaming_response: AsyncOnebusawaySDKWithStreamedResponse

    # client options
    api_key: str

    def __init__(
        self,
        *,
        api_key: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
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

        self.agencies_with_coverage = agencies_with_coverage.AsyncAgenciesWithCoverageResource(self)
        self.agency = agency.AsyncAgencyResource(self)
        self.vehicles_for_agency = vehicles_for_agency.AsyncVehiclesForAgencyResource(self)
        self.config = config.AsyncConfigResource(self)
        self.current_time = current_time.AsyncCurrentTimeResource(self)
        self.stops_for_location = stops_for_location.AsyncStopsForLocationResource(self)
        self.stops_for_route = stops_for_route.AsyncStopsForRouteResource(self)
        self.stops_for_agency = stops_for_agency.AsyncStopsForAgencyResource(self)
        self.stop = stop.AsyncStopResource(self)
        self.stop_ids_for_agency = stop_ids_for_agency.AsyncStopIDsForAgencyResource(self)
        self.schedule_for_stop = schedule_for_stop.AsyncScheduleForStopResource(self)
        self.route = route.AsyncRouteResource(self)
        self.route_ids_for_agency = route_ids_for_agency.AsyncRouteIDsForAgencyResource(self)
        self.routes_for_location = routes_for_location.AsyncRoutesForLocationResource(self)
        self.routes_for_agency = routes_for_agency.AsyncRoutesForAgencyResource(self)
        self.schedule_for_route = schedule_for_route.AsyncScheduleForRouteResource(self)
        self.arrival_and_departure = arrival_and_departure.AsyncArrivalAndDepartureResource(self)
        self.trip = trip.AsyncTripResource(self)
        self.trips_for_location = trips_for_location.AsyncTripsForLocationResource(self)
        self.trip_details = trip_details.AsyncTripDetailsResource(self)
        self.trip_for_vehicle = trip_for_vehicle.AsyncTripForVehicleResource(self)
        self.trips_for_route = trips_for_route.AsyncTripsForRouteResource(self)
        self.report_problem_with_stop = report_problem_with_stop.AsyncReportProblemWithStopResource(self)
        self.report_problem_with_trip = report_problem_with_trip.AsyncReportProblemWithTripResource(self)
        self.search_for_stop = search_for_stop.AsyncSearchForStopResource(self)
        self.search_for_route = search_for_route.AsyncSearchForRouteResource(self)
        self.block = block.AsyncBlockResource(self)
        self.shape = shape.AsyncShapeResource(self)
        self.with_raw_response = AsyncOnebusawaySDKWithRawResponse(self)
        self.with_streaming_response = AsyncOnebusawaySDKWithStreamedResponse(self)

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
        timeout: float | Timeout | None | NotGiven = NOT_GIVEN,
        http_client: httpx.AsyncClient | None = None,
        max_retries: int | NotGiven = NOT_GIVEN,
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
    def __init__(self, client: OnebusawaySDK) -> None:
        self.agencies_with_coverage = agencies_with_coverage.AgenciesWithCoverageResourceWithRawResponse(
            client.agencies_with_coverage
        )
        self.agency = agency.AgencyResourceWithRawResponse(client.agency)
        self.vehicles_for_agency = vehicles_for_agency.VehiclesForAgencyResourceWithRawResponse(
            client.vehicles_for_agency
        )
        self.config = config.ConfigResourceWithRawResponse(client.config)
        self.current_time = current_time.CurrentTimeResourceWithRawResponse(client.current_time)
        self.stops_for_location = stops_for_location.StopsForLocationResourceWithRawResponse(client.stops_for_location)
        self.stops_for_route = stops_for_route.StopsForRouteResourceWithRawResponse(client.stops_for_route)
        self.stops_for_agency = stops_for_agency.StopsForAgencyResourceWithRawResponse(client.stops_for_agency)
        self.stop = stop.StopResourceWithRawResponse(client.stop)
        self.stop_ids_for_agency = stop_ids_for_agency.StopIDsForAgencyResourceWithRawResponse(
            client.stop_ids_for_agency
        )
        self.schedule_for_stop = schedule_for_stop.ScheduleForStopResourceWithRawResponse(client.schedule_for_stop)
        self.route = route.RouteResourceWithRawResponse(client.route)
        self.route_ids_for_agency = route_ids_for_agency.RouteIDsForAgencyResourceWithRawResponse(
            client.route_ids_for_agency
        )
        self.routes_for_location = routes_for_location.RoutesForLocationResourceWithRawResponse(
            client.routes_for_location
        )
        self.routes_for_agency = routes_for_agency.RoutesForAgencyResourceWithRawResponse(client.routes_for_agency)
        self.schedule_for_route = schedule_for_route.ScheduleForRouteResourceWithRawResponse(client.schedule_for_route)
        self.arrival_and_departure = arrival_and_departure.ArrivalAndDepartureResourceWithRawResponse(
            client.arrival_and_departure
        )
        self.trip = trip.TripResourceWithRawResponse(client.trip)
        self.trips_for_location = trips_for_location.TripsForLocationResourceWithRawResponse(client.trips_for_location)
        self.trip_details = trip_details.TripDetailsResourceWithRawResponse(client.trip_details)
        self.trip_for_vehicle = trip_for_vehicle.TripForVehicleResourceWithRawResponse(client.trip_for_vehicle)
        self.trips_for_route = trips_for_route.TripsForRouteResourceWithRawResponse(client.trips_for_route)
        self.report_problem_with_stop = report_problem_with_stop.ReportProblemWithStopResourceWithRawResponse(
            client.report_problem_with_stop
        )
        self.report_problem_with_trip = report_problem_with_trip.ReportProblemWithTripResourceWithRawResponse(
            client.report_problem_with_trip
        )
        self.search_for_stop = search_for_stop.SearchForStopResourceWithRawResponse(client.search_for_stop)
        self.search_for_route = search_for_route.SearchForRouteResourceWithRawResponse(client.search_for_route)
        self.block = block.BlockResourceWithRawResponse(client.block)
        self.shape = shape.ShapeResourceWithRawResponse(client.shape)


class AsyncOnebusawaySDKWithRawResponse:
    def __init__(self, client: AsyncOnebusawaySDK) -> None:
        self.agencies_with_coverage = agencies_with_coverage.AsyncAgenciesWithCoverageResourceWithRawResponse(
            client.agencies_with_coverage
        )
        self.agency = agency.AsyncAgencyResourceWithRawResponse(client.agency)
        self.vehicles_for_agency = vehicles_for_agency.AsyncVehiclesForAgencyResourceWithRawResponse(
            client.vehicles_for_agency
        )
        self.config = config.AsyncConfigResourceWithRawResponse(client.config)
        self.current_time = current_time.AsyncCurrentTimeResourceWithRawResponse(client.current_time)
        self.stops_for_location = stops_for_location.AsyncStopsForLocationResourceWithRawResponse(
            client.stops_for_location
        )
        self.stops_for_route = stops_for_route.AsyncStopsForRouteResourceWithRawResponse(client.stops_for_route)
        self.stops_for_agency = stops_for_agency.AsyncStopsForAgencyResourceWithRawResponse(client.stops_for_agency)
        self.stop = stop.AsyncStopResourceWithRawResponse(client.stop)
        self.stop_ids_for_agency = stop_ids_for_agency.AsyncStopIDsForAgencyResourceWithRawResponse(
            client.stop_ids_for_agency
        )
        self.schedule_for_stop = schedule_for_stop.AsyncScheduleForStopResourceWithRawResponse(client.schedule_for_stop)
        self.route = route.AsyncRouteResourceWithRawResponse(client.route)
        self.route_ids_for_agency = route_ids_for_agency.AsyncRouteIDsForAgencyResourceWithRawResponse(
            client.route_ids_for_agency
        )
        self.routes_for_location = routes_for_location.AsyncRoutesForLocationResourceWithRawResponse(
            client.routes_for_location
        )
        self.routes_for_agency = routes_for_agency.AsyncRoutesForAgencyResourceWithRawResponse(client.routes_for_agency)
        self.schedule_for_route = schedule_for_route.AsyncScheduleForRouteResourceWithRawResponse(
            client.schedule_for_route
        )
        self.arrival_and_departure = arrival_and_departure.AsyncArrivalAndDepartureResourceWithRawResponse(
            client.arrival_and_departure
        )
        self.trip = trip.AsyncTripResourceWithRawResponse(client.trip)
        self.trips_for_location = trips_for_location.AsyncTripsForLocationResourceWithRawResponse(
            client.trips_for_location
        )
        self.trip_details = trip_details.AsyncTripDetailsResourceWithRawResponse(client.trip_details)
        self.trip_for_vehicle = trip_for_vehicle.AsyncTripForVehicleResourceWithRawResponse(client.trip_for_vehicle)
        self.trips_for_route = trips_for_route.AsyncTripsForRouteResourceWithRawResponse(client.trips_for_route)
        self.report_problem_with_stop = report_problem_with_stop.AsyncReportProblemWithStopResourceWithRawResponse(
            client.report_problem_with_stop
        )
        self.report_problem_with_trip = report_problem_with_trip.AsyncReportProblemWithTripResourceWithRawResponse(
            client.report_problem_with_trip
        )
        self.search_for_stop = search_for_stop.AsyncSearchForStopResourceWithRawResponse(client.search_for_stop)
        self.search_for_route = search_for_route.AsyncSearchForRouteResourceWithRawResponse(client.search_for_route)
        self.block = block.AsyncBlockResourceWithRawResponse(client.block)
        self.shape = shape.AsyncShapeResourceWithRawResponse(client.shape)


class OnebusawaySDKWithStreamedResponse:
    def __init__(self, client: OnebusawaySDK) -> None:
        self.agencies_with_coverage = agencies_with_coverage.AgenciesWithCoverageResourceWithStreamingResponse(
            client.agencies_with_coverage
        )
        self.agency = agency.AgencyResourceWithStreamingResponse(client.agency)
        self.vehicles_for_agency = vehicles_for_agency.VehiclesForAgencyResourceWithStreamingResponse(
            client.vehicles_for_agency
        )
        self.config = config.ConfigResourceWithStreamingResponse(client.config)
        self.current_time = current_time.CurrentTimeResourceWithStreamingResponse(client.current_time)
        self.stops_for_location = stops_for_location.StopsForLocationResourceWithStreamingResponse(
            client.stops_for_location
        )
        self.stops_for_route = stops_for_route.StopsForRouteResourceWithStreamingResponse(client.stops_for_route)
        self.stops_for_agency = stops_for_agency.StopsForAgencyResourceWithStreamingResponse(client.stops_for_agency)
        self.stop = stop.StopResourceWithStreamingResponse(client.stop)
        self.stop_ids_for_agency = stop_ids_for_agency.StopIDsForAgencyResourceWithStreamingResponse(
            client.stop_ids_for_agency
        )
        self.schedule_for_stop = schedule_for_stop.ScheduleForStopResourceWithStreamingResponse(
            client.schedule_for_stop
        )
        self.route = route.RouteResourceWithStreamingResponse(client.route)
        self.route_ids_for_agency = route_ids_for_agency.RouteIDsForAgencyResourceWithStreamingResponse(
            client.route_ids_for_agency
        )
        self.routes_for_location = routes_for_location.RoutesForLocationResourceWithStreamingResponse(
            client.routes_for_location
        )
        self.routes_for_agency = routes_for_agency.RoutesForAgencyResourceWithStreamingResponse(
            client.routes_for_agency
        )
        self.schedule_for_route = schedule_for_route.ScheduleForRouteResourceWithStreamingResponse(
            client.schedule_for_route
        )
        self.arrival_and_departure = arrival_and_departure.ArrivalAndDepartureResourceWithStreamingResponse(
            client.arrival_and_departure
        )
        self.trip = trip.TripResourceWithStreamingResponse(client.trip)
        self.trips_for_location = trips_for_location.TripsForLocationResourceWithStreamingResponse(
            client.trips_for_location
        )
        self.trip_details = trip_details.TripDetailsResourceWithStreamingResponse(client.trip_details)
        self.trip_for_vehicle = trip_for_vehicle.TripForVehicleResourceWithStreamingResponse(client.trip_for_vehicle)
        self.trips_for_route = trips_for_route.TripsForRouteResourceWithStreamingResponse(client.trips_for_route)
        self.report_problem_with_stop = report_problem_with_stop.ReportProblemWithStopResourceWithStreamingResponse(
            client.report_problem_with_stop
        )
        self.report_problem_with_trip = report_problem_with_trip.ReportProblemWithTripResourceWithStreamingResponse(
            client.report_problem_with_trip
        )
        self.search_for_stop = search_for_stop.SearchForStopResourceWithStreamingResponse(client.search_for_stop)
        self.search_for_route = search_for_route.SearchForRouteResourceWithStreamingResponse(client.search_for_route)
        self.block = block.BlockResourceWithStreamingResponse(client.block)
        self.shape = shape.ShapeResourceWithStreamingResponse(client.shape)


class AsyncOnebusawaySDKWithStreamedResponse:
    def __init__(self, client: AsyncOnebusawaySDK) -> None:
        self.agencies_with_coverage = agencies_with_coverage.AsyncAgenciesWithCoverageResourceWithStreamingResponse(
            client.agencies_with_coverage
        )
        self.agency = agency.AsyncAgencyResourceWithStreamingResponse(client.agency)
        self.vehicles_for_agency = vehicles_for_agency.AsyncVehiclesForAgencyResourceWithStreamingResponse(
            client.vehicles_for_agency
        )
        self.config = config.AsyncConfigResourceWithStreamingResponse(client.config)
        self.current_time = current_time.AsyncCurrentTimeResourceWithStreamingResponse(client.current_time)
        self.stops_for_location = stops_for_location.AsyncStopsForLocationResourceWithStreamingResponse(
            client.stops_for_location
        )
        self.stops_for_route = stops_for_route.AsyncStopsForRouteResourceWithStreamingResponse(client.stops_for_route)
        self.stops_for_agency = stops_for_agency.AsyncStopsForAgencyResourceWithStreamingResponse(
            client.stops_for_agency
        )
        self.stop = stop.AsyncStopResourceWithStreamingResponse(client.stop)
        self.stop_ids_for_agency = stop_ids_for_agency.AsyncStopIDsForAgencyResourceWithStreamingResponse(
            client.stop_ids_for_agency
        )
        self.schedule_for_stop = schedule_for_stop.AsyncScheduleForStopResourceWithStreamingResponse(
            client.schedule_for_stop
        )
        self.route = route.AsyncRouteResourceWithStreamingResponse(client.route)
        self.route_ids_for_agency = route_ids_for_agency.AsyncRouteIDsForAgencyResourceWithStreamingResponse(
            client.route_ids_for_agency
        )
        self.routes_for_location = routes_for_location.AsyncRoutesForLocationResourceWithStreamingResponse(
            client.routes_for_location
        )
        self.routes_for_agency = routes_for_agency.AsyncRoutesForAgencyResourceWithStreamingResponse(
            client.routes_for_agency
        )
        self.schedule_for_route = schedule_for_route.AsyncScheduleForRouteResourceWithStreamingResponse(
            client.schedule_for_route
        )
        self.arrival_and_departure = arrival_and_departure.AsyncArrivalAndDepartureResourceWithStreamingResponse(
            client.arrival_and_departure
        )
        self.trip = trip.AsyncTripResourceWithStreamingResponse(client.trip)
        self.trips_for_location = trips_for_location.AsyncTripsForLocationResourceWithStreamingResponse(
            client.trips_for_location
        )
        self.trip_details = trip_details.AsyncTripDetailsResourceWithStreamingResponse(client.trip_details)
        self.trip_for_vehicle = trip_for_vehicle.AsyncTripForVehicleResourceWithStreamingResponse(
            client.trip_for_vehicle
        )
        self.trips_for_route = trips_for_route.AsyncTripsForRouteResourceWithStreamingResponse(client.trips_for_route)
        self.report_problem_with_stop = (
            report_problem_with_stop.AsyncReportProblemWithStopResourceWithStreamingResponse(
                client.report_problem_with_stop
            )
        )
        self.report_problem_with_trip = (
            report_problem_with_trip.AsyncReportProblemWithTripResourceWithStreamingResponse(
                client.report_problem_with_trip
            )
        )
        self.search_for_stop = search_for_stop.AsyncSearchForStopResourceWithStreamingResponse(client.search_for_stop)
        self.search_for_route = search_for_route.AsyncSearchForRouteResourceWithStreamingResponse(
            client.search_for_route
        )
        self.block = block.AsyncBlockResourceWithStreamingResponse(client.block)
        self.shape = shape.AsyncShapeResourceWithStreamingResponse(client.shape)


Client = OnebusawaySDK

AsyncClient = AsyncOnebusawaySDK
