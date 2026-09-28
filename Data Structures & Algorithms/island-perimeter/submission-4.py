class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        visited = set()
        directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        def bfs(source): # in form r, c
            land = deque()
            visited.add(source)
            land.append(source)
            perimeter = 0

            while land:
                # contrib = 4
                currR, currC = land.popleft()
                for dr, dc in directions:
                    nr = currR + dr
                    nc = currC + dc
                    if (nr < 0) or (nr >= len(grid)) or (nc < 0) or (nc >= len(grid[0])) or grid[nr][nc] == 0:
                        perimeter += 1
                    elif (nr, nc) not in visited:
                        visited.add((nr, nc))
                        land.append((nr, nc))
            return perimeter
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    return bfs((r, c))
        return 0

