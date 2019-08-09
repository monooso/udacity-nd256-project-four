from route_finder import RouteFinder
from space import Space

def shortest_path(map_data, origin_id, goal_id):
    space = Space(map_data.intersections, map_data.roads)
    finder = RouteFinder(space)
    return finder.find_route(origin_id, goal_id)