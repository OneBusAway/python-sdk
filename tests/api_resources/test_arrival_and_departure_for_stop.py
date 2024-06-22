# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from onebusaway import OnebusawaySDK, AsyncOnebusawaySDK
from tests.utils import assert_matches_type
from onebusaway.types import ArrivalAndDepartureForStopRetrieveResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestArrivalAndDepartureForStop:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_retrieve(self, client: OnebusawaySDK) -> None:
        arrival_and_departure_for_stop = client.arrival_and_departure_for_stop.retrieve(
            "string",
            service_date=0,
            trip_id="string",
        )
        assert_matches_type(
            ArrivalAndDepartureForStopRetrieveResponse, arrival_and_departure_for_stop, path=["response"]
        )

    @parametrize
    def test_method_retrieve_with_all_params(self, client: OnebusawaySDK) -> None:
        arrival_and_departure_for_stop = client.arrival_and_departure_for_stop.retrieve(
            "string",
            service_date=0,
            trip_id="string",
            stop_sequence=0,
            time=0,
            vehicle_id="string",
        )
        assert_matches_type(
            ArrivalAndDepartureForStopRetrieveResponse, arrival_and_departure_for_stop, path=["response"]
        )

    @parametrize
    def test_raw_response_retrieve(self, client: OnebusawaySDK) -> None:
        response = client.arrival_and_departure_for_stop.with_raw_response.retrieve(
            "string",
            service_date=0,
            trip_id="string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        arrival_and_departure_for_stop = response.parse()
        assert_matches_type(
            ArrivalAndDepartureForStopRetrieveResponse, arrival_and_departure_for_stop, path=["response"]
        )

    @parametrize
    def test_streaming_response_retrieve(self, client: OnebusawaySDK) -> None:
        with client.arrival_and_departure_for_stop.with_streaming_response.retrieve(
            "string",
            service_date=0,
            trip_id="string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            arrival_and_departure_for_stop = response.parse()
            assert_matches_type(
                ArrivalAndDepartureForStopRetrieveResponse, arrival_and_departure_for_stop, path=["response"]
            )

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: OnebusawaySDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `stop_id` but received ''"):
            client.arrival_and_departure_for_stop.with_raw_response.retrieve(
                "",
                service_date=0,
                trip_id="string",
            )


class TestAsyncArrivalAndDepartureForStop:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncOnebusawaySDK) -> None:
        arrival_and_departure_for_stop = await async_client.arrival_and_departure_for_stop.retrieve(
            "string",
            service_date=0,
            trip_id="string",
        )
        assert_matches_type(
            ArrivalAndDepartureForStopRetrieveResponse, arrival_and_departure_for_stop, path=["response"]
        )

    @parametrize
    async def test_method_retrieve_with_all_params(self, async_client: AsyncOnebusawaySDK) -> None:
        arrival_and_departure_for_stop = await async_client.arrival_and_departure_for_stop.retrieve(
            "string",
            service_date=0,
            trip_id="string",
            stop_sequence=0,
            time=0,
            vehicle_id="string",
        )
        assert_matches_type(
            ArrivalAndDepartureForStopRetrieveResponse, arrival_and_departure_for_stop, path=["response"]
        )

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncOnebusawaySDK) -> None:
        response = await async_client.arrival_and_departure_for_stop.with_raw_response.retrieve(
            "string",
            service_date=0,
            trip_id="string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        arrival_and_departure_for_stop = await response.parse()
        assert_matches_type(
            ArrivalAndDepartureForStopRetrieveResponse, arrival_and_departure_for_stop, path=["response"]
        )

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncOnebusawaySDK) -> None:
        async with async_client.arrival_and_departure_for_stop.with_streaming_response.retrieve(
            "string",
            service_date=0,
            trip_id="string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            arrival_and_departure_for_stop = await response.parse()
            assert_matches_type(
                ArrivalAndDepartureForStopRetrieveResponse, arrival_and_departure_for_stop, path=["response"]
            )

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncOnebusawaySDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `stop_id` but received ''"):
            await async_client.arrival_and_departure_for_stop.with_raw_response.retrieve(
                "",
                service_date=0,
                trip_id="string",
            )
