import numpy as np
import pandas as pd

import Constants
from DistanceCalculator.DistanceCalculatorBuilder import DistanceCalculatorBuilder
from Location import Location
from Solver.SolverBuilder import SolverBuilder
from Visualization import visualize

"""
Variables that can be adjusted.

"""
input_file = 'msg_standorte_deutschland.csv'
distance_type = Constants.GREAT_CIRCLE_DISTANCE
solver_type = Constants.ORTOOLS_SOLVER

print_itinerary = True

visualization_options = {
    'show_visualization': True,
    'animate_visualization': True,
    'export_as_image': False}

#############################################################
"""
The following does not need to be changed.
"""

distance_calculator = DistanceCalculatorBuilder.build(distance_type)
solver = SolverBuilder.build(solver_type)

input_data = pd.read_csv(input_file)
locations = [Location(*kwargs.values()) for kwargs in input_data.to_dict(orient='records')]
n_locations = len(locations)
distances = np.zeros([n_locations, n_locations])
for i in range(n_locations):
    for j in range(i):
        distances[i, j] = distances[j, i] = distance_calculator.distance_between(locations[i], locations[j])

found_order, objective_value = solver.get_order(distances)


print(f'The best order found is: {found_order}')
print(f'The traveled distance with that order is: {objective_value} km')
if print_itinerary:
    print(f'This corresponds to the following itinerary:')
    [print(f'\t -> {locations[i].name}') for i in found_order]

visualization_options['sub_title'] = f'Distance Type: {distance_type} <br>' \
                                    + f'Solver Type: {solver_type} <br>' \
                                    + f'(Calculated) Traveled Distance: {objective_value} km'
visualize(locations, found_order, visualization_options)
