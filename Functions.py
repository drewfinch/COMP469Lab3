# "CONSTANTS"
R = 2
D = 3
ROOT = -2


class Node:
    def __init__(self, data, parent):
        self.parent = parent
        self.children = []
        self.data = data


def create_map():
    # map_name = input("Enter map name(try \"mazeMap.txt\"): ")
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
            line.append(2)
        elif char == 'D':
            line.append(3)
        elif char == '\n':
            maze.append(line)
            line = []
    if line:
        maze.append(line)
    file.close()
    return maze


def coordinates_of(maze, value):
    for i, x in enumerate(maze):
        if value in x:
            return [i, x.index(value)]


def is_floor(maze, coordinate):
    return maze[coordinate[0]][coordinate[1]] == 0


def get_children(parent, maze, moves, goal):
    children = []
    directions = []

    i = parent.data[1]
    while (i > -1 and maze[parent.data[0]][i] != 1):
        if maze[parent.data[0]][i - 1] == 1 and i != parent.data[1]:
            directions.append([parent.data[0], i])
        i -= 1
    i = parent.data[1]
    while (i < len(maze[parent.data[0]]) and maze[parent.data[0]][i] != 1):
        if maze[parent.data[0]][i + 1] == 1 and i != parent.data[1]:
            directions.append([parent.data[0], i])
        i += 1
    mazeColumn = ([x[parent.data[1]] for x in maze])
    i = parent.data[0]
    while (i > -1 and mazeColumn[i] != 1):
        if mazeColumn[i - 1] == 1 and i != parent.data[1]:
            directions.append([i, parent.data[1]])
        i -= 1
    i = parent.data[0]
    while (i < len(mazeColumn) and mazeColumn[i] != 1):
        if mazeColumn[i + 1] == 1 and i != parent.data[1]:
            directions.append([i, parent.data[1]])
        i += 1

    if goal in directions:
        return [Node(goal, parent)]

    moves_coordinates = []

    for move in moves:
        moves_coordinates.append(move.data)

    for direction in directions:
        if is_floor(maze, direction) and direction not in moves_coordinates:
            children.append(Node(direction, parent))
    return children


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

def depth_first_search(maze):
    return maze