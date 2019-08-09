from map_data import MapData
from space import Space


# Create the test data
map_data = MapData(
    intersections={0: [1, 2], 1: [2, 3], 2: [3, 4], 3: [5, 6]},
    roads=[[1, 2, 3], [0, 3], [0, 3], [0, 1, 2]]
)

# Initialise the space
space = Space(map_data.intersections, map_data.roads)

# Assert that the space was initialised correctly
assert space.lines[0] == [1, 2, 3]
assert space.lines[3] == [0, 1, 2]

assert space.nodes[0].id == 0
assert space.nodes[0].x == 1
assert space.nodes[0].y == 2

assert space.nodes[3].id == 3
assert space.nodes[3].x == 5
assert space.nodes[3].y == 6

# find_linked_nodes
assert space.find_linked_nodes(0) == [1, 2, 3]
assert space.find_linked_nodes(1) == [0, 3]
assert space.find_linked_nodes(2) == [0, 3]
assert space.find_linked_nodes(3) == [0, 1, 2]
assert space.find_linked_nodes(4) == []