class Frontier(object):
    def __init__(self):
        """Initialise the Frontier instance."""
        self.reset()

    def add_or_update(self, id, total_distance):
        """
        Add the node with the given ID to the frontier. If it already exists, update the distance.

        :param id: a node id
        :param total_distance: the total distance from the node to the goal
        """
        self.__nodes[id] = total_distance

    def remove(self):
        """
        The remove the lowest cost node from the frontier.

        :returns: a node id, or None
        """
        if len(self.__nodes) == 0:
            return None

        id = min(self.__nodes, key=self.__nodes.get)
        del self.__nodes[id]
        return id

    def reset(self):
        """Empty the frontier."""
        self.__nodes = {}