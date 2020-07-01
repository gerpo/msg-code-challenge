from geopy import distance

import Location
from DistanceCalculator.DistanceCalculatorInterface import DistanceCalculatorInterface


class GreatCircleDistanceCalculator(DistanceCalculatorInterface):
    def distance_between(self, a: Location, b: Location) -> float:
        return distance.great_circle((a.latitude, a.longitude), (b.latitude, b.longitude)).km
