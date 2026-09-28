class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        visited = set()
        directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        currArea = 0
        bestArea = 0

        def bfs(r, c):
            area = 0
            land = deque()
            visited.add((r, c))
            land.append((r, c))
            area += 1
            while land:
                currR, currC = land.popleft()
                for dr, dc in directions:
                    nr = currR + dr
                    nc = currC + dc
                    if (nr < 0) or (nr >= len(grid)) or (nc < 0) or (nc >= len(grid[0])) or grid[nr][nc] == 0 or (nr, nc) in visited:
                        continue
                    visited.add((nr, nc))
                    land.append((nr, nc))
                    area += 1
            return area
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1 and (r, c) not in visited:
                    currArea = bfs(r, c)
                bestArea = max(currArea, bestArea)
        return bestArea