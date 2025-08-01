# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from onebusaway import OnebusawaySDK, AsyncOnebusawaySDK
from tests.utils import assert_matches_type
from onebusaway.types import SearchForRouteListResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestSearchForRoute:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_list(self, client: OnebusawaySDK) -> None:
        search_for_route = client.search_for_route.list(
            input="input",
        )
        assert_matches_type(SearchForRouteListResponse, search_for_route, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: OnebusawaySDK) -> None:
        search_for_route = client.search_for_route.list(
            input="input",
            max_count=0,
        )
        assert_matches_type(SearchForRouteListResponse, search_for_route, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: OnebusawaySDK) -> None:
        response = client.search_for_route.with_raw_response.list(
            input="input",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        search_for_route = response.parse()
        assert_matches_type(SearchForRouteListResponse, search_for_route, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: OnebusawaySDK) -> None:
        with client.search_for_route.with_streaming_response.list(
            input="input",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            search_for_route = response.parse()
            assert_matches_type(SearchForRouteListResponse, search_for_route, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncSearchForRoute:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_list(self, async_client: AsyncOnebusawaySDK) -> None:
        search_for_route = await async_client.search_for_route.list(
            input="input",
        )
        assert_matches_type(SearchForRouteListResponse, search_for_route, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncOnebusawaySDK) -> None:
        search_for_route = await async_client.search_for_route.list(
            input="input",
            max_count=0,
        )
        assert_matches_type(SearchForRouteListResponse, search_for_route, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncOnebusawaySDK) -> None:
        response = await async_client.search_for_route.with_raw_response.list(
            input="input",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        search_for_route = await response.parse()
        assert_matches_type(SearchForRouteListResponse, search_for_route, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncOnebusawaySDK) -> None:
        async with async_client.search_for_route.with_streaming_response.list(
            input="input",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            search_for_route = await response.parse()
            assert_matches_type(SearchForRouteListResponse, search_for_route, path=["response"])

        assert cast(Any, response.is_closed) is True
