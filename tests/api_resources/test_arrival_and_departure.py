# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from onebusaway import OnebusawaySDK, AsyncOnebusawaySDK
from tests.utils import assert_matches_type
from onebusaway.types import (
    ArrivalAndDepartureListResponse,
    ArrivalAndDepartureRetrieveResponse,
)
from onebusaway._utils import parse_datetime

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestArrivalAndDeparture:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_retrieve(self, client: OnebusawaySDK) -> None:
        arrival_and_departure = client.arrival_and_departure.retrieve(
            stop_id="1_75403",
            service_date=0,
            trip_id="tripId",
        )
        assert_matches_type(ArrivalAndDepartureRetrieveResponse, arrival_and_departure, path=["response"])

    @parametrize
    def test_method_retrieve_with_all_params(self, client: OnebusawaySDK) -> None:
        arrival_and_departure = client.arrival_and_departure.retrieve(
            stop_id="1_75403",
            service_date=0,
            trip_id="tripId",
            stop_sequence=0,
            time=0,
            vehicle_id="vehicleId",
        )
        assert_matches_type(ArrivalAndDepartureRetrieveResponse, arrival_and_departure, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: OnebusawaySDK) -> None:
        response = client.arrival_and_departure.with_raw_response.retrieve(
            stop_id="1_75403",
            service_date=0,
            trip_id="tripId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        arrival_and_departure = response.parse()
        assert_matches_type(ArrivalAndDepartureRetrieveResponse, arrival_and_departure, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: OnebusawaySDK) -> None:
        with client.arrival_and_departure.with_streaming_response.retrieve(
            stop_id="1_75403",
            service_date=0,
            trip_id="tripId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            arrival_and_departure = response.parse()
            assert_matches_type(ArrivalAndDepartureRetrieveResponse, arrival_and_departure, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: OnebusawaySDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `stop_id` but received ''"):
            client.arrival_and_departure.with_raw_response.retrieve(
                stop_id="",
                service_date=0,
                trip_id="tripId",
            )

    @parametrize
    def test_method_list(self, client: OnebusawaySDK) -> None:
        arrival_and_departure = client.arrival_and_departure.list(
            stop_id="1_75403",
        )
        assert_matches_type(ArrivalAndDepartureListResponse, arrival_and_departure, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: OnebusawaySDK) -> None:
        arrival_and_departure = client.arrival_and_departure.list(
            stop_id="1_75403",
            minutes_after=0,
            minutes_before=0,
            time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(ArrivalAndDepartureListResponse, arrival_and_departure, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: OnebusawaySDK) -> None:
        response = client.arrival_and_departure.with_raw_response.list(
            stop_id="1_75403",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        arrival_and_departure = response.parse()
        assert_matches_type(ArrivalAndDepartureListResponse, arrival_and_departure, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: OnebusawaySDK) -> None:
        with client.arrival_and_departure.with_streaming_response.list(
            stop_id="1_75403",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            arrival_and_departure = response.parse()
            assert_matches_type(ArrivalAndDepartureListResponse, arrival_and_departure, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_list(self, client: OnebusawaySDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `stop_id` but received ''"):
            client.arrival_and_departure.with_raw_response.list(
                stop_id="",
            )


class TestAsyncArrivalAndDeparture:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncOnebusawaySDK) -> None:
        arrival_and_departure = await async_client.arrival_and_departure.retrieve(
            stop_id="1_75403",
            service_date=0,
            trip_id="tripId",
        )
        assert_matches_type(ArrivalAndDepartureRetrieveResponse, arrival_and_departure, path=["response"])

    @parametrize
    async def test_method_retrieve_with_all_params(self, async_client: AsyncOnebusawaySDK) -> None:
        arrival_and_departure = await async_client.arrival_and_departure.retrieve(
            stop_id="1_75403",
            service_date=0,
            trip_id="tripId",
            stop_sequence=0,
            time=0,
            vehicle_id="vehicleId",
        )
        assert_matches_type(ArrivalAndDepartureRetrieveResponse, arrival_and_departure, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncOnebusawaySDK) -> None:
        response = await async_client.arrival_and_departure.with_raw_response.retrieve(
            stop_id="1_75403",
            service_date=0,
            trip_id="tripId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        arrival_and_departure = await response.parse()
        assert_matches_type(ArrivalAndDepartureRetrieveResponse, arrival_and_departure, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncOnebusawaySDK) -> None:
        async with async_client.arrival_and_departure.with_streaming_response.retrieve(
            stop_id="1_75403",
            service_date=0,
            trip_id="tripId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            arrival_and_departure = await response.parse()
            assert_matches_type(ArrivalAndDepartureRetrieveResponse, arrival_and_departure, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncOnebusawaySDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `stop_id` but received ''"):
            await async_client.arrival_and_departure.with_raw_response.retrieve(
                stop_id="",
                service_date=0,
                trip_id="tripId",
            )

    @parametrize
    async def test_method_list(self, async_client: AsyncOnebusawaySDK) -> None:
        arrival_and_departure = await async_client.arrival_and_departure.list(
            stop_id="1_75403",
        )
        assert_matches_type(ArrivalAndDepartureListResponse, arrival_and_departure, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncOnebusawaySDK) -> None:
        arrival_and_departure = await async_client.arrival_and_departure.list(
            stop_id="1_75403",
            minutes_after=0,
            minutes_before=0,
            time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(ArrivalAndDepartureListResponse, arrival_and_departure, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncOnebusawaySDK) -> None:
        response = await async_client.arrival_and_departure.with_raw_response.list(
            stop_id="1_75403",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        arrival_and_departure = await response.parse()
        assert_matches_type(ArrivalAndDepartureListResponse, arrival_and_departure, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncOnebusawaySDK) -> None:
        async with async_client.arrival_and_departure.with_streaming_response.list(
            stop_id="1_75403",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            arrival_and_departure = await response.parse()
            assert_matches_type(ArrivalAndDepartureListResponse, arrival_and_departure, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_list(self, async_client: AsyncOnebusawaySDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `stop_id` but received ''"):
            await async_client.arrival_and_departure.with_raw_response.list(
                stop_id="",
            )
