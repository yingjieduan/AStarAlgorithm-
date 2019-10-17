# Finish A* search function that can find path from starting point to the end
# The robot starts from start position (0,0) and finds a path to end position (4, 5)
# In the maze, 0 is open path while 1 means wall (a robot cannot pass through wall)
# heuristic is provided

# example result:
# [[0, -1, -1, -1, -1, -1],
#  [1, -1, -1, -1, -1, -1],
#  [2, -1, -1, -1, -1, -1],
#  [3, -1,  8, 10, 12, 14],
#  [4,  5,  6,  7, -1, 15]]

maze = [[0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0]]

heuristic = [[9, 8, 7, 6, 5, 4],
             [8, 7, 6, 5, 4, 3],
             [7, 6, 5, 4, 3, 2],
             [6, 5, 4, 3, 2, 1],
             [5, 4, 3, 2, 1, 0]]

start = [0, 0] # starting position
end = [len(maze)-1, len(maze[0])-1] # ending position
cost = 1 # cost per movement

move = [[-1, 0 ], # go up
         [ 0, -1], # go left
         [ 1, 0 ], # go down
         [ 0, 1 ]] # go right

class Node(object):
    """
    Node object maintains the node information including its parent node
    """
    def __init__(self, position, g=0, father = None, heuristic = None):
        self.x, self.y = position  # location of this node
        self.father = father # Parent node also must be a Node instance
        self.g = g  # distance between start node to current node
        self.heuristic = heuristic

    def __eq__(self, other):
        if self.x == other.x and self.y == other.y:
            return True
        else:
            return False

    def getF(self): # total
        """
        return total cost g+h of this node
        """
        return self.g + self.heuristic[self.x][self.y]

    def getG(self): # real
        """
        distance - the real cost - between start node to current node
        """
        return self.g

    def getH(self): # heuristic
        """
        return heuristic cost from current Node to end
        """
        return self.heuristic[self.x][self.y]


def getNodeWithLoweastTotalCost(openList):
    """
    pop the node whose total cost is lowest in openList
    """
    minValue = None
    nodeOfLowTotalCost = None
    popIndex = None
    for index, node in enumerate(openList):
        if minValue is None or node.getF() < minValue:
            minValue = node.getF()
            nodeOfLowTotalCost = node
            popIndex = index

    openList.pop(popIndex)
    return nodeOfLowTotalCost

def printPath(node):
    """
    Print final path by reverse the orders of nodes
    """
    l = []
    while node is not None:
        l.append([node.x, node.y])
        node = node.father

    print("the robot path is ", l[::-1])

    res = [[-1]*len(maze[1]) for _ in range(len(maze))]

    for index, [x, y] in enumerate(l[::-1]):
        res[x][y] = index

    return res


### finish the A* search funciton below
def search(maze, start, end, cost, heuristic):

    # Create start node
    startNode = Node(start, heuristic = heuristic)

    openList = [startNode] #put start node into openList
    closedList = []

    while len(openList) > 0:

        currentNode = getNodeWithLoweastTotalCost(openList)

        closedList.append(currentNode)

        if currentNode.x == end[0] and currentNode.y == end[1]: # reach the end position
            return printPath(currentNode)
            # the end

        # based on current node to explore new consistent nodes
        newNodeExplores = []

        for step in move:
            # new node's location
            x, y = currentNode.x + step[0], currentNode.y + step[1]
            # cannot move out of map or on the wall
            if x < 0 or y < 0 or x > len(maze)-1 or y > len(maze[0])-1 or maze[x][y] == 1:
                continue

            node = Node(position = [x, y], g = currentNode.g + cost, father=currentNode, heuristic = heuristic) # create new node

            if node not in closedList:
                if node in openList:
                    tempNode = openList.pop(openList.index(node))
                    if node.getF() > tempNode.getF():
                        node = tempNode

                # Add the new node to the open list
                openList.append(node)

if __name__ == "__main__":
    res = search(maze, start, end, cost, heuristic)
    print()
    for row in res:
        for col in row:
            print(col, end="\t")
        print("")

""" result - 
[[0, -1, -1, -1, -1, -1],
 [1, -1, -1, -1, -1, -1],
 [2, -1, -1, -1, -1, -1],
 [3, -1,  7,  8,  9, 10],
 [4,  5,  6, -1, -1, 11]]
"""