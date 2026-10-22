class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # Trees are graphs with n vertices that are connected, acyclic and n - 1 edges.
        numEdges = 0
        visited = set()
        adjList = defaultdict(list)
        qVisit = deque()

        # Make adjacency list
        for e in edges:
            adjList[e[0]].append(e[1])
            # adjList[e[1]].append(e[0])
         
        qVisit.append(0)
        visited.add(0)

        while qVisit:
            curr = qVisit.popleft()
            visited.add(curr)
            for nei in adjList[curr]:
                if nei not in visited:
                    qVisit.append(nei)
                    numEdges += 1
        
        print("Vertices: ", n)
        print("Edges Calculated: ", numEdges)
        print("Vertices visited: ", len(visited))
        return (numEdges == n - 1)