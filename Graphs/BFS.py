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

    def BFS(self, s):

        # Mark all the vertices as not visited
        visited = [False] * (len(self.graph))

        # Create a queue for BFS
        queue = []

        # Mark the source node as
        # visited and enqueue it
        queue.append(s)
        visited[s] = True

        while queue:

            # Dequeue a vertex from
            # queue and print it

            s = queue.pop(0)

            print(s, end=" ")

            # Get all adjacent vertices of the
            # dequeued vertex s. If a adjacent
            # has not been visited, then mark it
            # visited and enqueue it

            for node in self.graph[s]:

                if visited[node] == False:
                    queue.append(node)
                    visited[node] = True


    # Different Version for handling character also
    def BFSV1(self, start):

        # keep track of all visited nodes
        explored = []
        # keep track of nodes to be checked
        queue = [start]

        # keep looping until there are nodes still to be checked
        while queue:
            node = queue.pop(0)

            if node not in explored:
                # add node to list of checked nodes
                explored.append(node)

                for neighbour in self.graph[node]:
                    queue.append(neighbour)
        return explored

g = Graph()
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(2, 3)
g.addEdge(3, 3)

# g.addEdge('A', 'B')
# g.addEdge('A', 'C')
# g.addEdge('A', 'E')
# g.addEdge('B', 'A')
# g.addEdge('B', 'D')
# g.addEdge('B', 'E')
# g.addEdge('C', 'A')
# g.addEdge('C', 'G')
# g.addEdge('C', 'F')
# g.addEdge('D', 'B')
# g.addEdge('E', 'A')
# g.addEdge('E', 'B')
# g.addEdge('E', 'D')
# g.addEdge('F', 'C')
# g.addEdge('G', 'C')

print("Following is BFS from (starting from vertex 2)")
# g.DFS(2)

visited = []

# print(g.BFSV1('A'))

g.BFS(2)