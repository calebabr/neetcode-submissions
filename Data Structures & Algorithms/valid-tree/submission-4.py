class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # Trees are graphs with n vertices that are connected, acyclic and n - 1 edges.
        if len(edges) > (n - 1):
            return False

        adjList = defaultdict(list)
        
        # Make adjacency list
        for e in edges:
            adjList[e[0]].append(e[1])
            adjList[e[1]].append(e[0])

        visited = set()
        qVisit = deque()
        qVisit.append([0, -1])
        visited.add(0)

        while qVisit:
            node, parent = qVisit.popleft()
            for nei in adjList[node]:
                if nei == parent:
                    continue
                if nei in visited:
                    return False
                visited.add(nei)
                qVisit.append((nei, node))

        return (len(visited) == n)