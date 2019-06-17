"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy

class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}
    def add_vertex(self, vertex):
        self.vertices[vertex]=set()

    def add_edge(self, v1, v2):
        self.vertices[v1].add(v2)

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """

        # create an empty set to store visited nodes
        visited = set()
        # create an empyt queue and enqueue the starting vertex
        q = Queue()
        q.enqueue(starting_vertex)
        printable= []
        while q.size()>0: # while the queue is not empty...
            
            v = q.dequeue() # dequeue the first vertex and set it to v for vertex
            if v not in visited: # if that vertex has not been visited
                visited.add(v) # mark it as visited
                printable.append(v) # do the thing we're supposed to do
                for neighbor in self.vertices[v]: # find all of its neighbors 
                    q.enqueue(neighbor) # add them to the queue
        print('bft: ', printable)
   

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        visited = set() # declare a new set to keep track of visits
        stack = Stack() # declare a new stack to keep track of order in which to visit
        stack.push(starting_vertex) # push starting index into the stack to start the while loop
        printable = []
        while stack.size()>0: # while there are vertices in the stack
            v = stack.pop() # take one off the end
            if v not in visited: # if it hasn't been visited
                visited.add(v) # note it's been visited
                printable.append(v) # do the thing we need to do
                for neighbor in self.vertices[v]: # loop through its neighbors
                    stack.push(neighbor) # add them to the stack
        print('dft: ', printable)        

    def dft_recursive(self, starting_vertex, visited = None):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        This should be done using recursion.
        """
        # keep track of where we've been
        if visited is None:
            visited = set()

        visited.add(starting_vertex)

        print(starting_vertex)
        
        for v in self.vertices[starting_vertex]: #loop through children
            #set base case
            if v not in visited:
                self.dft_recursive(v, visited) # call the function on each and pass increasingly large visited down each time


    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        
        Understand - need to take in two vertices, find all of the possible paths between them, return the length of the shortest 
        bfs means LIFO. Add each vertex to a list as it's traversed. When list -1 == destination vertex, list is complete. how do you get traversal to run multiple times?

        """
        visited = set()
        # create an empyt queue and enqueue the starting vertex
        q = Queue()
        q.enqueue(starting_vertex)
        printable= []
        while q.size()>0: # while the queue is not empty...
            
            v = q.dequeue() # dequeue the first vertex and set it to v for vertex
            if v not in visited: # if that vertex has not been visited
                visited.add(v) # mark it as visited
                printable.append(v) # do the thing we're supposed to do
                for neighbor in self.vertices[v]: # find all of its neighbors 
                    q.enqueue(neighbor) # add them to the queue
        print('bft: ', printable)        


    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        pass  # TODO





if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    print(graph.vertices)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    graph.dft(1)

    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    graph.bft(1)

    '''
    Valid DFT recursive paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print(graph.dfs(1, 6))
