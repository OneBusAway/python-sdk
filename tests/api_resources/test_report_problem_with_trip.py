# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from onebusaway import OnebusawaySDK, AsyncOnebusawaySDK
from tests.utils import assert_matches_type
from onebusaway.types.shared import ResponseWrapper

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestReportProblemWithTrip:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_retrieve(self, client: OnebusawaySDK) -> None:
        report_problem_with_trip = client.report_problem_with_trip.retrieve(
            trip_id="tripID",
        )
        assert_matches_type(ResponseWrapper, report_problem_with_trip, path=["response"])

    @parametrize
    def test_method_retrieve_with_all_params(self, client: OnebusawaySDK) -> None:
        report_problem_with_trip = client.report_problem_with_trip.retrieve(
            trip_id="tripID",
            code="vehicle_never_came",
            service_date=0,
            stop_id="stopID",
            user_comment="userComment",
            user_lat=0,
            user_location_accuracy=0,
            user_lon=0,
            user_on_vehicle=True,
            user_vehicle_number="userVehicleNumber",
            vehicle_id="vehicleID",
        )
        assert_matches_type(ResponseWrapper, report_problem_with_trip, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: OnebusawaySDK) -> None:
        response = client.report_problem_with_trip.with_raw_response.retrieve(
            trip_id="tripID",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        report_problem_with_trip = response.parse()
        assert_matches_type(ResponseWrapper, report_problem_with_trip, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: OnebusawaySDK) -> None:
        with client.report_problem_with_trip.with_streaming_response.retrieve(
            trip_id="tripID",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            report_problem_with_trip = response.parse()
            assert_matches_type(ResponseWrapper, report_problem_with_trip, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: OnebusawaySDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `trip_id` but received ''"):
            client.report_problem_with_trip.with_raw_response.retrieve(
                trip_id="",
            )


class TestAsyncReportProblemWithTrip:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncOnebusawaySDK) -> None:
        report_problem_with_trip = await async_client.report_problem_with_trip.retrieve(
            trip_id="tripID",
        )
        assert_matches_type(ResponseWrapper, report_problem_with_trip, path=["response"])

    @parametrize
    async def test_method_retrieve_with_all_params(self, async_client: AsyncOnebusawaySDK) -> None:
        report_problem_with_trip = await async_client.report_problem_with_trip.retrieve(
            trip_id="tripID",
            code="vehicle_never_came",
            service_date=0,
            stop_id="stopID",
            user_comment="userComment",
            user_lat=0,
            user_location_accuracy=0,
            user_lon=0,
            user_on_vehicle=True,
            user_vehicle_number="userVehicleNumber",
            vehicle_id="vehicleID",
        )
        assert_matches_type(ResponseWrapper, report_problem_with_trip, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncOnebusawaySDK) -> None:
        response = await async_client.report_problem_with_trip.with_raw_response.retrieve(
            trip_id="tripID",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        report_problem_with_trip = await response.parse()
        assert_matches_type(ResponseWrapper, report_problem_with_trip, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncOnebusawaySDK) -> None:
        async with async_client.report_problem_with_trip.with_streaming_response.retrieve(
            trip_id="tripID",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            report_problem_with_trip = await response.parse()
            assert_matches_type(ResponseWrapper, report_problem_with_trip, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncOnebusawaySDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `trip_id` but received ''"):
            await async_client.report_problem_with_trip.with_raw_response.retrieve(
                trip_id="",
            )
