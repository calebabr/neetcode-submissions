class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False
        
        adjL = defaultdict(list)
        for e in edges:
            adjL[e[0]].append(e[1])
            adjL[e[1]].append(e[0])
        
        visited = set()
        nextVisit = deque()
        nextVisit.append([0, -1])
        visited.add(0)
        while nextVisit:
            curr, parent = nextVisit.popleft()
            for nei in adjL[curr]:
                if nei == parent:
                    continue
                if nei in visited:
                    return False
                nextVisit.append([nei, curr])
        return True
        
        