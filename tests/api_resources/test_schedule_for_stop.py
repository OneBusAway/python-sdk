# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from onebusaway import OnebusawaySDK, AsyncOnebusawaySDK
from tests.utils import assert_matches_type
from onebusaway.types import ScheduleForStopRetrieveResponse
from onebusaway._utils import parse_date

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestScheduleForStop:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_retrieve(self, client: OnebusawaySDK) -> None:
        schedule_for_stop = client.schedule_for_stop.retrieve(
            stop_id="stopID",
        )
        assert_matches_type(ScheduleForStopRetrieveResponse, schedule_for_stop, path=["response"])

    @parametrize
    def test_method_retrieve_with_all_params(self, client: OnebusawaySDK) -> None:
        schedule_for_stop = client.schedule_for_stop.retrieve(
            stop_id="stopID",
            date=parse_date("2019-12-27"),
        )
        assert_matches_type(ScheduleForStopRetrieveResponse, schedule_for_stop, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: OnebusawaySDK) -> None:
        response = client.schedule_for_stop.with_raw_response.retrieve(
            stop_id="stopID",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        schedule_for_stop = response.parse()
        assert_matches_type(ScheduleForStopRetrieveResponse, schedule_for_stop, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: OnebusawaySDK) -> None:
        with client.schedule_for_stop.with_streaming_response.retrieve(
            stop_id="stopID",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            schedule_for_stop = response.parse()
            assert_matches_type(ScheduleForStopRetrieveResponse, schedule_for_stop, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: OnebusawaySDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `stop_id` but received ''"):
            client.schedule_for_stop.with_raw_response.retrieve(
                stop_id="",
            )


class TestAsyncScheduleForStop:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncOnebusawaySDK) -> None:
        schedule_for_stop = await async_client.schedule_for_stop.retrieve(
            stop_id="stopID",
        )
        assert_matches_type(ScheduleForStopRetrieveResponse, schedule_for_stop, path=["response"])

    @parametrize
    async def test_method_retrieve_with_all_params(self, async_client: AsyncOnebusawaySDK) -> None:
        schedule_for_stop = await async_client.schedule_for_stop.retrieve(
            stop_id="stopID",
            date=parse_date("2019-12-27"),
        )
        assert_matches_type(ScheduleForStopRetrieveResponse, schedule_for_stop, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncOnebusawaySDK) -> None:
        response = await async_client.schedule_for_stop.with_raw_response.retrieve(
            stop_id="stopID",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        schedule_for_stop = await response.parse()
        assert_matches_type(ScheduleForStopRetrieveResponse, schedule_for_stop, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncOnebusawaySDK) -> None:
        async with async_client.schedule_for_stop.with_streaming_response.retrieve(
            stop_id="stopID",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            schedule_for_stop = await response.parse()
            assert_matches_type(ScheduleForStopRetrieveResponse, schedule_for_stop, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncOnebusawaySDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `stop_id` but received ''"):
            await async_client.schedule_for_stop.with_raw_response.retrieve(
                stop_id="",
            )
