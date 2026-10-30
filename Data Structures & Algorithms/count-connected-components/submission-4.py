class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # Let E be len(edges)
        numCom = 0

        # Create adjacency list
        adjList = defaultdict(list)
        for e in edges: #O(E) time
            adjList[e[0]].append(e[1])
            adjList[e[1]].append(e[0])

        # define bfs from a node
        visited = set()
        def bfs(n):
            nextVisit = deque()
            nextVisit.append(n)
            visited.add(n)
            while nextVisit:
                curr = nextVisit.popleft()
                for nei in adjList[curr]:
                    if nei not in visited:
                        nextVisit.append(nei)
                        visited.add(nei)
                
        # iterate from 0 to n, run bfs at iteration if has not yet been visited
        for i in range(n):
            if i not in visited:
                bfs(i)
                numCom += 1

        return numCom