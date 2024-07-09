# coding: utf-8

"""
    Modelmetry API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from modelmetry.openapi.models.payload import Payload
from modelmetry.openapi.models.summarised_entry import SummarisedEntry
from typing import Optional, Set
from typing_extensions import Self

class Call(BaseModel):
    """
    Call
    """ # noqa: E501
    var_schema: Optional[StrictStr] = Field(default=None, description="A URL to the JSON Schema for this object.", alias="$schema")
    created_at: datetime = Field(alias="CreatedAt")
    created_by: StrictStr = Field(alias="CreatedBy")
    duration_ms: StrictInt = Field(alias="DurationMs")
    guardrail_id: StrictStr = Field(alias="GuardrailID")
    id: StrictStr = Field(alias="ID")
    metadata: Dict[str, Any] = Field(alias="Metadata")
    outcome: StrictStr = Field(alias="Outcome")
    payload: Payload = Field(alias="Payload")
    summarised_entries: List[SummarisedEntry] = Field(alias="SummarisedEntries")
    tenant_id: StrictStr = Field(alias="TenantID")
    updated_at: datetime = Field(alias="UpdatedAt")
    updated_by: StrictStr = Field(alias="UpdatedBy")
    additional_properties: Dict[str, Any] = {}
    __properties: ClassVar[List[str]] = ["$schema", "CreatedAt", "CreatedBy", "DurationMs", "GuardrailID", "ID", "Metadata", "Outcome", "Payload", "SummarisedEntries", "TenantID", "UpdatedAt", "UpdatedBy"]

    @field_validator('outcome')
    def outcome_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['pass', 'fail', 'skip', 'error']):
            raise ValueError("must be one of enum values ('pass', 'fail', 'skip', 'error')")
        return value

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of Call from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        * OpenAPI `readOnly` fields are excluded.
        * Fields in `self.additional_properties` are added to the output dict.
        """
        excluded_fields: Set[str] = set([
            "var_schema",
            "additional_properties",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of payload
        if self.payload:
            _dict['Payload'] = self.payload.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in summarised_entries (list)
        _items = []
        if self.summarised_entries:
            for _item in self.summarised_entries:
                if _item:
                    _items.append(_item.to_dict())
            _dict['SummarisedEntries'] = _items
        # puts key-value pairs in additional_properties in the top level
        if self.additional_properties is not None:
            for _key, _value in self.additional_properties.items():
                _dict[_key] = _value

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of Call from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "$schema": obj.get("$schema"),
            "CreatedAt": obj.get("CreatedAt"),
            "CreatedBy": obj.get("CreatedBy"),
            "DurationMs": obj.get("DurationMs"),
            "GuardrailID": obj.get("GuardrailID"),
            "ID": obj.get("ID"),
            "Metadata": obj.get("Metadata"),
            "Outcome": obj.get("Outcome"),
            "Payload": Payload.from_dict(obj["Payload"]) if obj.get("Payload") is not None else None,
            "SummarisedEntries": [SummarisedEntry.from_dict(_item) for _item in obj["SummarisedEntries"]] if obj.get("SummarisedEntries") is not None else None,
            "TenantID": obj.get("TenantID"),
            "UpdatedAt": obj.get("UpdatedAt"),
            "UpdatedBy": obj.get("UpdatedBy")
        })
        # store additional fields in additional_properties
        for _key in obj.keys():
            if _key not in cls.__properties:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj


