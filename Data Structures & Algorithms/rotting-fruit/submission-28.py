class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        numFresh = 0
        # visited = set()
        nextVisit = deque()
        rows, cols = len(grid), len(grid[0])

        # Populate nextVisit with all starting rotten with level 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    numFresh += 1
                if grid[r][c] == 2:
                    nextVisit.append(((r, c), 0)) # level 0 => rotten at time 0
        if numFresh == 0:
            return 0
        # helper bfs with input number fresh, returns number of fresh and max level depth after running. while nextVisit is nonempty, pop a rotten cell with its level, process by adding it to visited, check all neighbors if within bounds, not visited, and a 1. Change to 2, decrement fresh, append to deque as its now rotten. 
        def bfs(fresh):
            level = 0
            while nextVisit:
                coord, level = nextVisit.popleft()
                # visited.add(coord)
                for dr, dc in directions:
                    nr, nc = coord[0] + dr, coord[1] + dc
                    if (nr >= 0) and (nr < rows) and (nc >= 0) and (nc < cols) and (nr, nc) and grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        nextVisit.append(((nr, nc), level + 1))
                        fresh -= 1
                        if fresh == 0:
                            return 0, level + 1
            return fresh, level
        
        numFresh, time = bfs(numFresh)
        if numFresh != 0:
            return -1
        return time

