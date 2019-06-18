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



'''