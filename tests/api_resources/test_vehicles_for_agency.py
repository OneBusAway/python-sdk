# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from onebusaway import OnebusawaySDK, AsyncOnebusawaySDK
from tests.utils import assert_matches_type
from onebusaway.types import VehiclesForAgencyListResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestVehiclesForAgency:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_list(self, client: OnebusawaySDK) -> None:
        vehicles_for_agency = client.vehicles_for_agency.list(
            agency_id="agencyID",
        )
        assert_matches_type(VehiclesForAgencyListResponse, vehicles_for_agency, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: OnebusawaySDK) -> None:
        vehicles_for_agency = client.vehicles_for_agency.list(
            agency_id="agencyID",
            time="time",
        )
        assert_matches_type(VehiclesForAgencyListResponse, vehicles_for_agency, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: OnebusawaySDK) -> None:
        response = client.vehicles_for_agency.with_raw_response.list(
            agency_id="agencyID",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        vehicles_for_agency = response.parse()
        assert_matches_type(VehiclesForAgencyListResponse, vehicles_for_agency, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: OnebusawaySDK) -> None:
        with client.vehicles_for_agency.with_streaming_response.list(
            agency_id="agencyID",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            vehicles_for_agency = response.parse()
            assert_matches_type(VehiclesForAgencyListResponse, vehicles_for_agency, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_list(self, client: OnebusawaySDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agency_id` but received ''"):
            client.vehicles_for_agency.with_raw_response.list(
                agency_id="",
            )


class TestAsyncVehiclesForAgency:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_list(self, async_client: AsyncOnebusawaySDK) -> None:
        vehicles_for_agency = await async_client.vehicles_for_agency.list(
            agency_id="agencyID",
        )
        assert_matches_type(VehiclesForAgencyListResponse, vehicles_for_agency, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncOnebusawaySDK) -> None:
        vehicles_for_agency = await async_client.vehicles_for_agency.list(
            agency_id="agencyID",
            time="time",
        )
        assert_matches_type(VehiclesForAgencyListResponse, vehicles_for_agency, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncOnebusawaySDK) -> None:
        response = await async_client.vehicles_for_agency.with_raw_response.list(
            agency_id="agencyID",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        vehicles_for_agency = await response.parse()
        assert_matches_type(VehiclesForAgencyListResponse, vehicles_for_agency, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncOnebusawaySDK) -> None:
        async with async_client.vehicles_for_agency.with_streaming_response.list(
            agency_id="agencyID",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            vehicles_for_agency = await response.parse()
            assert_matches_type(VehiclesForAgencyListResponse, vehicles_for_agency, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_list(self, async_client: AsyncOnebusawaySDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agency_id` but received ''"):
            await async_client.vehicles_for_agency.with_raw_response.list(
                agency_id="",
            )
