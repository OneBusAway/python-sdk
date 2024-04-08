# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from open_transit import OpenTransit, AsyncOpenTransit

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestConfig:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_retrieve(self, client: OpenTransit) -> None:
        config = client.config.retrieve()
        assert config is None

    @parametrize
    def test_method_retrieve_with_all_params(self, client: OpenTransit) -> None:
        config = client.config.retrieve(
            key="string",
        )
        assert config is None

    @parametrize
    def test_raw_response_retrieve(self, client: OpenTransit) -> None:
        response = client.config.with_raw_response.retrieve()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        config = response.parse()
        assert config is None

    @parametrize
    def test_streaming_response_retrieve(self, client: OpenTransit) -> None:
        with client.config.with_streaming_response.retrieve() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            config = response.parse()
            assert config is None

        assert cast(Any, response.is_closed) is True


class TestAsyncConfig:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncOpenTransit) -> None:
        config = await async_client.config.retrieve()
        assert config is None

    @parametrize
    async def test_method_retrieve_with_all_params(self, async_client: AsyncOpenTransit) -> None:
        config = await async_client.config.retrieve(
            key="string",
        )
        assert config is None

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncOpenTransit) -> None:
        response = await async_client.config.with_raw_response.retrieve()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        config = await response.parse()
        assert config is None

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncOpenTransit) -> None:
        async with async_client.config.with_streaming_response.retrieve() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            config = await response.parse()
            assert config is None

        assert cast(Any, response.is_closed) is True
