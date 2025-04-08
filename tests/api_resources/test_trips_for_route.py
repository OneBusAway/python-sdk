# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from onebusaway import OnebusawaySDK, AsyncOnebusawaySDK
from tests.utils import assert_matches_type
from onebusaway.types import TripsForRouteListResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestTripsForRoute:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_list(self, client: OnebusawaySDK) -> None:
        trips_for_route = client.trips_for_route.list(
            route_id="routeID",
        )
        assert_matches_type(TripsForRouteListResponse, trips_for_route, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: OnebusawaySDK) -> None:
        trips_for_route = client.trips_for_route.list(
            route_id="routeID",
            include_schedule=True,
            include_status=True,
            time=0,
        )
        assert_matches_type(TripsForRouteListResponse, trips_for_route, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: OnebusawaySDK) -> None:
        response = client.trips_for_route.with_raw_response.list(
            route_id="routeID",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        trips_for_route = response.parse()
        assert_matches_type(TripsForRouteListResponse, trips_for_route, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: OnebusawaySDK) -> None:
        with client.trips_for_route.with_streaming_response.list(
            route_id="routeID",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            trips_for_route = response.parse()
            assert_matches_type(TripsForRouteListResponse, trips_for_route, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_list(self, client: OnebusawaySDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `route_id` but received ''"):
            client.trips_for_route.with_raw_response.list(
                route_id="",
            )


class TestAsyncTripsForRoute:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_list(self, async_client: AsyncOnebusawaySDK) -> None:
        trips_for_route = await async_client.trips_for_route.list(
            route_id="routeID",
        )
        assert_matches_type(TripsForRouteListResponse, trips_for_route, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncOnebusawaySDK) -> None:
        trips_for_route = await async_client.trips_for_route.list(
            route_id="routeID",
            include_schedule=True,
            include_status=True,
            time=0,
        )
        assert_matches_type(TripsForRouteListResponse, trips_for_route, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncOnebusawaySDK) -> None:
        response = await async_client.trips_for_route.with_raw_response.list(
            route_id="routeID",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        trips_for_route = await response.parse()
        assert_matches_type(TripsForRouteListResponse, trips_for_route, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncOnebusawaySDK) -> None:
        async with async_client.trips_for_route.with_streaming_response.list(
            route_id="routeID",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            trips_for_route = await response.parse()
            assert_matches_type(TripsForRouteListResponse, trips_for_route, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_list(self, async_client: AsyncOnebusawaySDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `route_id` but received ''"):
            await async_client.trips_for_route.with_raw_response.list(
                route_id="",
            )
