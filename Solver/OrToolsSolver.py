from typing import Tuple

import numpy as np
from ortools.constraint_solver import pywrapcp, routing_enums_pb2

from Solver.SolverInterface import SolverInterface


def _get_routes(solution, routing, manager):
    index = routing.Start(0)
    route = [manager.IndexToNode(index)]
    while not routing.IsEnd(index):
        index = solution.Value(routing.NextVar(index))
        route.append(manager.IndexToNode(index))
    return np.asarray(route)


class OrToolsSolver(SolverInterface):
    def get_order(self, distance_matrix: np.ndarray) -> Tuple[np.ndarray, float]:
        manager = pywrapcp.RoutingIndexManager(len(distance_matrix), 1, 0)
        routing = pywrapcp.RoutingModel(manager)

        def distance_callback(from_index, to_index):
            from_node = manager.IndexToNode(from_index)
            to_node = manager.IndexToNode(to_index)
            return distance_matrix[from_node][to_node]

        transit_callback_index = routing.RegisterTransitCallback(distance_callback)
        routing.SetArcCostEvaluatorOfAllVehicles(transit_callback_index)

        search_parameters = pywrapcp.DefaultRoutingSearchParameters()
        search_parameters.first_solution_strategy = routing_enums_pb2.FirstSolutionStrategy.PATH_CHEAPEST_ARC

        solution = routing.SolveWithParameters(search_parameters)

        return _get_routes(solution, routing, manager), solution.ObjectiveValue()
