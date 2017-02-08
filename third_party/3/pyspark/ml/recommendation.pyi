# Stubs for pyspark.ml.recommendation (Python 3.5)
#

from typing import Any, Optional
from pyspark.ml.util import *
from pyspark.ml.wrapper import JavaEstimator, JavaModel
from pyspark.ml.param.shared import *
from pyspark.sql.dataframe import DataFrame

class ALS(JavaEstimator, HasCheckpointInterval, HasMaxIter, HasPredictionCol, HasRegParam, HasSeed, JavaMLWritable, JavaMLReadable):
    rank = ...  # type: Param
    numUserBlocks = ...  # type: Param
    numItemBlocks = ...  # type: Param
    implicitPrefs = ...  # type: Param
    alpha = ...  # type: Param
    userCol = ...  # type: Param
    itemCol = ...  # type: Param
    ratingCol = ...  # type: Param
    nonnegative = ...  # type: Param
    intermediateStorageLevel = ...  # type: Param
    finalStorageLevel = ...  # type: Param
    def __init__(self, rank: int = ..., maxIter: int = ..., regParam: float = ..., numUserBlocks: int = ..., numItemBlocks: int = ..., implicitPrefs: bool = ..., alpha: float = ..., userCol: str = ..., itemCol: str = ..., seed: Optional[int] = ..., ratingCol: str = ..., nonnegative: bool = ..., checkpointInterval: int = ..., intermediateStorageLevel: str = ..., finalStorageLevel: str = ...) -> None: ...
    def setParams(self, rank: int = ..., maxIter: int = ..., regParam: float = ..., numUserBlocks: int = ..., numItemBlocks: int = ..., implicitPrefs: bool = ..., alpha: float = ..., userCol: str = ..., itemCol: str = ..., seed: Optional[int] = ..., ratingCol: str = ..., nonnegative: bool = ..., checkpointInterval: int = ..., intermediateStorageLevel: str = ..., finalStorageLevel: str = ...) -> ALS: ...
    def setRank(self, value: int) -> ALS: ...
    def getRank(self) -> int: ...
    def setNumUserBlocks(self, value: int) -> ALS: ...
    def getNumUserBlocks(self) -> int: ...
    def setNumItemBlocks(self, value: int) -> ALS: ...
    def getNumItemBlocks(self) -> int: ...
    def setNumBlocks(self, value: int) -> ALS: ...
    def setImplicitPrefs(self, value: bool) -> ALS: ...
    def getImplicitPrefs(self) -> bool: ...
    def setAlpha(self, value: float) -> ALS: ...
    def getAlpha(self) -> float: ...
    def setUserCol(self, value: str) -> ALS: ...
    def getUserCol(self) -> str: ...
    def setItemCol(self, value: str) -> ALS: ...
    def getItemCol(self) -> str: ...
    def setRatingCol(self, value: str) -> ALS: ...
    def getRatingCol(self) -> str: ...
    def setNonnegative(self, value: bool) -> ALS: ...
    def getNonnegative(self) -> bool: ...
    def setIntermediateStorageLevel(self, value: str) -> ALS: ...
    def getIntermediateStorageLevel(self) -> str: ...
    def setFinalStorageLevel(self, value: str) -> ALS: ...
    def getFinalStorageLevel(self) -> str: ...

class ALSModel(JavaModel, JavaMLWritable, JavaMLReadable):
    @property
    def rank(self) -> int: ...
    @property
    def userFactors(self) -> DataFrame: ...
    @property
    def itemFactors(self) -> DataFrame: ...
