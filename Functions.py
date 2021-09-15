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


#How would you like to use nodes in this project? An example or description will do :) tytyty
class Node:
    def __init__(self, data, parent):
        self.parent = parent
        self.children = []
        self.data = data

    def copy(self):
        newNode = Node(self.data, self.parent)
        return newNode

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
def coordinates_of(maze, value):
    for i, x in enumerate(maze):
        if value in x:
            return [i, x.index(value)]

# Evaluate available moves for agent. Available moves will be placed into the current state node as children.
def successor_func(maze, currentNode):
    goalFound = False
    copyLocation = currentNode.data.copy()
    #Order Reversal of ops so children mimics fringe stack.
    #Right - Evaluate right movement state if available
    copyLocation[COL] = copyLocation[COL] + 1
    if maze[copyLocation[ROW]][copyLocation[COL]] != WALL:
        while maze[copyLocation[ROW]][copyLocation[COL] + 1] != WALL:
            copyLocation[COL] = copyLocation[COL] + 1
        newNode = Node(copyLocation, currentNode)
        currentNode.children.append(newNode)
    #Down - Evaluate down movement state if available
    copyLocation = currentNode.data.copy()
    copyLocation[ROW] = copyLocation[ROW] + 1
    if maze[copyLocation[ROW]][copyLocation[COL]] != WALL:
        while maze[copyLocation[ROW] + 1][copyLocation[COL]] != WALL:
            copyLocation[ROW] = copyLocation[ROW] + 1
        newNode = Node(copyLocation, currentNode)
        currentNode.children.append(newNode)
    #Left - Evaluate left movement state if available
    copyLocation = currentNode.data.copy()
    copyLocation[COL] = copyLocation[COL] - 1
    if maze[copyLocation[ROW]][copyLocation[COL]] != WALL:
        while maze[copyLocation[ROW]][copyLocation[COL] - 1] != WALL:
            copyLocation[COL] = copyLocation[COL] - 1
        newNode = Node(copyLocation, currentNode)
        currentNode.children.append(newNode)
    #Up - Evaluate up movement state if available
    copyLocation = currentNode.data.copy()
    copyLocation[ROW] = copyLocation[ROW] - 1
    if maze[copyLocation[ROW]][copyLocation[COL]] != WALL:
        while maze[copyLocation[ROW] - 1][copyLocation[COL]] != WALL:
            copyLocation[ROW] = copyLocation[ROW] - 1
        newNode = Node(copyLocation, currentNode)
        currentNode.children.append(newNode)

    return currentNode

# Tree implementation of DFS search algorithm
def tree_search(maze):
    path = []
    start = coordinates_of(maze, ROBOT)
    goal = coordinates_of(maze, DIAMOND)
    head = Node(start, None)
    goalFound = False
    currentNode = None
    #Fringe utilizing stack behavior
    #Stack Behavior in Python. Use append, highest index is top of stack. Pop removes highest index.
    fringe = [head]
    while not goalFound and fringe:
        currentNode = fringe.pop()
        goalFound = goal_test(goal, currentNode)
        print(currentNode.data)
        if not goalFound:
            currentNode = successor_func(maze, currentNode)
            fringe = append_to_fringe(fringe, currentNode)
        else:
            path = populate_path(currentNode)
    print(path)
    return path

# Graph implementation of DFS search algorithm
def graph_search(maze):
    goalFound = False
    start = coordinates_of(maze, ROBOT)
    goal = coordinates_of(maze, DIAMOND)
    closed = []
    path = None
    head = Node(start, None)
    fringe = [head]
    currentNode = None
    while not goalFound and fringe:
        currentNode = fringe.pop()
        goalFound = goal_test(goal, currentNode)
        if not goalFound and currentNode.data not in closed:
            closed.append(currentNode.data)
            currentNode = successor_func(maze, currentNode)
            fringe = append_to_fringe(fringe, currentNode)
        elif goalFound:
            path = populate_path(currentNode)
    print(path)
    return path

# Returns an array of the locations traveled by the agent from Start to Goal
def populate_path(node):
    path = []
    currentNode = node.copy()
    while currentNode != None:
        path.insert(0, currentNode.data)
        currentNode = currentNode.parent
    return path

# Add the current nodes children to the fringe
def append_to_fringe(fringe, currentNode):
    for node in currentNode.children:
        fringe.append(node.copy())
    return fringe

def goal_test(goal, currentNode):
    goalFound = False
    if goal[ROW] == currentNode.data[ROW] and goal[COL] == currentNode.data[COL]:
        goalFound = True
    return goalFound


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

# Primary driver of functions
def maze_search(strategy, maze):
    path = None
    if strategy == 'tree':
        path = tree_search(maze)
    elif strategy == 'graph':
        path = graph_search(maze)
    else:
        print("Please specifiy either 'tree' or 'graph' for strategy.")
    return path
