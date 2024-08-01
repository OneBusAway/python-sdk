# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel
from .shared.references import References
from .shared.response_wrapper import ResponseWrapper

__all__ = [
    "ConfigRetrieveResponse",
    "ConfigRetrieveResponseData",
    "ConfigRetrieveResponseDataEntry",
    "ConfigRetrieveResponseDataEntryGitProperties",
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


class ConfigRetrieveResponseData(BaseModel):
    entry: ConfigRetrieveResponseDataEntry

    references: References


class ConfigRetrieveResponse(ResponseWrapper):
    data: ConfigRetrieveResponseData
