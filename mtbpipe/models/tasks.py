from datetime import datetime, timedelta
from typing import Generic, Optional
from uuid import uuid4
from pydantic import Field, UUID4

from mtbpipe.base.pydantic import AliasesBaseGenericModel

from .enums.statuses import TaskStatusT
from .errors import Error
from .cancel import CancelInfo, CancelReasonT
from .context import TaskContextT


class TaskModel(AliasesBaseGenericModel, Generic[TaskStatusT, CancelReasonT, TaskContextT]):
    id: UUID4 = Field(default_factory=uuid4)
    pipeline_id: UUID4 = Field(alias="pipelineId")
    name: str
    description: Optional[str] = ""
    context: TaskContextT
    status: TaskStatusT
    error: Optional[Error[TaskContextT]] = None
    cancel_reason: Optional[CancelInfo[CancelReasonT]] = Field(None, alias="cancelInfo")
    last_failed: Optional[datetime] = Field(None, alias="lastFailed")
    last_successful: Optional[datetime] = Field(None, alias="lastSuccessful")
    started_at: Optional[datetime] = Field(None, alias="startedAt")
    finished_at: Optional[datetime] = Field(None, alias="finishedAt")
    updated_at: datetime = Field(alias="updatedAt")
    created_at: datetime = Field(alias="createdAt")

    class Config:
        fields = {
            "duration": "duration",
        }

    @property
    def duration(self) -> Optional[timedelta]:
        if not (self.started_at or self.finished_at):
            return None
        return self.finished_at - self.started_at
