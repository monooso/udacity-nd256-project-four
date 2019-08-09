from node import Node


class Space(object):
    def __init__(self, nodes, lines):
        """
        Initialise the space using the given nodes and lines.

        :param nodes: a dictionary of nodes
        :param lines: a list of lines
        """
        self.nodes = self.create_nodes(nodes)
        self.lines = self.create_lines(lines)

    def create_nodes(self, map_nodes):
        """
        Create the nodes dict, using the given raw nodes data.

        :param map_nodes: a dictionary of map nodes
        """
        return {id: Node(id, pos[0], pos[1]) for id, pos in map_nodes.items()}

    def create_lines(self, map_lines):
        """
        Create the lines dict, using the given raw lines data.

        :param map_lines: a list of map lines
        """
        return {id: nodes for id, nodes in enumerate(map_lines)}

    def find_linked_nodes(self, node_id):
        """
        Get a list of the nodes linked to the given node.

        :param node_id: the ID of the "hub" node
        :returns: a list of node IDs that are connected to the hub node
        """
        return self.lines[node_id] if node_id in self.lines else []

    def reset(self):
        """Clear any calculated node values."""
        for _, node in self.nodes.items():
            node.reset()