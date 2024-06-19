# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from ...._models import BaseModel
from ...shared.response_wrapper import ResponseWrapper

__all__ = [
    "ConfigRetrieveResponse",
    "ConfigRetrieveResponseData",
    "ConfigRetrieveResponseDataEntry",
    "ConfigRetrieveResponseDataEntryGitProperties",
    "ConfigRetrieveResponseDataReferences",
    "ConfigRetrieveResponseDataReferencesAgency",
    "ConfigRetrieveResponseDataReferencesRoute",
    "ConfigRetrieveResponseDataReferencesStop",
    "ConfigRetrieveResponseDataReferencesTrip",
]


class ConfigRetrieveResponseDataEntryGitProperties(BaseModel):
    git_branch: Optional[str] = FieldInfo(alias="git.branch", default=None)

    git_build_host: Optional[str] = FieldInfo(alias="git.build.host", default=None)

    git_build_time: Optional[str] = FieldInfo(alias="git.build.time", default=None)

    git_build_user_email: Optional[str] = FieldInfo(alias="git.build.user.email", default=None)

    git_build_user_name: Optional[str] = FieldInfo(alias="git.build.user.name", default=None)

    git_build_version: Optional[str] = FieldInfo(alias="git.build.version", default=None)

    git_closest_tag_commit_count: Optional[str] = FieldInfo(alias="git.closest.tag.commit.count", default=None)

    git_closest_tag_name: Optional[str] = FieldInfo(alias="git.closest.tag.name", default=None)

    git_commit_id: Optional[str] = FieldInfo(alias="git.commit.id", default=None)

    git_commit_id_abbrev: Optional[str] = FieldInfo(alias="git.commit.id.abbrev", default=None)

    git_commit_id_describe: Optional[str] = FieldInfo(alias="git.commit.id.describe", default=None)

    git_commit_id_describe_short: Optional[str] = FieldInfo(alias="git.commit.id.describe-short", default=None)

    git_commit_message_full: Optional[str] = FieldInfo(alias="git.commit.message.full", default=None)

    git_commit_message_short: Optional[str] = FieldInfo(alias="git.commit.message.short", default=None)

    git_commit_time: Optional[str] = FieldInfo(alias="git.commit.time", default=None)

    git_commit_user_email: Optional[str] = FieldInfo(alias="git.commit.user.email", default=None)

    git_commit_user_name: Optional[str] = FieldInfo(alias="git.commit.user.name", default=None)

    git_dirty: Optional[str] = FieldInfo(alias="git.dirty", default=None)

    git_remote_origin_url: Optional[str] = FieldInfo(alias="git.remote.origin.url", default=None)

    git_tags: Optional[str] = FieldInfo(alias="git.tags", default=None)


class ConfigRetrieveResponseDataEntry(BaseModel):
    id: Optional[str] = None

    git_properties: Optional[ConfigRetrieveResponseDataEntryGitProperties] = FieldInfo(
        alias="gitProperties", default=None
    )

    name: Optional[str] = None

    service_date_from: Optional[str] = FieldInfo(alias="serviceDateFrom", default=None)

    service_date_to: Optional[str] = FieldInfo(alias="serviceDateTo", default=None)


class ConfigRetrieveResponseDataReferencesAgency(BaseModel):
    id: str

    name: str

    timezone: str

    url: str

    disclaimer: Optional[str] = None

    email: Optional[str] = None

    fare_url: Optional[str] = FieldInfo(alias="fareUrl", default=None)

    lang: Optional[str] = None

    phone: Optional[str] = None

    private_service: Optional[bool] = FieldInfo(alias="privateService", default=None)


class ConfigRetrieveResponseDataReferencesRoute(BaseModel):
    id: Optional[str] = None

    agency_id: Optional[str] = FieldInfo(alias="agencyId", default=None)

    color: Optional[str] = None

    description: Optional[str] = None

    long_name: Optional[str] = FieldInfo(alias="longName", default=None)

    null_safe_short_name: Optional[str] = FieldInfo(alias="nullSafeShortName", default=None)

    short_name: Optional[str] = FieldInfo(alias="shortName", default=None)

    text_color: Optional[str] = FieldInfo(alias="textColor", default=None)

    type: Optional[int] = None

    url: Optional[str] = None


class ConfigRetrieveResponseDataReferencesStop(BaseModel):
    id: str

    code: str

    lat: float

    lon: float

    name: str

    direction: Optional[str] = None

    location_type: Optional[int] = FieldInfo(alias="locationType", default=None)

    parent: Optional[str] = None

    route_ids: Optional[List[str]] = FieldInfo(alias="routeIds", default=None)

    static_route_ids: Optional[List[str]] = FieldInfo(alias="staticRouteIds", default=None)

    wheelchair_boarding: Optional[str] = FieldInfo(alias="wheelchairBoarding", default=None)


class ConfigRetrieveResponseDataReferencesTrip(BaseModel):
    id: str

    route_id: str = FieldInfo(alias="routeId")

    block_id: Optional[str] = FieldInfo(alias="blockId", default=None)

    direction_id: Optional[str] = FieldInfo(alias="directionId", default=None)

    peak_offpeak: Optional[int] = FieldInfo(alias="peakOffpeak", default=None)

    route_short_name: Optional[str] = FieldInfo(alias="routeShortName", default=None)

    service_id: Optional[str] = FieldInfo(alias="serviceId", default=None)

    shape_id: Optional[str] = FieldInfo(alias="shapeId", default=None)

    time_zone: Optional[str] = FieldInfo(alias="timeZone", default=None)

    trip_headsign: Optional[str] = FieldInfo(alias="tripHeadsign", default=None)

    trip_short_name: Optional[str] = FieldInfo(alias="tripShortName", default=None)


class ConfigRetrieveResponseDataReferences(BaseModel):
    agencies: Optional[List[ConfigRetrieveResponseDataReferencesAgency]] = None

    routes: Optional[List[ConfigRetrieveResponseDataReferencesRoute]] = None

    situations: Optional[List[object]] = None

    stops: Optional[List[ConfigRetrieveResponseDataReferencesStop]] = None

    stop_times: Optional[List[object]] = FieldInfo(alias="stopTimes", default=None)

    trips: Optional[List[ConfigRetrieveResponseDataReferencesTrip]] = None


class ConfigRetrieveResponseData(BaseModel):
    entry: Optional[ConfigRetrieveResponseDataEntry] = None

    references: Optional[ConfigRetrieveResponseDataReferences] = None


class ConfigRetrieveResponse(ResponseWrapper):
    data: Optional[ConfigRetrieveResponseData] = None
