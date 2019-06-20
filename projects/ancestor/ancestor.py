from util import Stack, Queue  # These may come in handy

'''
- translate the problem into graph terminology
    - adjacency list seems most reasonable
    - directed, acyclical graph
    - oldest ancestor will be the longest path between input integer and a leaf


- build the graph
    - goign to use the graph template from yesterday
- traverse the graph
    - Depth first to go straight to the bottom of the graph
'''


class Family:
    def __init__(self):
        self.vertices = {}
    def add_vertex(self, vertex):
        self.vertices[vertex] = set()
    def add_edge(self, v1, v2):
        self.vertices[v1].add(v2)
    
    def findEarliest(self, vert, visited = None, path = None):
        # need to keep track of how many loops through the array each child takes to get there.
        # given a vertice, find the longest path between it and an ancestor. 
        # Recursive attempt
        if visited is None:
            visited = set()
        if path is None:
            path = []
        visited.add(vert) 
        path.append(vert)
        for v in self.vertices[vert]:
            print('looping starts: ', v)
            if v not in visited:
                self.findEarliest(v, visited, path)
            print(f'line 37 path: {path}')
        if self.vertices[vert] == set():
            return -1
        else:
            return path[-1]
        

# assume that the input is a list of tuples in (child, parent) order
def makeFamily(arr):
    fam = Family()
    for item in arr:
        if item[0] not in fam.vertices:
            fam.add_vertex(item[0])
        if item[1] not in fam.vertices:
            fam.add_vertex(item[1])
        # need to flip the graph, and edges are unidirectional, so i'm goign to do something crazy and flip these
        fam.add_edge(item[1], item[0])
    return fam



def earliest_ancestor(arr, num):
    new_fam = makeFamily(arr)
    oldest = new_fam.findEarliest(num)
    print(f'Oldest: {oldest}')
    return oldest
