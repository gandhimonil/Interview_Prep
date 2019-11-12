# Python3 Program to print BFS traversal
# from a given source vertex. BFS(int s)
# traverses vertices reachable from s.
from collections import defaultdict


# This class represents a directed graph
# using adjacency list representation
class Graph:

    # Constructor
    def __init__(self):
        # default dictionary to store graph
        self.graph = defaultdict(list)

        # function to add an edge to graph

    def addEdge(self, u, v):
        self.graph[u].append(v)


    def route_between_nodes(self, start, end):

        if start == end:
            return True

        explored = []


        queue = [start]

        while queue:

            element = queue.pop(0)

            if element == end:
                return True

            if element not in explored:
                explored.append(element)

                for neighbour in self.graph[element]:
                    queue.append(neighbour)

        return False

g = Graph()

g.addEdge('A', 'B')
g.addEdge('A', 'C')
g.addEdge('A', 'E')
g.addEdge('B', 'A')
g.addEdge('B', 'D')
g.addEdge('B', 'E')
g.addEdge('C', 'A')
g.addEdge('C', 'G')
g.addEdge('C', 'F')
g.addEdge('D', 'B')
g.addEdge('E', 'A')
g.addEdge('E', 'B')
g.addEdge('E', 'D')
g.addEdge('F', 'C')
g.addEdge('G', 'C')

print(g.route_between_nodes('B', 'F'))


