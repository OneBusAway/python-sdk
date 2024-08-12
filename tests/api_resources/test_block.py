# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from onebusaway import OnebusawaySDK, AsyncOnebusawaySDK
from tests.utils import assert_matches_type
from onebusaway.types import BlockRetrieveResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestBlock:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_retrieve(self, client: OnebusawaySDK) -> None:
        block = client.block.retrieve(
            "blockID",
        )
        assert_matches_type(BlockRetrieveResponse, block, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: OnebusawaySDK) -> None:
        response = client.block.with_raw_response.retrieve(
            "blockID",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        block = response.parse()
        assert_matches_type(BlockRetrieveResponse, block, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: OnebusawaySDK) -> None:
        with client.block.with_streaming_response.retrieve(
            "blockID",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            block = response.parse()
            assert_matches_type(BlockRetrieveResponse, block, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: OnebusawaySDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `block_id` but received ''"):
            client.block.with_raw_response.retrieve(
                "",
            )


class TestAsyncBlock:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncOnebusawaySDK) -> None:
        block = await async_client.block.retrieve(
            "blockID",
        )
        assert_matches_type(BlockRetrieveResponse, block, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncOnebusawaySDK) -> None:
        response = await async_client.block.with_raw_response.retrieve(
            "blockID",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        block = await response.parse()
        assert_matches_type(BlockRetrieveResponse, block, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncOnebusawaySDK) -> None:
        async with async_client.block.with_streaming_response.retrieve(
            "blockID",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            block = await response.parse()
            assert_matches_type(BlockRetrieveResponse, block, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncOnebusawaySDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `block_id` but received ''"):
            await async_client.block.with_raw_response.retrieve(
                "",
            )
