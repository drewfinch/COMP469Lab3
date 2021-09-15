# COMP 469
# Lab 3
# Drew Finch
# Travis Chamness
from Functions import *

start_maze = create_map()
print_maze(start_maze)
# graph_search(start_maze)
# print(maze_search('tree',start_maze))
maze_search('graph', start_maze)
# maze_search('balogna', start_maze)

