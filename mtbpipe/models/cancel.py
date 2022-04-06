from enum import Enum
from typing import Generic, Optional, TypeVar, Union

from pydantic import Field, UUID4

from mtbpipe.base.pydantic import AliasesBaseGenericModel

from .enums.reasons import CancelReason

CancelReasonT = TypeVar("CancelReasonT", bound=Union[CancelReason, Enum])


class CancelInfo(AliasesBaseGenericModel, Generic[CancelReasonT]):
    actor: Optional[str] = "self"
    related_task_id: Optional[UUID4] = Field(None, alias="relatedTaskId")
    reason: CancelReasonT
