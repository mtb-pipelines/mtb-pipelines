from enum import auto

from mtbpipe.base.enums import StrAutoEnum


class CancelReason(StrAutoEnum):
    DEPEND_TASK_FAILED = auto()
    DEPEND_TASK_CANCELED = auto()
