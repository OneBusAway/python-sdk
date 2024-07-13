# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from onebusaway import OnebusawaySDK, AsyncOnebusawaySDK
from tests.utils import assert_matches_type
from onebusaway.types import StopsForLocationRetrieveResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestStopsForLocation:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_retrieve(self, client: OnebusawaySDK) -> None:
        stops_for_location = client.stops_for_location.retrieve(
            key="key",
        )
        assert_matches_type(StopsForLocationRetrieveResponse, stops_for_location, path=["response"])

    @parametrize
    def test_method_retrieve_with_all_params(self, client: OnebusawaySDK) -> None:
        stops_for_location = client.stops_for_location.retrieve(
            key="key",
            lat=0,
            lon=0,
        )
        assert_matches_type(StopsForLocationRetrieveResponse, stops_for_location, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: OnebusawaySDK) -> None:
        response = client.stops_for_location.with_raw_response.retrieve(
            key="key",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        stops_for_location = response.parse()
        assert_matches_type(StopsForLocationRetrieveResponse, stops_for_location, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: OnebusawaySDK) -> None:
        with client.stops_for_location.with_streaming_response.retrieve(
            key="key",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            stops_for_location = response.parse()
            assert_matches_type(StopsForLocationRetrieveResponse, stops_for_location, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncStopsForLocation:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncOnebusawaySDK) -> None:
        stops_for_location = await async_client.stops_for_location.retrieve(
            key="key",
        )
        assert_matches_type(StopsForLocationRetrieveResponse, stops_for_location, path=["response"])

    @parametrize
    async def test_method_retrieve_with_all_params(self, async_client: AsyncOnebusawaySDK) -> None:
        stops_for_location = await async_client.stops_for_location.retrieve(
            key="key",
            lat=0,
            lon=0,
        )
        assert_matches_type(StopsForLocationRetrieveResponse, stops_for_location, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncOnebusawaySDK) -> None:
        response = await async_client.stops_for_location.with_raw_response.retrieve(
            key="key",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        stops_for_location = await response.parse()
        assert_matches_type(StopsForLocationRetrieveResponse, stops_for_location, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncOnebusawaySDK) -> None:
        async with async_client.stops_for_location.with_streaming_response.retrieve(
            key="key",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            stops_for_location = await response.parse()
            assert_matches_type(StopsForLocationRetrieveResponse, stops_for_location, path=["response"])

        assert cast(Any, response.is_closed) is True
