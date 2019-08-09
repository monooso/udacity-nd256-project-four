import math
from node import Node

# Check that the node is initialised correctly
node = Node(999, 10, 20)

assert node.via is None
assert node.visited is False
assert math.isinf(node.distance_to_here)
assert math.isinf(node.distance_to_goal)
assert math.isinf(node.total_distance_to_goal)

# Check that the node is reset correctly
node.visited = True
node.reset()
assert node.visited is False

# Check that the total distance is calculated correctly
node.distance_to_here = 10
node.distance_to_goal = 20

assert node.total_distance_to_goal == 30