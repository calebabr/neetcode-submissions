class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        currArea = 0
        maxArea = 0
        visited = set()
        directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        def bfs(r, c):
            count = 1
            visited.add((r, c))
            neighborhood = deque()
            neighborhood.append((r, c))
            while neighborhood:
                currR, currC = neighborhood.popleft()
                for dr, dc in directions:
                    nr = currR + dr
                    nc = currC + dc
                    if (nr < 0) or (nr >= len(grid)) or (nc < 0) or (nc >= len(grid[0])) or grid[nr][nc] == 0 or (nr, nc) in visited:
                        continue
                    neighborhood.append((nr, nc))
                    visited.add((nr, nc))
                    count += 1
            return count
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if (r, c) not in visited and grid[r][c] == 1:
                    currArea = bfs(r, c)
                    maxArea = max(currArea, maxArea)
        return maxArea
                    