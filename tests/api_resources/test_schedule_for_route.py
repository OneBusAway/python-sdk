# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from onebusaway import OnebusawaySDK, AsyncOnebusawaySDK
from tests.utils import assert_matches_type
from onebusaway.types import ScheduleForRouteRetrieveResponse
from onebusaway._utils import parse_date

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestScheduleForRoute:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_retrieve(self, client: OnebusawaySDK) -> None:
        schedule_for_route = client.schedule_for_route.retrieve(
            route_id="1_100223",
        )
        assert_matches_type(ScheduleForRouteRetrieveResponse, schedule_for_route, path=["response"])

    @parametrize
    def test_method_retrieve_with_all_params(self, client: OnebusawaySDK) -> None:
        schedule_for_route = client.schedule_for_route.retrieve(
            route_id="1_100223",
            date=parse_date("2019-12-27"),
        )
        assert_matches_type(ScheduleForRouteRetrieveResponse, schedule_for_route, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: OnebusawaySDK) -> None:
        response = client.schedule_for_route.with_raw_response.retrieve(
            route_id="1_100223",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        schedule_for_route = response.parse()
        assert_matches_type(ScheduleForRouteRetrieveResponse, schedule_for_route, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: OnebusawaySDK) -> None:
        with client.schedule_for_route.with_streaming_response.retrieve(
            route_id="1_100223",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            schedule_for_route = response.parse()
            assert_matches_type(ScheduleForRouteRetrieveResponse, schedule_for_route, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: OnebusawaySDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `route_id` but received ''"):
            client.schedule_for_route.with_raw_response.retrieve(
                route_id="",
            )


class TestAsyncScheduleForRoute:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncOnebusawaySDK) -> None:
        schedule_for_route = await async_client.schedule_for_route.retrieve(
            route_id="1_100223",
        )
        assert_matches_type(ScheduleForRouteRetrieveResponse, schedule_for_route, path=["response"])

    @parametrize
    async def test_method_retrieve_with_all_params(self, async_client: AsyncOnebusawaySDK) -> None:
        schedule_for_route = await async_client.schedule_for_route.retrieve(
            route_id="1_100223",
            date=parse_date("2019-12-27"),
        )
        assert_matches_type(ScheduleForRouteRetrieveResponse, schedule_for_route, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncOnebusawaySDK) -> None:
        response = await async_client.schedule_for_route.with_raw_response.retrieve(
            route_id="1_100223",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        schedule_for_route = await response.parse()
        assert_matches_type(ScheduleForRouteRetrieveResponse, schedule_for_route, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncOnebusawaySDK) -> None:
        async with async_client.schedule_for_route.with_streaming_response.retrieve(
            route_id="1_100223",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            schedule_for_route = await response.parse()
            assert_matches_type(ScheduleForRouteRetrieveResponse, schedule_for_route, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncOnebusawaySDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `route_id` but received ''"):
            await async_client.schedule_for_route.with_raw_response.retrieve(
                route_id="",
            )
