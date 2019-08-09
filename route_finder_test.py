from map_data import MapData, map_40
from route_finder import RouteFinder
from space import Space


# Create the test data
map_data = MapData(
    intersections={0: [1, 2], 1: [2, 3], 2: [3, 4], 3: [5, 6]},
    roads=[[1, 2], [0, 3], [0, 2], [1, 2]]
)

# Initialise the space and route finder
space = Space(map_data.intersections, map_data.roads)
finder = RouteFinder(space)

# Find a route between invalid nodes
assert finder.find_route(10, 0) == None
assert finder.find_route(0, 10) == None

# Now for the real deal
space = Space(map_40.intersections, map_40.roads)
finder = RouteFinder(space)

assert finder.find_route(5, 34) == [5, 16, 37, 12, 34]
assert finder.find_route(5, 5) == [5]
assert finder.find_route(8, 24) == [8, 14, 16, 37, 12, 17, 10, 24]