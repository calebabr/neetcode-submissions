class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        visited = set()
        numFresh = 0
        rotten = deque()
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 2:
                    rotten.append(((r, c), 0))
                if grid[r][c] == 1:
                    numFresh += 1
        
        def bfs(num1):
            time = 0
            while rotten:
                if num1 == 0:
                    break
                coord, time = rotten.popleft()
                for dr, dc in directions:
                    nr = coord[0] + dr
                    nc = coord[1] + dc
                    if (nr < 0) or (nr >= len(grid)) or (nc < 0) or (nc >= len(grid[0])) or (nr, nc) in visited or grid[nr][nc] != 1:
                        continue
                    if (nr, nc) not in visited and grid[nr][nc] == 1:
                        grid[nr][nc] == 2
                        visited.add((nr, nc))
                        rotten.append(((nr, nc), time + 1))
                        num1 -= 1
                        if num1 == 0:
                            time += 1
                            break
            return time, num1
        time, number = bfs(numFresh)

        if number != 0:
            return -1
        else:
            return time
                 