# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel
from .shared.references import References
from .shared.response_wrapper import ResponseWrapper

__all__ = [
    "BlockRetrieveResponse",
    "BlockRetrieveResponseData",
    "BlockRetrieveResponseDataEntry",
    "BlockRetrieveResponseDataEntryConfiguration",
    "BlockRetrieveResponseDataEntryConfigurationTrip",
    "BlockRetrieveResponseDataEntryConfigurationTripBlockStopTime",
    "BlockRetrieveResponseDataEntryConfigurationTripBlockStopTimeStopTime",
]


class BlockRetrieveResponseDataEntryConfigurationTripBlockStopTimeStopTime(BaseModel):
    arrival_time: int = FieldInfo(alias="arrivalTime")

    departure_time: int = FieldInfo(alias="departureTime")

    stop_id: str = FieldInfo(alias="stopId")

    drop_off_type: Optional[int] = FieldInfo(alias="dropOffType", default=None)

    pickup_type: Optional[int] = FieldInfo(alias="pickupType", default=None)


class BlockRetrieveResponseDataEntryConfigurationTripBlockStopTime(BaseModel):
    accumulated_slack_time: float = FieldInfo(alias="accumulatedSlackTime")

    block_sequence: int = FieldInfo(alias="blockSequence")

    distance_along_block: float = FieldInfo(alias="distanceAlongBlock")

    stop_time: BlockRetrieveResponseDataEntryConfigurationTripBlockStopTimeStopTime = FieldInfo(alias="stopTime")


class BlockRetrieveResponseDataEntryConfigurationTrip(BaseModel):
    accumulated_slack_time: float = FieldInfo(alias="accumulatedSlackTime")

    block_stop_times: List[BlockRetrieveResponseDataEntryConfigurationTripBlockStopTime] = FieldInfo(
        alias="blockStopTimes"
    )

    distance_along_block: float = FieldInfo(alias="distanceAlongBlock")

    trip_id: str = FieldInfo(alias="tripId")


class BlockRetrieveResponseDataEntryConfiguration(BaseModel):
    active_service_ids: List[str] = FieldInfo(alias="activeServiceIds")

    trips: List[BlockRetrieveResponseDataEntryConfigurationTrip]

    inactive_service_ids: Optional[List[str]] = FieldInfo(alias="inactiveServiceIds", default=None)


class BlockRetrieveResponseDataEntry(BaseModel):
    id: str

    configurations: List[BlockRetrieveResponseDataEntryConfiguration]


class BlockRetrieveResponseData(BaseModel):
    entry: BlockRetrieveResponseDataEntry

    references: References


class BlockRetrieveResponse(ResponseWrapper):
    data: BlockRetrieveResponseData
