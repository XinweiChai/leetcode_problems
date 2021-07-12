from collections import defaultdict, deque


class Graph:
    def __init__(self, V: int = 0):  # Constructor
        self.V = V  # No. of vertices
        self.adj = [[] for _ in range(V)]  # adjacency lists
        self.graph = defaultdict(list)

    def addEdge(self, v: int, w: int):  # to add an edge to graph
        # self.adj[v].append(w)  # Add w to v’s list.
        self.graph[v].append(w)

    # prints all not yet visited vertices reachable from s
    def DFS(self, s: int):  # prints all vertices in DFS manner from a given source.
        visited = [False] * self.V

        # Create a stack for DFS
        stack = [s]
        while stack:
            # Pop a vertex from stack and print it
            s = stack.pop()

            # Stack may contain same vertex twice. So
            # we need to print the popped item only
            # if it is not visited.
            if not visited[s]:
                print(s, end=' ')
                visited[s] = True

            # Get all adjacent vertices of the popped vertex s
            # If a adjacent has not been visited, then push it
            # to the stack.
            for node in self.adj[s]:
                if not visited[node]:
                    stack.append(node)

    def BFS(self, s):
        visited = [False] * len(self.graph)

        # Create a queue for BFS
        queue = deque()

        # Mark the source node as
        # visited and enqueue it
        queue.append(s)
        visited[s] = True

        while queue:

            # Dequeue a vertex from
            # queue and print it
            s = queue.popleft()
            print(s, end=" ")

            # Get all adjacent vertices of the
            # dequeued vertex s. If a adjacent
            # has not been visited, then mark it
            # visited and enqueue it
            for i in self.graph[s]:
                if not visited[i]:
                    queue.append(i)
                    visited[i] = True

    def isCyclicUtil(self, v, visited, recStack):

        # Mark current node as visited and
        # adds to recursion stack
        visited[v] = True
        recStack[v] = True

        # Recur for all neighbours
        # if any neighbour is visited and in
        # recStack then graph is cyclic
        for neighbour in self.graph[v]:
            if visited[neighbour] == False:
                if self.isCyclicUtil(neighbour, visited, recStack) == True:
                    return True
            elif recStack[neighbour] == True:
                return True

        # The node needs to be poped from
        # recursion stack before function ends
        recStack[v] = False
        return False

    # Returns true if graph is cyclic else false
    def isCyclic(self):
        visited = [False] * (self.V + 1)
        recStack = [False] * (self.V + 1)
        for node in range(self.V):
            if visited[node] == False:
                if self.isCyclicUtil(node, visited, recStack) == True:
                    return True
        return False

    def has_cycle(self):
        visited = set()
        for i in self.graph:
            if i in visited:
                continue
            stack = [i]
            visited_in_round = {i}
            while stack:
                cur = stack.pop()
                for j in self.graph[cur]:
                    if j in visited_in_round:
                        return True
                    visited_in_round.add(j)
                    visited.add(j)
                    stack.append(j)
        return False


g = Graph()
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(2, 3)
g.addEdge(3, 3)

print("Following is Breadth First Traversal"
      " (starting from vertex 2)")
g.BFS(2)
print(g.has_cycle())