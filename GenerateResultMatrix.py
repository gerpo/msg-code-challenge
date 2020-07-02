import os
import time

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
distance_set = np.array([Constants.EUCLIDEAN_DISTANCE, Constants.HAVERSINE_DISTANCE, Constants.VINCENTY_DISTANCE, Constants.GREAT_CIRCLE_DISTANCE])
solver_set = np.array([Constants.MLROSE_SOLVER, Constants.LKH_SOLVER, Constants.ORTOOLS_SOLVER])

visualization_options = {
    'show_visualization': False,
    'animate_visualization': False,
    'export_as_image': True}

#############################################################
"""
The following does not need to be changed.
"""

matrix = np.array(np.meshgrid(solver_set, distance_set)).T.reshape(-1, 2)

dataframe_data = {}

input_data = pd.read_csv(input_file)
locations = [Location(*kwargs.values()) for kwargs in input_data.to_dict(orient='records')]
n_locations = len(locations)
distances = np.zeros([n_locations, n_locations])

for x in range(len(matrix)):
    solver_type = matrix[x][0]
    distance_type = matrix[x][1]
    distance_calculator = DistanceCalculatorBuilder.build(distance_type)
    solver = SolverBuilder.build(solver_type)

    for i in range(n_locations):
        for j in range(i):
            distances[i, j] = distances[j, i] = distance_calculator.distance_between(locations[i], locations[j])

    start_time = time.time()
    found_order, objective_value = solver.get_order(distances)
    duration = time.time() - start_time

    dataframe_data.setdefault(distance_type, []).append(f'{objective_value:.2f} km<br> {duration} s<br> [Result](results/images/{solver_type}_{distance_type}.svg)')

    visualization_options['sub_title'] = f'Distance Type: {distance_type} <br>' \
                                         + f'Solver Type: {solver_type} <br>' \
                                         + f'(Calculated) Traveled Distance: {objective_value:.2f} km'
    visualization_options['export_name'] = f'{solver_type}_{distance_type}'
    visualize(locations, found_order, visualization_options)

results = pd.DataFrame(data=dataframe_data, index=pd.Series(solver_set))
results.to_csv(os.path.join('results', 'results.csv'))


