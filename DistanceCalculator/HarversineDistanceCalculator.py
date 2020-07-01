import math

import Constants
import Location
from DistanceCalculator.DistanceCalculatorInterface import DistanceCalculatorInterface


class HarversineDistanceCalculator(DistanceCalculatorInterface):
    def distance_between(self, a: Location, b: Location) -> float:
        # convert decimal degrees to radians
        lon1, lat1, lon2, lat2 = map(math.radians, [a.longitude, a.latitude, b.longitude, b.latitude])

        # haversine formula
        dlon = lon2 - lon1
        dlat = lat2 - lat1
        a = math.sin(dlat / 2) ** 2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2) ** 2
        c = 2 * math.asin(math.sqrt(a))
        r = Constants.EARTH_RADIUS
        return c * r
