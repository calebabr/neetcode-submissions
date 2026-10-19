class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        numFresh = 0
        visited = set()
        rotten = deque()

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 2:
                    rotten.append(((r, c), 0))
                    visited.add((r, c))
                if grid[r][c] == 1:
                    numFresh += 1
        
        def bfs(fresh):
            time = 0
            while rotten:
                currCoord, time = rotten.popleft()
                for dr, dc in directions:
                    nr, nc = currCoord[0] + dr, currCoord[1] + dc
                    if (nr < 0) or (nr >= len(grid)) or (nc < 0) or (nc >= len(grid[0])) or grid[nr][nc] != 1 or (nr, nc) in visited:
                        continue
                    grid[nr][nc] = 2
                    rotten.append(((nr, nc), time + 1))
                    fresh -= 1
                    if fresh == 0:
                        return time, 0

            return time, fresh
        
        totalTime, numFresh = bfs(numFresh)
        if numFresh != 0:
            return -1
        return totalTime