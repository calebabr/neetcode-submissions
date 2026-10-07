class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        currArea = 0
        maxArea = 0
        directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        visited = set()

        def bfs(r, c):
            count = 1
            land = deque()
            visited.add((r, c))
            land.append((r, c))
            while land:
                currR, currC = land.popleft()
                for dr, dc in directions:
                    nr = currR + dr
                    nc = currC + dc
                    if (nr < 0) or (nr >= len(grid)) or (nc < 0) or (nc >= len(grid[0])) or (nr, nc) in visited or grid[nr][nc] == 0:
                        continue
                    count += 1
                    visited.add((nr, nc))
                    land.append((nr, nc))
            return count
        
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1 and (r, c) not in visited:
                    currArea = bfs(r, c)
                    maxArea = max(currArea, maxArea)
        return maxArea