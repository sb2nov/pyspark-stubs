# Stubs for pyspark.ml.clustering (Python 3)
#

from typing import Any, List, Optional

from pyspark.ml.linalg import Matrix, Vector
from pyspark.ml.util import *
from pyspark.ml.wrapper import JavaEstimator, JavaModel, JavaParams, JavaWrapper
from pyspark.ml.param.shared import *
from pyspark.ml.stat import MultivariateGaussian
from pyspark.sql.dataframe import DataFrame

from numpy import ndarray  # type: ignore[import]

class ClusteringSummary(JavaWrapper):
    @property
    def predictionCol(self) -> str: ...
    @property
    def predictions(self) -> DataFrame: ...
    @property
    def featuresCol(self) -> str: ...
    @property
    def k(self) -> int: ...
    @property
    def cluster(self) -> DataFrame: ...
    @property
    def clusterSizes(self) -> List[int]: ...
    @property
    def numIter(self) -> int: ...

class _GaussianMixtureParams(
    HasMaxIter,
    HasFeaturesCol,
    HasSeed,
    HasPredictionCol,
    HasProbabilityCol,
    HasTol,
    HasAggregationDepth,
    HasWeightCol,
):
    k: Param[int]
    def getK(self) -> int: ...

class GaussianMixtureModel(
    JavaModel,
    _GaussianMixtureParams,
    JavaMLWritable,
    JavaMLReadable[GaussianMixtureModel],
    HasTrainingSummary[GaussianMixtureSummary],
):
    def setFeaturesCol(self, value: str) -> GaussianMixtureModel: ...
    def setPredictionCol(self, value: str) -> GaussianMixtureModel: ...
    def setProbabilityCol(self, value: str) -> GaussianMixtureModel: ...
    @property
    def weights(self) -> List[float]: ...
    @property
    def gaussians(self) -> List[MultivariateGaussian]: ...
    @property
    def gaussiansDF(self) -> DataFrame: ...
    @property
    def summary(self) -> GaussianMixtureSummary: ...
    def predict(self, value: Vector) -> int: ...
    def predictProbability(self, value: Vector) -> Vector: ...

class GaussianMixture(
    JavaEstimator[GaussianMixtureModel],
    _GaussianMixtureParams,
    JavaMLWritable,
    JavaMLReadable[GaussianMixture],
):
    def __init__(
        self,
        *,
        featuresCol: str = ...,
        predictionCol: str = ...,
        k: int = ...,
        probabilityCol: str = ...,
        tol: float = ...,
        maxIter: int = ...,
        seed: Optional[int] = ...,
        aggregationDepth: int = ...,
        weightCol: Optional[str] = ...
    ) -> None: ...
    def setParams(
        self,
        *,
        featuresCol: str = ...,
        predictionCol: str = ...,
        k: int = ...,
        probabilityCol: str = ...,
        tol: float = ...,
        maxIter: int = ...,
        seed: Optional[int] = ...,
        aggregationDepth: int = ...,
        weightCol: Optional[str] = ...
    ) -> GaussianMixture: ...
    def setK(self, value: int) -> GaussianMixture: ...
    def setMaxIter(self, value: int) -> GaussianMixture: ...
    def setFeaturesCol(self, value: str) -> GaussianMixture: ...
    def setPredictionCol(self, value: str) -> GaussianMixture: ...
    def setProbabilityCol(self, value: str) -> GaussianMixture: ...
    def setWeightCol(self, value: str) -> GaussianMixture: ...
    def setSeed(self, value: int) -> GaussianMixture: ...
    def setTol(self, value: float) -> GaussianMixture: ...
    def setAggregationDepth(self, value: int) -> GaussianMixture: ...

class GaussianMixtureSummary(ClusteringSummary):
    @property
    def probabilityCol(self) -> str: ...
    @property
    def probability(self) -> DataFrame: ...
    @property
    def logLikelihood(self) -> float: ...

class KMeansSummary(ClusteringSummary):
    def trainingCost(self) -> float: ...

class _KMeansParams(
    HasMaxIter,
    HasFeaturesCol,
    HasSeed,
    HasPredictionCol,
    HasTol,
    HasDistanceMeasure,
    HasWeightCol,
):
    k: Param[int]
    initMode: Param[str]
    initSteps: Param[int]
    def getK(self) -> int: ...
    def getInitMode(self) -> str: ...
    def getInitSteps(self) -> int: ...

class KMeansModel(
    JavaModel,
    _KMeansParams,
    GeneralJavaMLWritable,
    JavaMLReadable[KMeansModel],
    HasTrainingSummary[KMeansSummary],
):
    def setFeaturesCol(self, value: str) -> KMeansModel: ...
    def setPredictionCol(self, value: str) -> KMeansModel: ...
    def clusterCenters(self) -> List[ndarray]: ...
    @property
    def summary(self) -> KMeansSummary: ...
    def predict(self, value: Vector) -> int: ...

class KMeans(
    JavaEstimator[KMeansModel], _KMeansParams, JavaMLWritable, JavaMLReadable[KMeans]
):
    def __init__(
        self,
        *,
        featuresCol: str = ...,
        predictionCol: str = ...,
        k: int = ...,
        initMode: str = ...,
        initSteps: int = ...,
        tol: float = ...,
        maxIter: int = ...,
        seed: Optional[int] = ...,
        distanceMeasure: str = ...,
        weightCol: Optional[str] = ...
    ) -> None: ...
    def setParams(
        self,
        *,
        featuresCol: str = ...,
        predictionCol: str = ...,
        k: int = ...,
        initMode: str = ...,
        initSteps: int = ...,
        tol: float = ...,
        maxIter: int = ...,
        seed: Optional[int] = ...,
        distanceMeasure: str = ...,
        weightCol: Optional[str] = ...
    ) -> KMeans: ...
    def setK(self, value: int) -> KMeans: ...
    def setInitMode(self, value: str) -> KMeans: ...
    def setInitSteps(self, value: int) -> KMeans: ...
    def setDistanceMeasure(self, value: str) -> KMeans: ...
    def setMaxIter(self, value: int) -> KMeans: ...
    def setFeaturesCol(self, value: str) -> KMeans: ...
    def setPredictionCol(self, value: str) -> KMeans: ...
    def setSeed(self, value: int) -> KMeans: ...
    def setTol(self, value: float) -> KMeans: ...
    def setWeightCol(self, value: str) -> KMeans: ...

class _BisectingKMeansParams(
    HasMaxIter,
    HasFeaturesCol,
    HasSeed,
    HasPredictionCol,
    HasDistanceMeasure,
    HasWeightCol,
):
    k: Param[int]
    minDivisibleClusterSize: Param[float]
    def getK(self) -> int: ...
    def getMinDivisibleClusterSize(self) -> float: ...

class BisectingKMeansModel(
    JavaModel,
    _BisectingKMeansParams,
    JavaMLWritable,
    JavaMLReadable[BisectingKMeansModel],
    HasTrainingSummary[BisectingKMeansSummary],
):
    def setFeaturesCol(self, value: str) -> BisectingKMeansModel: ...
    def setPredictionCol(self, value: str) -> BisectingKMeansModel: ...
    def clusterCenters(self) -> List[ndarray]: ...
    def computeCost(self, dataset: DataFrame) -> float: ...
    @property
    def summary(self) -> BisectingKMeansSummary: ...
    def predict(self, value: Vector) -> int: ...

class BisectingKMeans(
    JavaEstimator[BisectingKMeansModel],
    _BisectingKMeansParams,
    JavaMLWritable,
    JavaMLReadable[BisectingKMeans],
):
    def __init__(
        self,
        *,
        featuresCol: str = ...,
        predictionCol: str = ...,
        maxIter: int = ...,
        seed: Optional[int] = ...,
        k: int = ...,
        minDivisibleClusterSize: float = ...,
        distanceMeasure: str = ...,
        weightCol: Optional[str] = ...
    ) -> None: ...
    def setParams(
        self,
        *,
        featuresCol: str = ...,
        predictionCol: str = ...,
        maxIter: int = ...,
        seed: Optional[int] = ...,
        k: int = ...,
        minDivisibleClusterSize: float = ...,
        distanceMeasure: str = ...,
        weightCol: Optional[str] = ...
    ) -> BisectingKMeans: ...
    def setK(self, value: int) -> BisectingKMeans: ...
    def setMinDivisibleClusterSize(self, value: float) -> BisectingKMeans: ...
    def setDistanceMeasure(self, value: str) -> BisectingKMeans: ...
    def setMaxIter(self, value: int) -> BisectingKMeans: ...
    def setFeaturesCol(self, value: str) -> BisectingKMeans: ...
    def setPredictionCol(self, value: str) -> BisectingKMeans: ...
    def setSeed(self, value: int) -> BisectingKMeans: ...
    def setWeightCol(self, value: str) -> BisectingKMeans: ...

class BisectingKMeansSummary(ClusteringSummary):
    @property
    def trainingCost(self) -> float: ...

class _LDAParams(HasMaxIter, HasFeaturesCol, HasSeed, HasCheckpointInterval):
    k: Param[int]
    optimizer: Param[str]
    learningOffset: Param[float]
    learningDecay: Param[float]
    subsamplingRate: Param[float]
    optimizeDocConcentration: Param[bool]
    docConcentration: Param[List[float]]
    topicConcentration: Param[float]
    topicDistributionCol: Param[str]
    keepLastCheckpoint: Param[bool]
    def setK(self, value: int) -> LDA: ...
    def getOptimizer(self) -> str: ...
    def getLearningOffset(self) -> float: ...
    def getLearningDecay(self) -> float: ...
    def getSubsamplingRate(self) -> float: ...
    def getOptimizeDocConcentration(self) -> bool: ...
    def getDocConcentration(self) -> List[float]: ...
    def getTopicConcentration(self) -> float: ...
    def getTopicDistributionCol(self) -> str: ...
    def getKeepLastCheckpoint(self) -> bool: ...

class LDAModel(JavaModel, _LDAParams):
    def setFeaturesCol(self, value: str) -> LDAModel: ...
    def setSeed(self, value: int) -> LDAModel: ...
    def setTopicDistributionCol(self, value: str) -> LDAModel: ...
    def isDistributed(self) -> bool: ...
    def vocabSize(self) -> int: ...
    def topicsMatrix(self) -> Matrix: ...
    def logLikelihood(self, dataset: DataFrame) -> float: ...
    def logPerplexity(self, dataset: DataFrame) -> float: ...
    def describeTopics(self, maxTermsPerTopic: int = ...) -> DataFrame: ...
    def estimatedDocConcentration(self) -> Vector: ...

class DistributedLDAModel(
    LDAModel, JavaMLReadable[DistributedLDAModel], JavaMLWritable
):
    def toLocal(self) -> LDAModel: ...
    def trainingLogLikelihood(self) -> float: ...
    def logPrior(self) -> float: ...
    def getCheckpointFiles(self) -> List[str]: ...

class LocalLDAModel(LDAModel, JavaMLReadable[LocalLDAModel], JavaMLWritable): ...

class LDA(JavaEstimator[LDAModel], _LDAParams, JavaMLReadable[LDA], JavaMLWritable):
    def __init__(
        self,
        *,
        featuresCol: str = ...,
        maxIter: int = ...,
        seed: Optional[int] = ...,
        checkpointInterval: int = ...,
        k: int = ...,
        optimizer: str = ...,
        learningOffset: float = ...,
        learningDecay: float = ...,
        subsamplingRate: float = ...,
        optimizeDocConcentration: bool = ...,
        docConcentration: Optional[List[float]] = ...,
        topicConcentration: Optional[float] = ...,
        topicDistributionCol: str = ...,
        keepLastCheckpoint: bool = ...
    ) -> None: ...
    def setParams(
        self,
        *,
        featuresCol: str = ...,
        maxIter: int = ...,
        seed: Optional[int] = ...,
        checkpointInterval: int = ...,
        k: int = ...,
        optimizer: str = ...,
        learningOffset: float = ...,
        learningDecay: float = ...,
        subsamplingRate: float = ...,
        optimizeDocConcentration: bool = ...,
        docConcentration: Optional[List[float]] = ...,
        topicConcentration: Optional[float] = ...,
        topicDistributionCol: str = ...,
        keepLastCheckpoint: bool = ...
    ) -> LDA: ...
    def setCheckpointInterval(self, value: int) -> LDA: ...
    def setSeed(self, value: int) -> LDA: ...
    def setK(self, value: int) -> LDA: ...
    def setOptimizer(self, value: str) -> LDA: ...
    def setLearningOffset(self, value: float) -> LDA: ...
    def setLearningDecay(self, value: float) -> LDA: ...
    def setSubsamplingRate(self, value: float) -> LDA: ...
    def setOptimizeDocConcentration(self, value: bool) -> LDA: ...
    def setDocConcentration(self, value: List[float]) -> LDA: ...
    def setTopicConcentration(self, value: float) -> LDA: ...
    def setTopicDistributionCol(self, value: str) -> LDA: ...
    def setKeepLastCheckpoint(self, value: bool) -> LDA: ...
    def setMaxIter(self, value: int) -> LDA: ...
    def setFeaturesCol(self, value: str) -> LDA: ...

class _PowerIterationClusteringParams(HasMaxIter, HasWeightCol):
    k: Param[int]
    initMode: Param[str]
    srcCol: Param[str]
    dstCol: Param[str]
    def getK(self) -> int: ...
    def getInitMode(self) -> str: ...
    def getSrcCol(self) -> str: ...
    def getDstCol(self) -> str: ...

class PowerIterationClustering(
    _PowerIterationClusteringParams,
    JavaParams,
    JavaMLReadable[PowerIterationClustering],
    JavaMLWritable,
):
    def __init__(
        self,
        *,
        k: int = ...,
        maxIter: int = ...,
        initMode: str = ...,
        srcCol: str = ...,
        dstCol: str = ...,
        weightCol: Optional[str] = ...
    ) -> None: ...
    def setParams(
        self,
        *,
        k: int = ...,
        maxIter: int = ...,
        initMode: str = ...,
        srcCol: str = ...,
        dstCol: str = ...,
        weightCol: Optional[str] = ...
    ) -> PowerIterationClustering: ...
    def setK(self, value: int) -> PowerIterationClustering: ...
    def setInitMode(self, value: str) -> PowerIterationClustering: ...
    def setSrcCol(self, value: str) -> str: ...
    def setDstCol(self, value: str) -> PowerIterationClustering: ...
    def setMaxIter(self, value: int) -> PowerIterationClustering: ...
    def setWeightCol(self, value: str) -> PowerIterationClustering: ...
    def assignClusters(self, dataset: DataFrame) -> DataFrame: ...
