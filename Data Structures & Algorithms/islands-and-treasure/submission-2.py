class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        nextTravel = deque()
        
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 0:
                    nextTravel.append(((r, c), 0))
        
        def bfs():
            while nextTravel:
                coord, time = nextTravel.popleft()
                for dr, dc in directions:
                    nr, nc = coord[0] + dr, coord[1] + dc
                    if (nr < 0) or (nr >= len(grid)) or (nc < 0) or (nc >= len(grid[0])) or (grid[nr][nc] != 2**31 - 1):
                        continue
                    grid[nr][nc] = time + 1
                    nextTravel.append(((nr, nc), time + 1))
        
        bfs()
        