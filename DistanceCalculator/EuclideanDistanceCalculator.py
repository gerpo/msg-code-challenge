import math

import Constants
import Location
from DistanceCalculator.DistanceCalculatorInterface import DistanceCalculatorInterface


class EuclideanDistanceCalculator(DistanceCalculatorInterface):
    def distance_between(self, a: Location, b: Location) -> float:
        x = (a.latitude - b.latitude)
        y = (a.longitude - b.longitude) * math.cos(b.latitude)
        return Constants.LONGITUDE_MAX_DISTANCE * math.sqrt(x ** 2 + y ** 2)
