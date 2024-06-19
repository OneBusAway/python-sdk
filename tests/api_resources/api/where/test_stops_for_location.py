# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from open_transit import OneBusAway, AsyncOneBusAway
from open_transit.types.api.where import StopsForLocationListResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestStopsForLocation:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_list(self, client: OneBusAway) -> None:
        stops_for_location = client.api.where.stops_for_location.list(
            key="string",
        )
        assert_matches_type(StopsForLocationListResponse, stops_for_location, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: OneBusAway) -> None:
        stops_for_location = client.api.where.stops_for_location.list(
            key="string",
            lat=0,
            lon=0,
        )
        assert_matches_type(StopsForLocationListResponse, stops_for_location, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: OneBusAway) -> None:
        response = client.api.where.stops_for_location.with_raw_response.list(
            key="string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        stops_for_location = response.parse()
        assert_matches_type(StopsForLocationListResponse, stops_for_location, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: OneBusAway) -> None:
        with client.api.where.stops_for_location.with_streaming_response.list(
            key="string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            stops_for_location = response.parse()
            assert_matches_type(StopsForLocationListResponse, stops_for_location, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncStopsForLocation:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_list(self, async_client: AsyncOneBusAway) -> None:
        stops_for_location = await async_client.api.where.stops_for_location.list(
            key="string",
        )
        assert_matches_type(StopsForLocationListResponse, stops_for_location, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncOneBusAway) -> None:
        stops_for_location = await async_client.api.where.stops_for_location.list(
            key="string",
            lat=0,
            lon=0,
        )
        assert_matches_type(StopsForLocationListResponse, stops_for_location, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncOneBusAway) -> None:
        response = await async_client.api.where.stops_for_location.with_raw_response.list(
            key="string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        stops_for_location = await response.parse()
        assert_matches_type(StopsForLocationListResponse, stops_for_location, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncOneBusAway) -> None:
        async with async_client.api.where.stops_for_location.with_streaming_response.list(
            key="string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            stops_for_location = await response.parse()
            assert_matches_type(StopsForLocationListResponse, stops_for_location, path=["response"])

        assert cast(Any, response.is_closed) is True