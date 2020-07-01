import Constants
from DistanceCalculator import DistanceCalculatorInterface
from DistanceCalculator.EuclideanDistanceCalculator import EuclideanDistanceCalculator
from DistanceCalculator.GreatCircleDistanceCalculator import GreatCircleDistanceCalculator
from DistanceCalculator.HarversineDistanceCalculator import HarversineDistanceCalculator
from DistanceCalculator.VincentyDistanceCalculator import VincentyDistanceCalculator


class InvalidCalculatorType(Exception):
    pass


class DistanceCalculatorBuilder:
    @staticmethod
    def build(calculator_type: str) -> DistanceCalculatorInterface:
        switcher = {
            Constants.EUCLIDEAN_DISTANCE: EuclideanDistanceCalculator,
            Constants.HAVERSINE_DISTANCE: HarversineDistanceCalculator,
            Constants.VINCENTY_DISTANCE: VincentyDistanceCalculator,
            Constants.GREAT_CIRCLE_DISTANCE: GreatCircleDistanceCalculator,
        }
        try:
            return switcher[calculator_type]()
        except KeyError:
            raise InvalidCalculatorType from None
