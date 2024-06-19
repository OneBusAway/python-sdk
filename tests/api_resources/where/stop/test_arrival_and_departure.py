# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from open_transit import OpenTransit, AsyncOpenTransit
from open_transit.types.where.stop import ArrivalAndDepartureRetrieveResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestArrivalAndDeparture:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_retrieve(self, client: OpenTransit) -> None:
        arrival_and_departure = client.where.stop.arrival_and_departure.retrieve(
            "string",
            service_date=0,
            trip_id="string",
        )
        assert_matches_type(ArrivalAndDepartureRetrieveResponse, arrival_and_departure, path=["response"])

    @parametrize
    def test_method_retrieve_with_all_params(self, client: OpenTransit) -> None:
        arrival_and_departure = client.where.stop.arrival_and_departure.retrieve(
            "string",
            service_date=0,
            trip_id="string",
            stop_sequence=0,
            time=0,
            vehicle_id="string",
        )
        assert_matches_type(ArrivalAndDepartureRetrieveResponse, arrival_and_departure, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: OpenTransit) -> None:
        response = client.where.stop.arrival_and_departure.with_raw_response.retrieve(
            "string",
            service_date=0,
            trip_id="string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        arrival_and_departure = response.parse()
        assert_matches_type(ArrivalAndDepartureRetrieveResponse, arrival_and_departure, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: OpenTransit) -> None:
        with client.where.stop.arrival_and_departure.with_streaming_response.retrieve(
            "string",
            service_date=0,
            trip_id="string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            arrival_and_departure = response.parse()
            assert_matches_type(ArrivalAndDepartureRetrieveResponse, arrival_and_departure, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: OpenTransit) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `stop_id` but received ''"):
            client.where.stop.arrival_and_departure.with_raw_response.retrieve(
                "",
                service_date=0,
                trip_id="string",
            )


class TestAsyncArrivalAndDeparture:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncOpenTransit) -> None:
        arrival_and_departure = await async_client.where.stop.arrival_and_departure.retrieve(
            "string",
            service_date=0,
            trip_id="string",
        )
        assert_matches_type(ArrivalAndDepartureRetrieveResponse, arrival_and_departure, path=["response"])

    @parametrize
    async def test_method_retrieve_with_all_params(self, async_client: AsyncOpenTransit) -> None:
        arrival_and_departure = await async_client.where.stop.arrival_and_departure.retrieve(
            "string",
            service_date=0,
            trip_id="string",
            stop_sequence=0,
            time=0,
            vehicle_id="string",
        )
        assert_matches_type(ArrivalAndDepartureRetrieveResponse, arrival_and_departure, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncOpenTransit) -> None:
        response = await async_client.where.stop.arrival_and_departure.with_raw_response.retrieve(
            "string",
            service_date=0,
            trip_id="string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        arrival_and_departure = await response.parse()
        assert_matches_type(ArrivalAndDepartureRetrieveResponse, arrival_and_departure, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncOpenTransit) -> None:
        async with async_client.where.stop.arrival_and_departure.with_streaming_response.retrieve(
            "string",
            service_date=0,
            trip_id="string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            arrival_and_departure = await response.parse()
            assert_matches_type(ArrivalAndDepartureRetrieveResponse, arrival_and_departure, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncOpenTransit) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `stop_id` but received ''"):
            await async_client.where.stop.arrival_and_departure.with_raw_response.retrieve(
                "",
                service_date=0,
                trip_id="string",
            )
