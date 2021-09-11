from Functions import *

def populatePathTest():
    head = Node([2,7], None)
    node1 = Node([1,7], head)
    head.children.append(node1)
    node2 = Node([1,5], node1)
    node1.children.append(node2)
    node3 = Node([3,5], node2)
    node2.children.append(node3)
    path = populate_path(node3)
    print(path) #Expected: [2, 7], [1, 7], [1, 5], [3, 5]

populatePathTest()
