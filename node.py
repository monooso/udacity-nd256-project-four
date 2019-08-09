class Node(object):
    def __init__(self, id, x, y):
        self.__id = id
        self.__x = x
        self.__y = y
        self.reset()

    @property
    def id(self):
        return self.__id

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    @property
    def total_distance_to_goal(self):
        """
        Get the distance from the origin to the goal, via this node.

        :returns: the total distance
        """
        return self.distance_to_here + self.distance_to_goal

    def reset(self):
        """Reset any mutable values."""
        self.via = None
        self.visited = False
        self.distance_to_goal = float('inf')
        self.distance_to_here = float('inf')