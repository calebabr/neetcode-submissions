class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        numCom = 0
        # Create adjacency list
        adjList = defaultdict(list)
        for e in edges:
            adjList[e[0]].append(e[1])
            adjList[e[1]].append(e[0])

        # define bfs from a node
        visited = set()
        def bfs(node):
            nextVisit = deque()
            nextVisit.append(node)
            while nextVisit:
                # Process Node
                curr = nextVisit.popleft()
                visited.add(curr)
                # Append all neighbors to nextVisit if not yet visited
                for nei in adjList[curr]:
                    if nei not in visited:
                        nextVisit.append(nei)
        
        # iterate from 0 to n, run bfs at iteration if has not yet been visited
        for i in range(n):
            if i not in visited:
                bfs(i)
                numCom += 1

        return numCom