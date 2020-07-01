from typing import Tuple

import mlrose_hiive as mlrose
import numpy as np

from Solver.SolverInterface import SolverInterface


def _create_distance_triples(distance_matrix: np.ndarray) -> list:
    n_locations = len(distance_matrix)
    distance_triples = []
    for i in range(n_locations):
        for j in range(i + 1, n_locations):
            distance_triples.append((i, j, distance_matrix[i][j]))

    return distance_triples


class GeneticAlgSolver(SolverInterface):
    def get_order(self, distance_matrix) -> Tuple[np.ndarray, float]:
        n_locations = len(distance_matrix)
        distance_triples = _create_distance_triples(distance_matrix)
        fitness_dists = mlrose.TravellingSales(distances=distance_triples)
        problem_fit = mlrose.TSPOpt(length=n_locations, fitness_fn=fitness_dists, maximize=False)
        best_state, best_fitness, iterations = mlrose.genetic_alg(problem_fit, mutation_prob=0.2,
                                                                  max_attempts=100, random_state=2)

        best_state = super()._close_circle(super()._roll_state_in_order(best_state))
        return best_state, best_fitness
