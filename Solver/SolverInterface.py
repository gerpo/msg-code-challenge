import abc
from typing import Tuple

import numpy as np


class SolverInterface:
    @abc.abstractmethod
    def get_order(self, distance_matrix: np.ndarray) -> Tuple[np.ndarray, float]:
        raise NotImplementedError

    @staticmethod
    def _roll_state_in_order(state: np.ndarray) -> np.ndarray:
        index = -np.where(state == 0)[0]
        return np.roll(state, index)

    @staticmethod
    def _close_circle(state: np.ndarray) -> np.ndarray:
        return np.append(state, 0)
