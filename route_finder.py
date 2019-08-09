import math
from frontier import Frontier


class RouteFinder(object):
    def __init__(self, space):
        self.__space = space
        self.__frontier = Frontier()
        self.__goal = None
        self.__origin = None

    def __calculate_distance(self, from_xy, to_xy):
        """
        Calculate the distance between the given coordinates using MATH.

        :param from_xy: a tuple of the form (x, y)
        :param to_xy: a tuple of the form (x, y)
        :returns: float
        """
        diff_x = math.fabs(from_xy[0] - to_xy[0])
        diff_y = math.fabs(from_xy[1] - to_xy[1])
        return math.sqrt(math.pow(diff_x, 2) + math.pow(diff_y, 2))

    def __initialize_goal(self, goal_id):
        """
        Initialise the goal node, identified by the given ID.

        :param goal_id: the goal id
        """
        self.__goal = self.__space.nodes[goal_id]
        self.__goal.distance_to_goal = 0

    def __initialize_origin(self, origin_id):
        """
        Initialise the origin node, identified by the given ID.

        :param origin: the origin id
        """
        self.__origin = self.__space.nodes[origin_id]
        self.__origin.route_distance = 0

    def __add_to_frontier(self, from_node, to_node):
        """
        Attempt to add the "to" node to the frontier.

        :param from_node: the previous node
        :param to_node: the next node
        """
        if to_node.visited:
            return

        if from_node is None:
            distance_to_node = 0
        else:
            distance_to_node = self.__calculate_distance(
                (from_node.x, from_node.y),
                (to_node.x, to_node.y)
            ) + from_node.distance_to_here

        # Have we found a shorter route to this node?
        if distance_to_node < to_node.distance_to_here:
            to_node.distance_to_here = distance_to_node
            to_node.via = from_node

        if math.isinf(to_node.distance_to_goal):
            # Always low-ball to estimated distance, otherwise A* won't work
            to_node.distance_to_goal = self.__calculate_distance(
                (to_node.x, to_node.y),
                (self.__goal.x, self.__goal.y)
            ) * 0.9

        self.__frontier.add_or_update(to_node.id, to_node.total_distance_to_goal)

    def __get_route_ids(self):
        """
        Get the IDs of the best route from the origin to the goal.

        :returns: a list of node IDs
        """
        route = []
        node = self.__goal
        while node is not None:
            route.append(node.id)
            node = node.via
        return list(reversed(route))

    def __find_route(self):
        """
        Find the shortest route between the origin and the goal.

        :returns: a list of IDs representing the steps from the origin to the goal, or None
        """
        active_node = self.__space.nodes[self.__frontier.remove()]

        # Exit conditions
        if active_node is None:
            return None
        if active_node == self.__goal:
            return self.__get_route_ids()

        active_node.visited = True

        # Add the linked nodes to the frontier
        for linked_id in self.__space.find_linked_nodes(active_node.id):
            if linked_id not in self.__space.nodes:
                # Something is awry with the map data
                return None
            self.__add_to_frontier(active_node, self.__space.nodes[linked_id])

        return self.__find_route()

    def find_route(self, origin_id, goal_id):
        """
        Find the shortest route between the specified nodes.

        :param origin_id: the ID of the "origin" node
        :param goal_id: the ID of the "goal" node
        :returns: a list of IDs representing the steps from the origin to the goal, or None
        """
        if origin_id not in self.__space.nodes or goal_id not in self.__space.nodes:
            return None

        if origin_id == goal_id:
            return [origin_id]

        self.__space.reset()
        self.__frontier.reset()
        self.__initialize_origin(origin_id)
        self.__initialize_goal(goal_id)
        self.__add_to_frontier(None, self.__origin)

        return self.__find_route()