from map_data import map_40
from student_code import shortest_path

# Double-check everything runs correctly via the required shortest_path function
assert shortest_path(map_40, 5, 34) == [5, 16, 37, 12, 34]
assert shortest_path(map_40, 5, 5) == [5]
assert shortest_path(map_40, 8, 24) == [8, 14, 16, 37, 12, 17, 10, 24]