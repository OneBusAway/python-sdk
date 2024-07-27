# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, Union, Mapping
from typing_extensions import Self, override

import httpx

from . import resources, _exceptions
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
from ._utils import (
    is_given,
    get_async_library,
)
from ._version import __version__
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
    "resources",
    "OnebusawaySDK",
    "AsyncOnebusawaySDK",
    "Client",
    "AsyncClient",
]


class OnebusawaySDK(SyncAPIClient):
    agencies_with_coverage: resources.AgenciesWithCoverageResource
    agency: resources.AgencyResource
    config: resources.ConfigResource
    current_time: resources.CurrentTimeResource
    stops_for_location: resources.StopsForLocationResource
    stops_for_route: resources.StopsForRouteResource
    stop: resources.StopResource
    stop_ids_for_agency: resources.StopIDsForAgencyResource
    route: resources.RouteResource
    arrival_and_departure: resources.ArrivalAndDepartureResource
    trip: resources.TripResource
    trips_for_location: resources.TripsForLocationResource
    trip_details: resources.TripDetailsResource
    trip_for_vehicle: resources.TripForVehicleResource
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
        """Construct a new synchronous onebusaway-sdk client instance.

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

        self.agencies_with_coverage = resources.AgenciesWithCoverageResource(self)
        self.agency = resources.AgencyResource(self)
        self.config = resources.ConfigResource(self)
        self.current_time = resources.CurrentTimeResource(self)
        self.stops_for_location = resources.StopsForLocationResource(self)
        self.stops_for_route = resources.StopsForRouteResource(self)
        self.stop = resources.StopResource(self)
        self.stop_ids_for_agency = resources.StopIDsForAgencyResource(self)
        self.route = resources.RouteResource(self)
        self.arrival_and_departure = resources.ArrivalAndDepartureResource(self)
        self.trip = resources.TripResource(self)
        self.trips_for_location = resources.TripsForLocationResource(self)
        self.trip_details = resources.TripDetailsResource(self)
        self.trip_for_vehicle = resources.TripForVehicleResource(self)
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
    agencies_with_coverage: resources.AsyncAgenciesWithCoverageResource
    agency: resources.AsyncAgencyResource
    config: resources.AsyncConfigResource
    current_time: resources.AsyncCurrentTimeResource
    stops_for_location: resources.AsyncStopsForLocationResource
    stops_for_route: resources.AsyncStopsForRouteResource
    stop: resources.AsyncStopResource
    stop_ids_for_agency: resources.AsyncStopIDsForAgencyResource
    route: resources.AsyncRouteResource
    arrival_and_departure: resources.AsyncArrivalAndDepartureResource
    trip: resources.AsyncTripResource
    trips_for_location: resources.AsyncTripsForLocationResource
    trip_details: resources.AsyncTripDetailsResource
    trip_for_vehicle: resources.AsyncTripForVehicleResource
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
        """Construct a new async onebusaway-sdk client instance.

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

        self.agencies_with_coverage = resources.AsyncAgenciesWithCoverageResource(self)
        self.agency = resources.AsyncAgencyResource(self)
        self.config = resources.AsyncConfigResource(self)
        self.current_time = resources.AsyncCurrentTimeResource(self)
        self.stops_for_location = resources.AsyncStopsForLocationResource(self)
        self.stops_for_route = resources.AsyncStopsForRouteResource(self)
        self.stop = resources.AsyncStopResource(self)
        self.stop_ids_for_agency = resources.AsyncStopIDsForAgencyResource(self)
        self.route = resources.AsyncRouteResource(self)
        self.arrival_and_departure = resources.AsyncArrivalAndDepartureResource(self)
        self.trip = resources.AsyncTripResource(self)
        self.trips_for_location = resources.AsyncTripsForLocationResource(self)
        self.trip_details = resources.AsyncTripDetailsResource(self)
        self.trip_for_vehicle = resources.AsyncTripForVehicleResource(self)
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
        self.agencies_with_coverage = resources.AgenciesWithCoverageResourceWithRawResponse(
            client.agencies_with_coverage
        )
        self.agency = resources.AgencyResourceWithRawResponse(client.agency)
        self.config = resources.ConfigResourceWithRawResponse(client.config)
        self.current_time = resources.CurrentTimeResourceWithRawResponse(client.current_time)
        self.stops_for_location = resources.StopsForLocationResourceWithRawResponse(client.stops_for_location)
        self.stops_for_route = resources.StopsForRouteResourceWithRawResponse(client.stops_for_route)
        self.stop = resources.StopResourceWithRawResponse(client.stop)
        self.stop_ids_for_agency = resources.StopIDsForAgencyResourceWithRawResponse(client.stop_ids_for_agency)
        self.route = resources.RouteResourceWithRawResponse(client.route)
        self.arrival_and_departure = resources.ArrivalAndDepartureResourceWithRawResponse(client.arrival_and_departure)
        self.trip = resources.TripResourceWithRawResponse(client.trip)
        self.trips_for_location = resources.TripsForLocationResourceWithRawResponse(client.trips_for_location)
        self.trip_details = resources.TripDetailsResourceWithRawResponse(client.trip_details)
        self.trip_for_vehicle = resources.TripForVehicleResourceWithRawResponse(client.trip_for_vehicle)


class AsyncOnebusawaySDKWithRawResponse:
    def __init__(self, client: AsyncOnebusawaySDK) -> None:
        self.agencies_with_coverage = resources.AsyncAgenciesWithCoverageResourceWithRawResponse(
            client.agencies_with_coverage
        )
        self.agency = resources.AsyncAgencyResourceWithRawResponse(client.agency)
        self.config = resources.AsyncConfigResourceWithRawResponse(client.config)
        self.current_time = resources.AsyncCurrentTimeResourceWithRawResponse(client.current_time)
        self.stops_for_location = resources.AsyncStopsForLocationResourceWithRawResponse(client.stops_for_location)
        self.stops_for_route = resources.AsyncStopsForRouteResourceWithRawResponse(client.stops_for_route)
        self.stop = resources.AsyncStopResourceWithRawResponse(client.stop)
        self.stop_ids_for_agency = resources.AsyncStopIDsForAgencyResourceWithRawResponse(client.stop_ids_for_agency)
        self.route = resources.AsyncRouteResourceWithRawResponse(client.route)
        self.arrival_and_departure = resources.AsyncArrivalAndDepartureResourceWithRawResponse(
            client.arrival_and_departure
        )
        self.trip = resources.AsyncTripResourceWithRawResponse(client.trip)
        self.trips_for_location = resources.AsyncTripsForLocationResourceWithRawResponse(client.trips_for_location)
        self.trip_details = resources.AsyncTripDetailsResourceWithRawResponse(client.trip_details)
        self.trip_for_vehicle = resources.AsyncTripForVehicleResourceWithRawResponse(client.trip_for_vehicle)


class OnebusawaySDKWithStreamedResponse:
    def __init__(self, client: OnebusawaySDK) -> None:
        self.agencies_with_coverage = resources.AgenciesWithCoverageResourceWithStreamingResponse(
            client.agencies_with_coverage
        )
        self.agency = resources.AgencyResourceWithStreamingResponse(client.agency)
        self.config = resources.ConfigResourceWithStreamingResponse(client.config)
        self.current_time = resources.CurrentTimeResourceWithStreamingResponse(client.current_time)
        self.stops_for_location = resources.StopsForLocationResourceWithStreamingResponse(client.stops_for_location)
        self.stops_for_route = resources.StopsForRouteResourceWithStreamingResponse(client.stops_for_route)
        self.stop = resources.StopResourceWithStreamingResponse(client.stop)
        self.stop_ids_for_agency = resources.StopIDsForAgencyResourceWithStreamingResponse(client.stop_ids_for_agency)
        self.route = resources.RouteResourceWithStreamingResponse(client.route)
        self.arrival_and_departure = resources.ArrivalAndDepartureResourceWithStreamingResponse(
            client.arrival_and_departure
        )
        self.trip = resources.TripResourceWithStreamingResponse(client.trip)
        self.trips_for_location = resources.TripsForLocationResourceWithStreamingResponse(client.trips_for_location)
        self.trip_details = resources.TripDetailsResourceWithStreamingResponse(client.trip_details)
        self.trip_for_vehicle = resources.TripForVehicleResourceWithStreamingResponse(client.trip_for_vehicle)


class AsyncOnebusawaySDKWithStreamedResponse:
    def __init__(self, client: AsyncOnebusawaySDK) -> None:
        self.agencies_with_coverage = resources.AsyncAgenciesWithCoverageResourceWithStreamingResponse(
            client.agencies_with_coverage
        )
        self.agency = resources.AsyncAgencyResourceWithStreamingResponse(client.agency)
        self.config = resources.AsyncConfigResourceWithStreamingResponse(client.config)
        self.current_time = resources.AsyncCurrentTimeResourceWithStreamingResponse(client.current_time)
        self.stops_for_location = resources.AsyncStopsForLocationResourceWithStreamingResponse(
            client.stops_for_location
        )
        self.stops_for_route = resources.AsyncStopsForRouteResourceWithStreamingResponse(client.stops_for_route)
        self.stop = resources.AsyncStopResourceWithStreamingResponse(client.stop)
        self.stop_ids_for_agency = resources.AsyncStopIDsForAgencyResourceWithStreamingResponse(
            client.stop_ids_for_agency
        )
        self.route = resources.AsyncRouteResourceWithStreamingResponse(client.route)
        self.arrival_and_departure = resources.AsyncArrivalAndDepartureResourceWithStreamingResponse(
            client.arrival_and_departure
        )
        self.trip = resources.AsyncTripResourceWithStreamingResponse(client.trip)
        self.trips_for_location = resources.AsyncTripsForLocationResourceWithStreamingResponse(
            client.trips_for_location
        )
        self.trip_details = resources.AsyncTripDetailsResourceWithStreamingResponse(client.trip_details)
        self.trip_for_vehicle = resources.AsyncTripForVehicleResourceWithStreamingResponse(client.trip_for_vehicle)


Client = OnebusawaySDK

AsyncClient = AsyncOnebusawaySDK
