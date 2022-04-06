from typing import Any, Dict, TypeVar, Union

from pydantic import BaseModel

TaskContextT = TypeVar("TaskContextT", bound=Union[Dict[str, Any], BaseModel])
