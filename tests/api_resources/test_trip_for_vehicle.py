# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from onebusaway import OnebusawaySDK, AsyncOnebusawaySDK
from tests.utils import assert_matches_type
from onebusaway.types import TripForVehicleRetrieveResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestTripForVehicle:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_retrieve(self, client: OnebusawaySDK) -> None:
        trip_for_vehicle = client.trip_for_vehicle.retrieve(
            vehicle_id="vehicleID",
        )
        assert_matches_type(TripForVehicleRetrieveResponse, trip_for_vehicle, path=["response"])

    @parametrize
    def test_method_retrieve_with_all_params(self, client: OnebusawaySDK) -> None:
        trip_for_vehicle = client.trip_for_vehicle.retrieve(
            vehicle_id="vehicleID",
            include_schedule=True,
            include_status=True,
            include_trip=True,
            time=0,
        )
        assert_matches_type(TripForVehicleRetrieveResponse, trip_for_vehicle, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: OnebusawaySDK) -> None:
        response = client.trip_for_vehicle.with_raw_response.retrieve(
            vehicle_id="vehicleID",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        trip_for_vehicle = response.parse()
        assert_matches_type(TripForVehicleRetrieveResponse, trip_for_vehicle, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: OnebusawaySDK) -> None:
        with client.trip_for_vehicle.with_streaming_response.retrieve(
            vehicle_id="vehicleID",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            trip_for_vehicle = response.parse()
            assert_matches_type(TripForVehicleRetrieveResponse, trip_for_vehicle, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: OnebusawaySDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `vehicle_id` but received ''"):
            client.trip_for_vehicle.with_raw_response.retrieve(
                vehicle_id="",
            )


class TestAsyncTripForVehicle:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncOnebusawaySDK) -> None:
        trip_for_vehicle = await async_client.trip_for_vehicle.retrieve(
            vehicle_id="vehicleID",
        )
        assert_matches_type(TripForVehicleRetrieveResponse, trip_for_vehicle, path=["response"])

    @parametrize
    async def test_method_retrieve_with_all_params(self, async_client: AsyncOnebusawaySDK) -> None:
        trip_for_vehicle = await async_client.trip_for_vehicle.retrieve(
            vehicle_id="vehicleID",
            include_schedule=True,
            include_status=True,
            include_trip=True,
            time=0,
        )
        assert_matches_type(TripForVehicleRetrieveResponse, trip_for_vehicle, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncOnebusawaySDK) -> None:
        response = await async_client.trip_for_vehicle.with_raw_response.retrieve(
            vehicle_id="vehicleID",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        trip_for_vehicle = await response.parse()
        assert_matches_type(TripForVehicleRetrieveResponse, trip_for_vehicle, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncOnebusawaySDK) -> None:
        async with async_client.trip_for_vehicle.with_streaming_response.retrieve(
            vehicle_id="vehicleID",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            trip_for_vehicle = await response.parse()
            assert_matches_type(TripForVehicleRetrieveResponse, trip_for_vehicle, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncOnebusawaySDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `vehicle_id` but received ''"):
            await async_client.trip_for_vehicle.with_raw_response.retrieve(
                vehicle_id="",
            )
