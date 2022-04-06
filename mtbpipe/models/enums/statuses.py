from enum import Enum, auto
from typing import TypeVar, Union

from mtbpipe.base.enums import StrAutoEnum


class TaskStatus(StrAutoEnum):
    NEW = auto()
    PENDING = auto()
    IN_PROGRESS = auto()
    DONE = auto()
    FAILED = auto()
    CANCELED = auto()
    AUTO_CANCELED = auto()


class PipelineStatus(StrAutoEnum):
    NEW = auto()
    IN_PROGRESS = auto()
    DONE = auto()
    PART_FAILED = auto()
    FAILED = auto()
    CANCELED = auto()
    AUTO_CANCELED = auto()


TaskStatusT = TypeVar("TaskStatusT", bound=Union[TaskStatus, Enum])
PipelineStatusT = TypeVar("PipelineStatusT", bound=Union[PipelineStatus, Enum])
