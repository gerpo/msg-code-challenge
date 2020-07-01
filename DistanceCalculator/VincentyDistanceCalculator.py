from geopy import distance

import Location
from DistanceCalculator.DistanceCalculatorInterface import DistanceCalculatorInterface


class VincentyDistanceCalculator(DistanceCalculatorInterface):
    def distance_between(self, a: Location, b: Location) -> float:
        return distance.geodesic((a.latitude, a.longitude), (b.latitude, b.longitude)).km
