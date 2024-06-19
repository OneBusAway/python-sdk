# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from open_transit import OpenTransit, AsyncOpenTransit
from open_transit.types.where.stop import ArrivalsAndDepartureListResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestArrivalsAndDepartures:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_list(self, client: OpenTransit) -> None:
        arrivals_and_departure = client.where.stop.arrivals_and_departures.list(
            "string",
        )
        assert_matches_type(ArrivalsAndDepartureListResponse, arrivals_and_departure, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: OpenTransit) -> None:
        response = client.where.stop.arrivals_and_departures.with_raw_response.list(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        arrivals_and_departure = response.parse()
        assert_matches_type(ArrivalsAndDepartureListResponse, arrivals_and_departure, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: OpenTransit) -> None:
        with client.where.stop.arrivals_and_departures.with_streaming_response.list(
            "string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            arrivals_and_departure = response.parse()
            assert_matches_type(ArrivalsAndDepartureListResponse, arrivals_and_departure, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_list(self, client: OpenTransit) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `stop_id` but received ''"):
            client.where.stop.arrivals_and_departures.with_raw_response.list(
                "",
            )


class TestAsyncArrivalsAndDepartures:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_list(self, async_client: AsyncOpenTransit) -> None:
        arrivals_and_departure = await async_client.where.stop.arrivals_and_departures.list(
            "string",
        )
        assert_matches_type(ArrivalsAndDepartureListResponse, arrivals_and_departure, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncOpenTransit) -> None:
        response = await async_client.where.stop.arrivals_and_departures.with_raw_response.list(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        arrivals_and_departure = await response.parse()
        assert_matches_type(ArrivalsAndDepartureListResponse, arrivals_and_departure, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncOpenTransit) -> None:
        async with async_client.where.stop.arrivals_and_departures.with_streaming_response.list(
            "string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            arrivals_and_departure = await response.parse()
            assert_matches_type(ArrivalsAndDepartureListResponse, arrivals_and_departure, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_list(self, async_client: AsyncOpenTransit) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `stop_id` but received ''"):
            await async_client.where.stop.arrivals_and_departures.with_raw_response.list(
                "",
            )
