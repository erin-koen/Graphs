from util import Stack, Queue  # These may come in handy


class Graph:
    # build the graph
    # build edges in revers
    def __init__(self):
        self.vertices = {}
    def add_vertex(self, vertex):
        self.vertices[vertex] = set()
    def add_edge(self, v1, v2):
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            raise IndexError("That vertex does not exist")

def earliest_ancestor(ancestors, starting_node):
    graph = Graph()
    for pair in ancestors:
        graph.add_vertex(pair[0])
        graph.add_vertex(pair[1])
        # build edges in reverse
        graph.add_edge(pair[1], pair[0])
    q = Queue()
    q.enqueue([starting_node])
    # track the longest path length and the earliest ancestor node
    max_path_length = 1
    earliest_ancestor = -1
    # do a Breadth First Search from starting_node to each other node
    while q.size() > 0:
        path = q.dequeue()
        v = path[-1]
        if len(path) >= max_path_length and v < earliest_ancestor or (len(path) > max_path_length):
            earliest_ancestor = v
            max_path_length = len(path)
        for neighbor in graph.vertices[v]:
            path_copy = list(path)
            path_copy.append(neighbor)
            q.enqueue(path_copy)
    return earliest_ancestor
    # return the node at the end of the longest path