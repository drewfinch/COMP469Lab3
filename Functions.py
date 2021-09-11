# "CONSTANTS"
R = 2
D = 3
ROOT = -2

#How would you like to use nodes in this project? An example or description will do :) tytyty
class Node:
    def __init__(self, data, parent):
        self.parent = parent
        self.children = []
        self.data = data


def create_map():
    map_name = input("Enter map name(try \"mazeMap.txt\"): ")
    map_name = "mazeMap.txt"
    file = open(map_name, "r")
    maze = []
    line = []
    while 1:
        char = file.read(1)
        if not char:
            break
        elif char == '1':
            line.append(1)
        elif char == '0':
            line.append(0)
        elif char == 'R':
            line.append(R) #Using Macro R: 2
        elif char == 'D':
            line.append(D) #Using Macro D: 3
        elif char == '\n':
            maze.append(line)
            line = []
    if line:
        maze.append(line)
    file.close()
    return maze

# coordinates_of determines the [ROW, COL] or R or D depending on what you pass as value
def coordinates_of(maze, value):  # to find R and D
    for i, x in enumerate(maze):
        if value in x:
            return [i, x.index(value)]

#Checks that current location is not the wall
def is_floor(maze, coordinate):
    return maze[coordinate[0]][coordinate[1]] == 0

#To be filled
def tree_search(maze):
    start = coordinates_of(maze, R)
    goal = coordinates_of(maze, D)
    fringe = []

    return 0

#To be filled
def graph_search(maze):
    return 0

# successors will be pushed
def tree_successor_func():


# Prints the full maze
def print_maze(maze):
    for line in maze:
        print()
        for character in line:
            if character == R:
                print('R', end=' ')
            elif character == D:
                print('D', end=' ')
            elif character == 4:
                print(' ', end=' ')
            else:
                print(character, end=' ')
    print()




