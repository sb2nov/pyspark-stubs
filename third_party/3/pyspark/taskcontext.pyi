# Stubs for pyspark.taskcontext (Python 3)
#

from typing import Any, Dict, List
from typing_extensions import Literal
from pyspark.resourceinformation import ResourceInformation

class TaskContext:
    def __new__(cls) -> TaskContext: ...
    @classmethod
    def get(cls) -> TaskContext: ...
    def stageId(self) -> int: ...
    def partitionId(self) -> int: ...
    def attemptNumber(self) -> int: ...
    def taskAttemptId(self) -> int: ...
    def getLocalProperty(self, key: str) -> str: ...
    def resources(self) -> Dict[str, ResourceInformation]: ...

BARRIER_FUNCTION = Literal[1]

class BarrierTaskContext(TaskContext):
    @classmethod
    def get(cls) -> BarrierTaskContext: ...
    def barrier(self) -> None: ...
    def allGather(self, message: str = ...) -> List[str]: ...
    def getTaskInfos(self) -> List[BarrierTaskInfo]: ...

class BarrierTaskInfo:
    address: str
    def __init__(self, address: str) -> None: ...
