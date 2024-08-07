# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from onebusaway import OnebusawaySDK, AsyncOnebusawaySDK
from tests.utils import assert_matches_type
from onebusaway.types import RoutesForAgencyListResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestRoutesForAgency:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_list(self, client: OnebusawaySDK) -> None:
        routes_for_agency = client.routes_for_agency.list(
            "agencyID",
        )
        assert_matches_type(RoutesForAgencyListResponse, routes_for_agency, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: OnebusawaySDK) -> None:
        response = client.routes_for_agency.with_raw_response.list(
            "agencyID",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        routes_for_agency = response.parse()
        assert_matches_type(RoutesForAgencyListResponse, routes_for_agency, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: OnebusawaySDK) -> None:
        with client.routes_for_agency.with_streaming_response.list(
            "agencyID",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            routes_for_agency = response.parse()
            assert_matches_type(RoutesForAgencyListResponse, routes_for_agency, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_list(self, client: OnebusawaySDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agency_id` but received ''"):
            client.routes_for_agency.with_raw_response.list(
                "",
            )


class TestAsyncRoutesForAgency:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_list(self, async_client: AsyncOnebusawaySDK) -> None:
        routes_for_agency = await async_client.routes_for_agency.list(
            "agencyID",
        )
        assert_matches_type(RoutesForAgencyListResponse, routes_for_agency, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncOnebusawaySDK) -> None:
        response = await async_client.routes_for_agency.with_raw_response.list(
            "agencyID",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        routes_for_agency = await response.parse()
        assert_matches_type(RoutesForAgencyListResponse, routes_for_agency, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncOnebusawaySDK) -> None:
        async with async_client.routes_for_agency.with_streaming_response.list(
            "agencyID",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            routes_for_agency = await response.parse()
            assert_matches_type(RoutesForAgencyListResponse, routes_for_agency, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_list(self, async_client: AsyncOnebusawaySDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agency_id` but received ''"):
            await async_client.routes_for_agency.with_raw_response.list(
                "",
            )
