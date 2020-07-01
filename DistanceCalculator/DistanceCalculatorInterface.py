import abc
import Location


class DistanceCalculatorInterface:

    @abc.abstractmethod
    def distance_between(self, a: Location, b: Location) -> float:
        raise NotImplementedError
