# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from onebusaway import OnebusawaySDK, AsyncOnebusawaySDK
from tests.utils import assert_matches_type
from onebusaway.types import (
    ArrivalAndDepartureSearchForStopResponse,
    ArrivalAndDepartureSearchAllForStopResponse,
)
from onebusaway._utils import parse_datetime

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestArrivalAndDeparture:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_search_all_for_stop(self, client: OnebusawaySDK) -> None:
        arrival_and_departure = client.arrival_and_departure.search_all_for_stop(
            "string",
        )
        assert_matches_type(ArrivalAndDepartureSearchAllForStopResponse, arrival_and_departure, path=["response"])

    @parametrize
    def test_method_search_all_for_stop_with_all_params(self, client: OnebusawaySDK) -> None:
        arrival_and_departure = client.arrival_and_departure.search_all_for_stop(
            "string",
            minutes_after=0,
            minutes_before=0,
            time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(ArrivalAndDepartureSearchAllForStopResponse, arrival_and_departure, path=["response"])

    @parametrize
    def test_raw_response_search_all_for_stop(self, client: OnebusawaySDK) -> None:
        response = client.arrival_and_departure.with_raw_response.search_all_for_stop(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        arrival_and_departure = response.parse()
        assert_matches_type(ArrivalAndDepartureSearchAllForStopResponse, arrival_and_departure, path=["response"])

    @parametrize
    def test_streaming_response_search_all_for_stop(self, client: OnebusawaySDK) -> None:
        with client.arrival_and_departure.with_streaming_response.search_all_for_stop(
            "string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            arrival_and_departure = response.parse()
            assert_matches_type(ArrivalAndDepartureSearchAllForStopResponse, arrival_and_departure, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_search_all_for_stop(self, client: OnebusawaySDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `stop_id` but received ''"):
            client.arrival_and_departure.with_raw_response.search_all_for_stop(
                "",
            )

    @parametrize
    def test_method_search_for_stop(self, client: OnebusawaySDK) -> None:
        arrival_and_departure = client.arrival_and_departure.search_for_stop(
            "string",
            service_date=0,
            trip_id="string",
        )
        assert_matches_type(ArrivalAndDepartureSearchForStopResponse, arrival_and_departure, path=["response"])

    @parametrize
    def test_method_search_for_stop_with_all_params(self, client: OnebusawaySDK) -> None:
        arrival_and_departure = client.arrival_and_departure.search_for_stop(
            "string",
            service_date=0,
            trip_id="string",
            stop_sequence=0,
            time=0,
            vehicle_id="string",
        )
        assert_matches_type(ArrivalAndDepartureSearchForStopResponse, arrival_and_departure, path=["response"])

    @parametrize
    def test_raw_response_search_for_stop(self, client: OnebusawaySDK) -> None:
        response = client.arrival_and_departure.with_raw_response.search_for_stop(
            "string",
            service_date=0,
            trip_id="string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        arrival_and_departure = response.parse()
        assert_matches_type(ArrivalAndDepartureSearchForStopResponse, arrival_and_departure, path=["response"])

    @parametrize
    def test_streaming_response_search_for_stop(self, client: OnebusawaySDK) -> None:
        with client.arrival_and_departure.with_streaming_response.search_for_stop(
            "string",
            service_date=0,
            trip_id="string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            arrival_and_departure = response.parse()
            assert_matches_type(ArrivalAndDepartureSearchForStopResponse, arrival_and_departure, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_search_for_stop(self, client: OnebusawaySDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `stop_id` but received ''"):
            client.arrival_and_departure.with_raw_response.search_for_stop(
                "",
                service_date=0,
                trip_id="string",
            )


class TestAsyncArrivalAndDeparture:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_search_all_for_stop(self, async_client: AsyncOnebusawaySDK) -> None:
        arrival_and_departure = await async_client.arrival_and_departure.search_all_for_stop(
            "string",
        )
        assert_matches_type(ArrivalAndDepartureSearchAllForStopResponse, arrival_and_departure, path=["response"])

    @parametrize
    async def test_method_search_all_for_stop_with_all_params(self, async_client: AsyncOnebusawaySDK) -> None:
        arrival_and_departure = await async_client.arrival_and_departure.search_all_for_stop(
            "string",
            minutes_after=0,
            minutes_before=0,
            time=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert_matches_type(ArrivalAndDepartureSearchAllForStopResponse, arrival_and_departure, path=["response"])

    @parametrize
    async def test_raw_response_search_all_for_stop(self, async_client: AsyncOnebusawaySDK) -> None:
        response = await async_client.arrival_and_departure.with_raw_response.search_all_for_stop(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        arrival_and_departure = await response.parse()
        assert_matches_type(ArrivalAndDepartureSearchAllForStopResponse, arrival_and_departure, path=["response"])

    @parametrize
    async def test_streaming_response_search_all_for_stop(self, async_client: AsyncOnebusawaySDK) -> None:
        async with async_client.arrival_and_departure.with_streaming_response.search_all_for_stop(
            "string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            arrival_and_departure = await response.parse()
            assert_matches_type(ArrivalAndDepartureSearchAllForStopResponse, arrival_and_departure, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_search_all_for_stop(self, async_client: AsyncOnebusawaySDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `stop_id` but received ''"):
            await async_client.arrival_and_departure.with_raw_response.search_all_for_stop(
                "",
            )

    @parametrize
    async def test_method_search_for_stop(self, async_client: AsyncOnebusawaySDK) -> None:
        arrival_and_departure = await async_client.arrival_and_departure.search_for_stop(
            "string",
            service_date=0,
            trip_id="string",
        )
        assert_matches_type(ArrivalAndDepartureSearchForStopResponse, arrival_and_departure, path=["response"])

    @parametrize
    async def test_method_search_for_stop_with_all_params(self, async_client: AsyncOnebusawaySDK) -> None:
        arrival_and_departure = await async_client.arrival_and_departure.search_for_stop(
            "string",
            service_date=0,
            trip_id="string",
            stop_sequence=0,
            time=0,
            vehicle_id="string",
        )
        assert_matches_type(ArrivalAndDepartureSearchForStopResponse, arrival_and_departure, path=["response"])

    @parametrize
    async def test_raw_response_search_for_stop(self, async_client: AsyncOnebusawaySDK) -> None:
        response = await async_client.arrival_and_departure.with_raw_response.search_for_stop(
            "string",
            service_date=0,
            trip_id="string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        arrival_and_departure = await response.parse()
        assert_matches_type(ArrivalAndDepartureSearchForStopResponse, arrival_and_departure, path=["response"])

    @parametrize
    async def test_streaming_response_search_for_stop(self, async_client: AsyncOnebusawaySDK) -> None:
        async with async_client.arrival_and_departure.with_streaming_response.search_for_stop(
            "string",
            service_date=0,
            trip_id="string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            arrival_and_departure = await response.parse()
            assert_matches_type(ArrivalAndDepartureSearchForStopResponse, arrival_and_departure, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_search_for_stop(self, async_client: AsyncOnebusawaySDK) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `stop_id` but received ''"):
            await async_client.arrival_and_departure.with_raw_response.search_for_stop(
                "",
                service_date=0,
                trip_id="string",
            )
