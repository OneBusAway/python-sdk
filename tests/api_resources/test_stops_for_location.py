# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from open_transit import OpenTransit, AsyncOpenTransit

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestStopsForLocation:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_list(self, client: OpenTransit) -> None:
        stops_for_location = client.stops_for_location.list()
        assert stops_for_location is None

    @parametrize
    def test_method_list_with_all_params(self, client: OpenTransit) -> None:
        stops_for_location = client.stops_for_location.list(
            key="string",
            lat=0,
            lon=0,
        )
        assert stops_for_location is None

    @parametrize
    def test_raw_response_list(self, client: OpenTransit) -> None:
        response = client.stops_for_location.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        stops_for_location = response.parse()
        assert stops_for_location is None

    @parametrize
    def test_streaming_response_list(self, client: OpenTransit) -> None:
        with client.stops_for_location.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            stops_for_location = response.parse()
            assert stops_for_location is None

        assert cast(Any, response.is_closed) is True


class TestAsyncStopsForLocation:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_list(self, async_client: AsyncOpenTransit) -> None:
        stops_for_location = await async_client.stops_for_location.list()
        assert stops_for_location is None

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncOpenTransit) -> None:
        stops_for_location = await async_client.stops_for_location.list(
            key="string",
            lat=0,
            lon=0,
        )
        assert stops_for_location is None

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncOpenTransit) -> None:
        response = await async_client.stops_for_location.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        stops_for_location = await response.parse()
        assert stops_for_location is None

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncOpenTransit) -> None:
        async with async_client.stops_for_location.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            stops_for_location = await response.parse()
            assert stops_for_location is None

        assert cast(Any, response.is_closed) is True
