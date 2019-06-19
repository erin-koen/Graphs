
class Stack():
    def __init__(self):
        self.stack = []
    def push(self, value):
        self.stack.append(value)
    def pop(self):
        if self.size() > 0:
            return self.stack.pop()
        else:
            return None
    def size(self):
        return len(self.stack)


'''
BFS and DFS should be memorized. We're going to be using them over and over again. It's never going to be exactly the same, variances based on types of data, shape of the graph, etc. Memorize the baseline and have a strong understanding of it. Memorize key principles AND lines of code. 

Need to be able to transcribe a written spec into code.

Solving Graph Problems:

- translate it into graph terminology
- build your graph
- traverse it

Dense - high proporition of nodes to edges. 
Sparse - low proportion of nodes to edges. 

Cyclic graph - any graph in which you can follow edges and move into a node that's already been inspected.

Acyclic graph - a graph in which the above is impossible. Most trees are acyclic graphs. 

Directed Acyclic Graphs - One way edges. No cycles. 

Adjacency matrices are good for dense graphs rather than sparse graphs. <-- This would make more sense if i'd paid attn for the last 20 min. 

A search is a traversal that stops when the target value is found. 

Breadth-First Search -
Perform a traversal, then return the path.
- create an empty set to store visited nodes
- create an empty queue and enqueue A PATH TO the starting vertex
- while the queue is not empty
    - deque the first path
    - grab the vertext from the end of the path (v = path[-1])
    - if v = target, return path
    - if v not in visited, visited.add(v)
    - then add a path to all of its neighbors tot he back of the queue
    for neightbor  in self.vertices[v]:
        # copy the path
        path_copy = list.path
        # append the neighbord to the back of the copy
        # enqueue the copy


Write a function that takes a 2D binary array and returns the number of 1 islands. An island consists of 1s that are connected to the north, south, east or west. For example:

islands = [[0, 1, 0, 1, 0],
           [1, 1, 0, 1, 1],
           [0, 0, 1, 0, 0],
           [1, 0, 1, 0, 0],
           [1, 1, 0, 0, 0]]

island_counter(islands) # returns 4
'''
# 1. Translate problem into graph terminology: islands are cells. Edges are connectiosn between two adjacent 1s. Unweighted undirected. 
# 2. Build your graphs.
# 3. Traverse your graph. 
def island_counter(matrix):
    
    # create a counter variable
    # walk through each cell in the matrix, if that cell has not been visited:
        # when i reach a 1, do a DFT and mark each as visitied
        # increment counter by 1
    island_count = 0
    
    visited = [] # created a visited matrix
    for i in range(len(matrix)): 
        visited.append([False]* len(matrix[0]))

    for col in range(len(matrix[0])):
        for row in range(len(matrix)):
            if not visited[row][col]:
                if matrix[row][col] == 1:
                    visited = dft(col, row, matrix, visited)
                    island_count+=1


def get_neighbors(v, matrix):
    # look one up, one down, one right, one left. 
    # handle boundaries
    col = v[0] # column
    row = v[1] # row
    neighbors = []
    # Check North
    if row > 0 and matrix[row-1][col] == 1:
        neighbors.append((col, row-1))
    # Check South
    if row < len(matrix-1) and matrix[row+1][col] == 1:
        neighbors.append((col, row+11))
    # Check East:
    if col < len(matrix[0]) - 1 and matrix[row][col+1] == 1:
        neighbors.append((col +1, row))
    # Check East:
    if col > 0 and matrix[row][col-1] == 1:
        neighbors.append((col +1, row))
    
    return neighbors

def dft(col, row, matrix, visited):
    s = Stack()
    s.push((col, row))
    while s.size > 0:
        v = s.pop()
        row = v[0]
        col = v[1]
        if not visited[row][col]:
            visited[row][col] = True
            for neighbor in get_neighbors(v, matrix): # STUB
                s.push(neighbor)
    return visited

islands = [[0, 1, 0, 1, 0],
           [1, 1, 0, 1, 1],
           [0, 0, 1, 0, 0],
           [1, 0, 1, 0, 0],
           [1, 1, 0, 0, 0]]

island_counter(islands) # returns 4

'''
import random

def fisher_yates_shuffle(l):
    for i in range(0, len(l)):
        random_index = random.randint(0, len(l)-1) # random.randint gives you a random interval between i and len(l)-1 inclusive
        l[random_index], l[i] = l[i], l[random_index] # swap
'''
