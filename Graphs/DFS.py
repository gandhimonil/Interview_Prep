# Python3 program to print DFS traversal
# from a given given graph
from collections import defaultdict


# This class represents a directed graph using
# adjacency list representation
class Graph:

    # Constructor
    def __init__(self):

        # default dictionary to store graph
        self.graph = defaultdict(list)

    def addEdge(self, u, v):
        self.graph[u].append(v)

    # The function to do DFS traversal. It uses
    # recursive DFSUtil()
    def DFS(self, v):

        # Mark all the vertices as not visited

        visited = [False] * len(self.graph)

        self.DFSUtil(v,visited)

    def DFSUtil(self, v, visited):

        # Mark the current node as visited
        # and print it

        visited[v] = True

        print(v, end=' ')

        # Recur for all the vertices
        # adjacent to this vertex

        for i in self.graph[v]:

            if visited[i] == False:
                self.DFSUtil(i, visited)

    # Different Version for handling character also
    def DFSV1(self, visited, graph, node):

        if node not in visited:
            print(node)
            visited.append(node)
            for neighbour in self.graph[node]:
                self.DFSV1(visited,self.graph,neighbour)


# Driver code

# Create a graph given
# in the above diagram
g = Graph()
# g.addEdge(0, 1)
# g.addEdge(0, 2)
# g.addEdge(1, 2)
# g.addEdge(2, 0)
# g.addEdge(2, 3)
# g.addEdge(3, 3)

g.addEdge('A', 'B')
g.addEdge('A', 'C')
g.addEdge('B', 'D')
g.addEdge('B', 'E')
g.addEdge('C', 'F')
g.addEdge('E', 'F')



print("Following is DFS from (starting from vertex 2)")
# g.DFS(2)

visited = []

g.DFSV1(visited,g,'A')





