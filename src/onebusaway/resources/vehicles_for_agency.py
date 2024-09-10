# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..types import vehicles_for_agency_list_params
from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from .._utils import (
    maybe_transform,
    async_maybe_transform,
)
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.vehicles_for_agency_list_response import VehiclesForAgencyListResponse

__all__ = ["VehiclesForAgencyResource", "AsyncVehiclesForAgencyResource"]


class VehiclesForAgencyResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> VehiclesForAgencyResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/OneBusAway/python-sdk#accessing-raw-response-data-eg-headers
        """
        return VehiclesForAgencyResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> VehiclesForAgencyResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/OneBusAway/python-sdk#with_streaming_response
        """
        return VehiclesForAgencyResourceWithStreamingResponse(self)

    def list(
        self,
        agency_id: str,
        *,
        time: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> VehiclesForAgencyListResponse:
        """
        Get vehicles for a specific agency

        Args:
          time: Specific time for querying the status (timestamp format)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not agency_id:
            raise ValueError(f"Expected a non-empty value for `agency_id` but received {agency_id!r}")
        return self._get(
            f"/api/where/vehicles-for-agency/{agency_id}.json",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"time": time}, vehicles_for_agency_list_params.VehiclesForAgencyListParams),
            ),
            cast_to=VehiclesForAgencyListResponse,
        )


class AsyncVehiclesForAgencyResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncVehiclesForAgencyResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/OneBusAway/python-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncVehiclesForAgencyResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncVehiclesForAgencyResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/OneBusAway/python-sdk#with_streaming_response
        """
        return AsyncVehiclesForAgencyResourceWithStreamingResponse(self)

    async def list(
        self,
        agency_id: str,
        *,
        time: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> VehiclesForAgencyListResponse:
        """
        Get vehicles for a specific agency

        Args:
          time: Specific time for querying the status (timestamp format)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not agency_id:
            raise ValueError(f"Expected a non-empty value for `agency_id` but received {agency_id!r}")
        return await self._get(
            f"/api/where/vehicles-for-agency/{agency_id}.json",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"time": time}, vehicles_for_agency_list_params.VehiclesForAgencyListParams
                ),
            ),
            cast_to=VehiclesForAgencyListResponse,
        )


class VehiclesForAgencyResourceWithRawResponse:
    def __init__(self, vehicles_for_agency: VehiclesForAgencyResource) -> None:
        self._vehicles_for_agency = vehicles_for_agency

        self.list = to_raw_response_wrapper(
            vehicles_for_agency.list,
        )


class AsyncVehiclesForAgencyResourceWithRawResponse:
    def __init__(self, vehicles_for_agency: AsyncVehiclesForAgencyResource) -> None:
        self._vehicles_for_agency = vehicles_for_agency

        self.list = async_to_raw_response_wrapper(
            vehicles_for_agency.list,
        )


class VehiclesForAgencyResourceWithStreamingResponse:
    def __init__(self, vehicles_for_agency: VehiclesForAgencyResource) -> None:
        self._vehicles_for_agency = vehicles_for_agency

        self.list = to_streamed_response_wrapper(
            vehicles_for_agency.list,
        )


class AsyncVehiclesForAgencyResourceWithStreamingResponse:
    def __init__(self, vehicles_for_agency: AsyncVehiclesForAgencyResource) -> None:
        self._vehicles_for_agency = vehicles_for_agency

        self.list = async_to_streamed_response_wrapper(
            vehicles_for_agency.list,
        )
