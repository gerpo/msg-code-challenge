from typing import Tuple

import elkai
import numpy as np

from Solver.SolverInterface import SolverInterface


def _full_distance_for_state(state: np.ndarray, distance_matrix: np.ndarray) -> float:
    n_state = len(state)
    distance = 0
    for i in range(n_state - 1):
        distance = distance + distance_matrix[state[i], state[i + 1]]

    return distance


class LKHSolver(SolverInterface):
    def get_order(self, distance_matrix: np.ndarray) -> Tuple[np.ndarray, float]:
        state = elkai.solve_float_matrix(distance_matrix)
        state = super()._close_circle(super()._roll_state_in_order(state))
        full_distance = _full_distance_for_state(state, distance_matrix)

        return state, full_distance
