from datetime import datetime, timedelta
from typing import Dict, Generic, List, Optional, TypeVar
from uuid import uuid4
from pydantic import Field, UUID4

from mtbpipe.base.pydantic import AliasesBaseGenericModel

from .enums.statuses import PipelineStatusT
from .tasks import TaskModel
from .errors import Error
from .context import TaskContextT

TaskModelT = TypeVar("TaskModelT", bound=TaskModel)


class PipelineModel(AliasesBaseGenericModel, Generic[PipelineStatusT, TaskModelT]):
    id: UUID4 = Field(default_factory=uuid4)
    name: str
    description: Optional[str] = ""
    tasks: List[TaskModelT]
    status: PipelineStatusT
    last_failed: Optional[datetime] = Field(None, alias="lastFailed")
    last_successful: Optional[datetime] = Field(None, alias="lastSuccessful")
    started_at: Optional[datetime] = Field(None, alias="startedAt")
    finished_at: Optional[datetime] = Field(None, alias="finishedAt")
    updated_at: datetime = Field(alias="updated_at")
    created_at: datetime = Field(alias="created_at")

    class Config:
        fields = {
            "errors": "errors",
            "duration": "duration",
            "duration_task_in_progress": "duration_task_in_progress",
        }

    @property
    def errors(self) -> Dict[UUID4, Error[TaskContextT]]:
        return {
            task.id: task.error
            for task in self.tasks
            if task.error
        }

    @property
    def duration(self) -> Optional[timedelta]:
        if not (self.started_at or self.finished_at):
            return None
        return self.finished_at - self.started_at

    @property
    def duration_task_in_progress(self) -> timedelta:
        duration = timedelta()
        for task in self.tasks:
            duration += task.duration if task.duration else 0
        return duration
