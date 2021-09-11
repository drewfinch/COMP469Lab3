# "CONSTANTS"
#Describes Row/Col indexes to location array
ROW = 0
COL = 1
#Describes value expected at a location that we consider a wall
WALL = 1
#Describes expected value at a location that we consider the Robots current location
ROBOT = 2 # Refactored R to Robot, all instances in project updated. Purpose - Eliminate confusion with ROW Macro
#Describes expected value at a location that we consider the Diamond's location
DIAMOND = 3 # Refactored D to Diamond, all instances in project updated. Purpose - More descriptive
#? Start Location ? Not used in creation of map.
ROOT = -2

#How would you like to use nodes in this project? An example or description will do :) tytyty
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
            line.append(ROBOT) #Using Macro R: 2
        elif char == 'D':
            line.append(DIAMOND) #Using Macro D: 3
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
#   Inlined Func: needed?
def is_floor(maze, coordinate):
    return maze[coordinate[0]][coordinate[1]] == 0

# successors will be pushed
def tree_successor_func(maze, currentNode):
    goalFound = False
    copyLocation = currentNode.data.copy()
    #Order Reversal of Order of Ops allows for Immediate pushing to stack resulting in what has the highest priority of
    # the successor function being placed on top of the stack as the interpreter descends the code.
    #Right
    copyLocation = currentNode.data.copy()
    copyLocation[COL] = copyLocation[COL] + 1
    if is_floor(maze, copyLocation):
        while maze[copyLocation[ROW]][copyLocation[COL] + 1] != WALL:
            copyLocation[COL] = copyLocation[COL] + 1
        newNode = Node(copyLocation, currentNode)
        currentNode.children.append(newNode)
    #Down
    copyLocation = currentNode.data.copy()
    copyLocation[ROW] = copyLocation[ROW] + 1
    if is_floor(maze, copyLocation):
        while maze[copyLocation[ROW] + 1][copyLocation[COL]] != WALL:
            copyLocation[ROW] = copyLocation[ROW] + 1
        newNode = Node(copyLocation, currentNode)
        currentNode.children.append(newNode)
    #Left
    copyLocation = currentNode.data.copy()
    copyLocation[COL] = copyLocation[COL] - 1
    if is_floor(maze, copyLocation):
        while maze[copyLocation[ROW]][copyLocation[COL] - 1] != WALL:
            copyLocation[COL] = copyLocation[COL] - 1
        newNode = Node(copyLocation, currentNode)
        currentNode.children.append(newNode)
    #Up
    copyLocation = currentNode.data.copy()
    copyLocation[ROW] = copyLocation[ROW] - 1
    if is_floor(maze, copyLocation):
        while maze[copyLocation[ROW] - 1][copyLocation[COL]] != WALL:
            copyLocation[ROW] = copyLocation[ROW] - 1
        newNode = Node(copyLocation, currentNode)
        currentNode.children.append(newNode)

    return currentNode

#To be filled
def tree_search(maze):
    path = []
    start = coordinates_of(maze, ROBOT)
    goal = coordinates_of(maze, DIAMOND)
    startNode = Node(start, None)
    goalFound = False
    currentNode = Node(None, None)
    #Fringe utilizing stack behavior
    #Stack Behavior in Python. Use append, highest index is top of stack. Pop removes highest index.
    fringe = [startNode]
    while not goalFound and fringe:
        currentNode = fringe.pop()
        #goal test
        print(currentNode)
        if not goalFound:
            currentNode = tree_successor_func(maze, currentNode)
            fringe.append(currentNode.children.copy())
        else:
            #Populate path from current node
            
    return path

#To be filled
def graph_search(maze):
    return 0


# Prints the full maze
def print_maze(maze):
    for line in maze:
        print()
        for character in line:
            if character == ROBOT:
                print('R', end=' ')
            elif character == DIAMOND:
                print('D', end=' ')
            elif character == 4: #Not Described, but that is the path determined by the node for path to goal
                print(' ', end=' ')
            else:
                print(character, end=' ')
    print()




