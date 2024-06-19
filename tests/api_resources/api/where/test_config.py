# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from open_transit import OneBusAway, AsyncOneBusAway
from open_transit.types.api.where import ConfigRetrieveResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestConfig:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_retrieve(self, client: OneBusAway) -> None:
        config = client.api.where.config.retrieve()
        assert_matches_type(ConfigRetrieveResponse, config, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: OneBusAway) -> None:
        response = client.api.where.config.with_raw_response.retrieve()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        config = response.parse()
        assert_matches_type(ConfigRetrieveResponse, config, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: OneBusAway) -> None:
        with client.api.where.config.with_streaming_response.retrieve() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            config = response.parse()
            assert_matches_type(ConfigRetrieveResponse, config, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncConfig:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncOneBusAway) -> None:
        config = await async_client.api.where.config.retrieve()
        assert_matches_type(ConfigRetrieveResponse, config, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncOneBusAway) -> None:
        response = await async_client.api.where.config.with_raw_response.retrieve()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        config = await response.parse()
        assert_matches_type(ConfigRetrieveResponse, config, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncOneBusAway) -> None:
        async with async_client.api.where.config.with_streaming_response.retrieve() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            config = await response.parse()
            assert_matches_type(ConfigRetrieveResponse, config, path=["response"])

        assert cast(Any, response.is_closed) is True