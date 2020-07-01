"""
General constants.
"""
EARTH_RADIUS = 6371
LONGITUDE_MAX_DISTANCE = 111.3

"""
Distance constants that can be used to calculate the distance between locations.
"""
EUCLIDEAN_DISTANCE = "euclidean"
HAVERSINE_DISTANCE = "haversine"
VINCENTY_DISTANCE = "vincenty"
GREAT_CIRCLE_DISTANCE = "great_circle"

"""
Solver constants that can be used to solve the TSP problem.
"""
MLROSE_SOLVER = "mlrose"
LKH_SOLVER = "lkh"
ORTOOLS_SOLVER = "ortools"
