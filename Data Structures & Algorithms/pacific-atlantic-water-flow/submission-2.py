class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        directions = [[-1, 0], [1, 0], [0, 1], [0, -1]]
        res = []
        pacificFlow = set()
        atlanticFlow = set()

        pacificVisit = deque()
        atlanticVisit = deque()

        for r in range(len(heights)):
            pacificVisit.append((r, 0)) # left border
            pacificFlow.add((r, 0))

            atlanticVisit.append((r, len(heights[0]) - 1)) # right border
            atlanticFlow.add((r, len(heights[0])- 1))
        
        for c in range(len(heights[0])):
            pacificVisit.append((0, c)) # top border
            pacificFlow.add((0, c))

            atlanticVisit.append((len(heights) - 1, c)) # bottom border
            atlanticFlow.add((len(heights) - 1, c))
        
        def bfs(q, s):
            while q:
                currR, currC = q.popleft()
                for dr, dc in directions:
                    nr, nc = currR + dr, currC + dc
                    if (nr >= 0) and (nr < len(heights)) and (nc >= 0) and nc < len(heights[0]) and heights[currR][currC] <= heights[nr][nc] and (nr, nc) not in s:
                        q.append((nr, nc))
                        s.add((nr, nc))
        bfs(pacificVisit, pacificFlow)
        bfs(atlanticVisit, atlanticFlow)

        for r in range(len(heights)):
            for c in range(len(heights[0])):
                if (r, c) in pacificFlow and (r, c) in atlanticFlow:
                    res.append([r, c])
        return res