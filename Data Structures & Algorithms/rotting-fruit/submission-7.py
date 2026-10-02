class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        rotten = deque()
        visited = set()
        num1 = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 2:
                    rotten.append(((r, c), 0))
                if grid[r][c] == 1:
                    num1 += 1
        def bfs(number1):
            time = 0
            while rotten:
                coord, time = rotten.popleft()
                visited.add(coord)
                for dr, dc in directions:
                    nr = coord[0] + dr
                    nc = coord[1] + dc
                    if (nr < 0) or (nr >= len(grid)) or (nc < 0) or (nc >= len(grid[0])) or (nr, nc) in visited or grid[nr][nc] != 1:
                        continue
                    if (nr, nc) not in visited and grid[nr][nc] == 1:
                        visited.add((nr, nc))
                        rotten.append(((nr, nc), time + 1))
                        number1 -= 1
            return time, number1
        timeTaken, num = bfs(num1)
        num1 = num
        if num1 != 0:
            return -1
        else:
            return timeTaken