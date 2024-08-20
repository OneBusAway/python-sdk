# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from onebusaway import OnebusawaySDK, AsyncOnebusawaySDK
from tests.utils import assert_matches_type
from onebusaway.types import RoutesForLocationListResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestRoutesForLocation:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_list(self, client: OnebusawaySDK) -> None:
        routes_for_location = client.routes_for_location.list(
            lat=0,
            lon=0,
        )
        assert_matches_type(RoutesForLocationListResponse, routes_for_location, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: OnebusawaySDK) -> None:
        routes_for_location = client.routes_for_location.list(
            lat=0,
            lon=0,
            lat_span=0,
            lon_span=0,
            query="query",
            radius=0,
        )
        assert_matches_type(RoutesForLocationListResponse, routes_for_location, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: OnebusawaySDK) -> None:
        response = client.routes_for_location.with_raw_response.list(
            lat=0,
            lon=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        routes_for_location = response.parse()
        assert_matches_type(RoutesForLocationListResponse, routes_for_location, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: OnebusawaySDK) -> None:
        with client.routes_for_location.with_streaming_response.list(
            lat=0,
            lon=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            routes_for_location = response.parse()
            assert_matches_type(RoutesForLocationListResponse, routes_for_location, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncRoutesForLocation:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_list(self, async_client: AsyncOnebusawaySDK) -> None:
        routes_for_location = await async_client.routes_for_location.list(
            lat=0,
            lon=0,
        )
        assert_matches_type(RoutesForLocationListResponse, routes_for_location, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncOnebusawaySDK) -> None:
        routes_for_location = await async_client.routes_for_location.list(
            lat=0,
            lon=0,
            lat_span=0,
            lon_span=0,
            query="query",
            radius=0,
        )
        assert_matches_type(RoutesForLocationListResponse, routes_for_location, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncOnebusawaySDK) -> None:
        response = await async_client.routes_for_location.with_raw_response.list(
            lat=0,
            lon=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        routes_for_location = await response.parse()
        assert_matches_type(RoutesForLocationListResponse, routes_for_location, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncOnebusawaySDK) -> None:
        async with async_client.routes_for_location.with_streaming_response.list(
            lat=0,
            lon=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            routes_for_location = await response.parse()
            assert_matches_type(RoutesForLocationListResponse, routes_for_location, path=["response"])

        assert cast(Any, response.is_closed) is True
