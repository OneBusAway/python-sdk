# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from open_transit import OneBusAway, AsyncOneBusAway
from open_transit.types.api.where import AgenciesWithCoverageListResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestAgenciesWithCoverage:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_list(self, client: OneBusAway) -> None:
        agencies_with_coverage = client.api.where.agencies_with_coverage.list()
        assert_matches_type(AgenciesWithCoverageListResponse, agencies_with_coverage, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: OneBusAway) -> None:
        response = client.api.where.agencies_with_coverage.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        agencies_with_coverage = response.parse()
        assert_matches_type(AgenciesWithCoverageListResponse, agencies_with_coverage, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: OneBusAway) -> None:
        with client.api.where.agencies_with_coverage.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            agencies_with_coverage = response.parse()
            assert_matches_type(AgenciesWithCoverageListResponse, agencies_with_coverage, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncAgenciesWithCoverage:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_list(self, async_client: AsyncOneBusAway) -> None:
        agencies_with_coverage = await async_client.api.where.agencies_with_coverage.list()
        assert_matches_type(AgenciesWithCoverageListResponse, agencies_with_coverage, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncOneBusAway) -> None:
        response = await async_client.api.where.agencies_with_coverage.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        agencies_with_coverage = await response.parse()
        assert_matches_type(AgenciesWithCoverageListResponse, agencies_with_coverage, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncOneBusAway) -> None:
        async with async_client.api.where.agencies_with_coverage.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            agencies_with_coverage = await response.parse()
            assert_matches_type(AgenciesWithCoverageListResponse, agencies_with_coverage, path=["response"])

        assert cast(Any, response.is_closed) is True