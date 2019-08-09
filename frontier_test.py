from frontier import Frontier
from node import Node

frontier = Frontier()
frontier.add_or_update('a', 40)
frontier.add_or_update('b', 20)
frontier.add_or_update('c', 30)

assert frontier.remove() == 'b'
assert frontier.remove() == 'c'

frontier.add_or_update('d', 10)
frontier.add_or_update('e', 50)

assert frontier.remove() == 'd'
assert frontier.remove() == 'a'
assert frontier.remove() == 'e'
assert frontier.remove() is None
