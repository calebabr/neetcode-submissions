class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        nextTravel = deque()
        visited = set()
        directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 0:
                    nextTravel.append(((r, c), 0))
                    visited.add((r, c))
        def bfs():
            while nextTravel:
                coord, level = nextTravel.popleft()
                for dr, dc in directions:
                    nr = coord[0] + dr
                    nc = coord[1] + dc
                    if (nr < 0) or (nr >= len(grid)) or (nc < 0) or (nc >= len(grid[0])) or grid[nr][nc] == -1 or (nr, nc) in visited:
                        continue
                    visited.add((nr, nc))
                    nextTravel.append(((nr, nc), level + 1))
                    grid[nr][nc] = level + 1
        bfs()