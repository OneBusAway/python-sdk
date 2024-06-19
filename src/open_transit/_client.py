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
from ._exceptions import APIStatusError, OneBusAwayError
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
    "OneBusAway",
    "AsyncOneBusAway",
    "Client",
    "AsyncClient",
]


class OneBusAway(SyncAPIClient):
    agencies_with_coverage: resources.AgenciesWithCoverageResource
    config: resources.ConfigResource
    current_time: resources.CurrentTimeResource
    stops_for_location: resources.StopsForLocationResource
    arrival_and_departure_for_stop: resources.ArrivalAndDepartureForStopResource
    arrivals_and_departures_for_stop: resources.ArrivalsAndDeparturesForStopResource
    with_raw_response: OneBusAwayWithRawResponse
    with_streaming_response: OneBusAwayWithStreamedResponse

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
        """Construct a new synchronous OneBusAway client instance.

        This automatically infers the `api_key` argument from the `ONEBUSAWAY_API_KEY` environment variable if it is not provided.
        """
        if api_key is None:
            api_key = os.environ.get("ONEBUSAWAY_API_KEY")
        if api_key is None:
            raise OneBusAwayError(
                "The api_key client option must be set either by passing api_key to the client or by setting the ONEBUSAWAY_API_KEY environment variable"
            )
        self.api_key = api_key

        if base_url is None:
            base_url = os.environ.get("ONE_BUS_AWAY_BASE_URL")
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
        self.config = resources.ConfigResource(self)
        self.current_time = resources.CurrentTimeResource(self)
        self.stops_for_location = resources.StopsForLocationResource(self)
        self.arrival_and_departure_for_stop = resources.ArrivalAndDepartureForStopResource(self)
        self.arrivals_and_departures_for_stop = resources.ArrivalsAndDeparturesForStopResource(self)
        self.with_raw_response = OneBusAwayWithRawResponse(self)
        self.with_streaming_response = OneBusAwayWithStreamedResponse(self)

    @property
    @override
    def qs(self) -> Querystring:
        return Querystring(array_format="comma")

    @property
    def auth_headers(self) -> httpx.Auth:
        raise NotImplementedError("This auth method has not been implemented yet.")

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


class AsyncOneBusAway(AsyncAPIClient):
    agencies_with_coverage: resources.AsyncAgenciesWithCoverageResource
    config: resources.AsyncConfigResource
    current_time: resources.AsyncCurrentTimeResource
    stops_for_location: resources.AsyncStopsForLocationResource
    arrival_and_departure_for_stop: resources.AsyncArrivalAndDepartureForStopResource
    arrivals_and_departures_for_stop: resources.AsyncArrivalsAndDeparturesForStopResource
    with_raw_response: AsyncOneBusAwayWithRawResponse
    with_streaming_response: AsyncOneBusAwayWithStreamedResponse

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
        """Construct a new async OneBusAway client instance.

        This automatically infers the `api_key` argument from the `ONEBUSAWAY_API_KEY` environment variable if it is not provided.
        """
        if api_key is None:
            api_key = os.environ.get("ONEBUSAWAY_API_KEY")
        if api_key is None:
            raise OneBusAwayError(
                "The api_key client option must be set either by passing api_key to the client or by setting the ONEBUSAWAY_API_KEY environment variable"
            )
        self.api_key = api_key

        if base_url is None:
            base_url = os.environ.get("ONE_BUS_AWAY_BASE_URL")
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
        self.config = resources.AsyncConfigResource(self)
        self.current_time = resources.AsyncCurrentTimeResource(self)
        self.stops_for_location = resources.AsyncStopsForLocationResource(self)
        self.arrival_and_departure_for_stop = resources.AsyncArrivalAndDepartureForStopResource(self)
        self.arrivals_and_departures_for_stop = resources.AsyncArrivalsAndDeparturesForStopResource(self)
        self.with_raw_response = AsyncOneBusAwayWithRawResponse(self)
        self.with_streaming_response = AsyncOneBusAwayWithStreamedResponse(self)

    @property
    @override
    def qs(self) -> Querystring:
        return Querystring(array_format="comma")

    @property
    def auth_headers(self) -> httpx.Auth:
        raise NotImplementedError("This auth method has not been implemented yet.")

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


class OneBusAwayWithRawResponse:
    def __init__(self, client: OneBusAway) -> None:
        self.agencies_with_coverage = resources.AgenciesWithCoverageResourceWithRawResponse(
            client.agencies_with_coverage
        )
        self.config = resources.ConfigResourceWithRawResponse(client.config)
        self.current_time = resources.CurrentTimeResourceWithRawResponse(client.current_time)
        self.stops_for_location = resources.StopsForLocationResourceWithRawResponse(client.stops_for_location)
        self.arrival_and_departure_for_stop = resources.ArrivalAndDepartureForStopResourceWithRawResponse(
            client.arrival_and_departure_for_stop
        )
        self.arrivals_and_departures_for_stop = resources.ArrivalsAndDeparturesForStopResourceWithRawResponse(
            client.arrivals_and_departures_for_stop
        )


class AsyncOneBusAwayWithRawResponse:
    def __init__(self, client: AsyncOneBusAway) -> None:
        self.agencies_with_coverage = resources.AsyncAgenciesWithCoverageResourceWithRawResponse(
            client.agencies_with_coverage
        )
        self.config = resources.AsyncConfigResourceWithRawResponse(client.config)
        self.current_time = resources.AsyncCurrentTimeResourceWithRawResponse(client.current_time)
        self.stops_for_location = resources.AsyncStopsForLocationResourceWithRawResponse(client.stops_for_location)
        self.arrival_and_departure_for_stop = resources.AsyncArrivalAndDepartureForStopResourceWithRawResponse(
            client.arrival_and_departure_for_stop
        )
        self.arrivals_and_departures_for_stop = resources.AsyncArrivalsAndDeparturesForStopResourceWithRawResponse(
            client.arrivals_and_departures_for_stop
        )


class OneBusAwayWithStreamedResponse:
    def __init__(self, client: OneBusAway) -> None:
        self.agencies_with_coverage = resources.AgenciesWithCoverageResourceWithStreamingResponse(
            client.agencies_with_coverage
        )
        self.config = resources.ConfigResourceWithStreamingResponse(client.config)
        self.current_time = resources.CurrentTimeResourceWithStreamingResponse(client.current_time)
        self.stops_for_location = resources.StopsForLocationResourceWithStreamingResponse(client.stops_for_location)
        self.arrival_and_departure_for_stop = resources.ArrivalAndDepartureForStopResourceWithStreamingResponse(
            client.arrival_and_departure_for_stop
        )
        self.arrivals_and_departures_for_stop = resources.ArrivalsAndDeparturesForStopResourceWithStreamingResponse(
            client.arrivals_and_departures_for_stop
        )


class AsyncOneBusAwayWithStreamedResponse:
    def __init__(self, client: AsyncOneBusAway) -> None:
        self.agencies_with_coverage = resources.AsyncAgenciesWithCoverageResourceWithStreamingResponse(
            client.agencies_with_coverage
        )
        self.config = resources.AsyncConfigResourceWithStreamingResponse(client.config)
        self.current_time = resources.AsyncCurrentTimeResourceWithStreamingResponse(client.current_time)
        self.stops_for_location = resources.AsyncStopsForLocationResourceWithStreamingResponse(
            client.stops_for_location
        )
        self.arrival_and_departure_for_stop = resources.AsyncArrivalAndDepartureForStopResourceWithStreamingResponse(
            client.arrival_and_departure_for_stop
        )
        self.arrivals_and_departures_for_stop = (
            resources.AsyncArrivalsAndDeparturesForStopResourceWithStreamingResponse(
                client.arrivals_and_departures_for_stop
            )
        )


Client = OneBusAway

AsyncClient = AsyncOneBusAway
