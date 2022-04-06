from typing import Generic, Optional

from pydantic import Field, UUID4

from mtbpipe.base.pydantic import AliasesBaseGenericModel

from .context import TaskContextT


class Error(AliasesBaseGenericModel, Generic[TaskContextT]):
    task_id: UUID4
    exception: str
    error_traceback: Optional[str] = Field("", alias="traceback")
    details: Optional[str] = ""
    task_context: TaskContextT = Field(default_factory=dict)
