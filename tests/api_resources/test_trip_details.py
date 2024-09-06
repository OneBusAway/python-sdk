# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from onebusaway import OnebusawaySDK, AsyncOnebusawaySDK
from tests.utils import assert_matches_type
from onebusaway.types import TripDetailRetrieveResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestTripDetails:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_retrieve(self, client: OnebusawaySDK) -> None:
        trip_detail = client.trip_details.retrieve(
            trip_id="tripID",
        )
        assert_matches_type(TripDetailRetrieveResponse, trip_detail, path=["response"])

    @parametrize
    def test_method_retrieve_with_all_params(self, client: OnebusawaySDK) -> None:
        trip_detail = client.trip_details.retrieve(
            trip_id="tripID",
            include_schedule=True,
            include_status=True,
            include_trip=True,
            service_date=0,
            time=0,
        )
        assert_matches_type(TripDetailRetrieveResponse, trip_detail, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: OnebusawaySDK) -> None:
        response = client.trip_details.with_raw_response.retrieve(
            trip_id="tripID",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        trip_detail = response.parse()
        assert_matches_type(TripDetailRetrieveResponse, trip_detail, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: OnebusawaySDK) -> None:
        with client.trip_details.with_streaming_response.retrieve(
            trip_id="tripID",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            trip_detail = response.parse()
            assert_matches_type(TripDetailRetrieveResponse, trip_detail, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: OnebusawaySDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `trip_id` but received ''"):
            client.trip_details.with_raw_response.retrieve(
                trip_id="",
            )


class TestAsyncTripDetails:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncOnebusawaySDK) -> None:
        trip_detail = await async_client.trip_details.retrieve(
            trip_id="tripID",
        )
        assert_matches_type(TripDetailRetrieveResponse, trip_detail, path=["response"])

    @parametrize
    async def test_method_retrieve_with_all_params(self, async_client: AsyncOnebusawaySDK) -> None:
        trip_detail = await async_client.trip_details.retrieve(
            trip_id="tripID",
            include_schedule=True,
            include_status=True,
            include_trip=True,
            service_date=0,
            time=0,
        )
        assert_matches_type(TripDetailRetrieveResponse, trip_detail, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncOnebusawaySDK) -> None:
        response = await async_client.trip_details.with_raw_response.retrieve(
            trip_id="tripID",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        trip_detail = await response.parse()
        assert_matches_type(TripDetailRetrieveResponse, trip_detail, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncOnebusawaySDK) -> None:
        async with async_client.trip_details.with_streaming_response.retrieve(
            trip_id="tripID",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            trip_detail = await response.parse()
            assert_matches_type(TripDetailRetrieveResponse, trip_detail, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncOnebusawaySDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `trip_id` but received ''"):
            await async_client.trip_details.with_raw_response.retrieve(
                trip_id="",
            )
