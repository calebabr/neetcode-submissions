class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        visited = set()
        directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        perimeter = 0
        def bfs(source): # in form r, c
            land = deque()
            visited.add(source)
            land.append(source)
            while land:
                contrib = 4
                currR, currC = land.popleft()
                for dr, dc in directions:
                    nr = currR + dr
                    nc = currC + dc
                    if (nr < 0) or (nr >= len(grid)) or (nc < 0) or (nc >= len(grid[0])) or grid[nr][nc] != 1 or (nr, nc) in visited:
                        continue
                    visited.add((nr, nc))
                    land.append((nr, nc))
                    contrib -= 1
                contrib += contrib
            return contrib
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1 and (r, c) not in visited:
                    perimeter += bfs((r, c))
        return perimeter

