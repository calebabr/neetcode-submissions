class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        visited = set()
        directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        # Any cell automatically contributes 4 to perimeter. 
        def bfs(src):
            perimeter = 0
            neighborhood = deque()
            neighborhood.append(src)
            visited.add(src)
            while neighborhood:
                currR, currC = neighborhood.popleft()
                for dr, dc in directions:
                    nr = currR + dr
                    nc = currC + dc
                    if (nr < 0) or (nr >= len(grid)) or (nc < 0) or (nc >= len(grid[0])) or grid[nr][nc] == 0: 
                        perimeter += 1
                    elif (nr, nc) not in visited:
                        visited.add((nr, nc))
                        neighborhood.append((nr, nc))
            return perimeter
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    return bfs((r, c))
        return 0