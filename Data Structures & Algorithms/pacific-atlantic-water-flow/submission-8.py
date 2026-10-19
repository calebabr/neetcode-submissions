class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        res = []

        pacificSet = set()
        atlanticSet = set()

        pacificQueue = deque()
        atlanticQueue = deque()
        # Populate both sets
        for r in range(len(heights)):
            pacificSet.add((r, 0))
            pacificQueue.append((r, 0))

            atlanticSet.add((r, len(heights) - 1))
            atlanticQueue.append((r, len(heights) - 1))
        for c in range(len(heights[0])):
            pacificSet.add((0, c))
            pacificQueue.append((0, c))

            atlanticSet.add((len(heights[0]) - 1, c))
            atlanticQueue.append((len(heights[0]) - 1, c))
        
        def bfs(q, s):
            while q:
                currR, currC = q.popleft()
                for dr, dc in directions:
                    nr, nc = currR + dr, currC + dc
                    if (nr >= 0) and (nr < len(heights)) and (nc >= 0) and (nc < len(heights[0])) and heights[currR][currC] <= heights[nr][nc] and (nr, nc) not in s:
                        q.append((nr, nc))
                        s.add((nr, nc))
        # Run bfs for both
        bfs(pacificQueue, pacificSet)
        bfs(atlanticQueue, atlanticSet)

        # O(m*n) to check if in both sets
        for r in range(len(heights)):
            for c in range(len(heights)):
                if (r, c) in pacificSet and (r, c) in atlanticSet:
                    res.append([r, c])
        return res