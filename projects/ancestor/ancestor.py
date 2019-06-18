from util import Stack, Queue  # These may come in handy

'''
- translate the problem into graph terminology
    - adjacency list seems most reasonable
    - directed, acyclical graph
    - oldest ancestor will be the longest path between input integer and a leaf


- build the graph
    - goign to use the graph template from yesterday
- traverse the graph
    - need to do breadth first but not return when we hit the target. Store all paths in an array. figure that out when you get to it. 
'''


class Family:
    def __init__(self):
        self.vertices = {}
    def add_vertex(self, vertex):
        self.vertices[vertex] = set()
    def add_edge(self, v1, v2):
        self.vertices[v1].add(v2)
    
    def findEarliest(self, vert, visited = None, path = None):
        # given a vertice, find the longest path between it and an ancestor. 
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
        print(f'path: {path}')
        return path[-1]


# assume that the input is a list of tuples
def makeFamily(arr):
    fam = Family()
    for item in arr:
        if item[0] not in fam.vertices:
            fam.add_vertex(item[0])
        if item[1] not in fam.vertices:
            fam.add_vertex(item[1])
        # need to flip the graph, and edges are unidirectional, so i'm goign to do something crazy and flip these
        fam.add_edge(item[1], item[0])
    print(fam.vertices)
    return fam



def earliest_ancestor(arr, num):
    new_fam = makeFamily(arr)
    visited = new_fam.findEarliest(num)
    print(f'VISITED: {visited}')
    return visited

test_ancestors = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]

makeFamily(test_ancestors)