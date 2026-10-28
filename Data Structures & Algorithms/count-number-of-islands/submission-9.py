class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        numIslands = 0
        visited = set()

        def bfs(r, c):
            nextVisit = deque()
            nextVisit.append((r, c))
            # grid[r][c] = '1'
            while nextVisit:
                currR, currC = nextVisit.popleft()
                grid[currR][currC] = '0'
                # visited.add((currR, currC))
                for dr, dc in directions:
                    nr, nc = currR + dr, currC + dc
                    if (nr < 0) or (nr >= len(grid)) or (nc < 0) or (nc >= len(grid[0])) or (nr, nc) in visited or grid[nr][nc] == "0":
                        continue
                    # visited.add((nr, nc))
                    nextVisit.append((nr, nc))
                    grid[nr][nc] = '0'
        
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == '1':
                    bfs(r, c)
                    numIslands += 1
        return numIslands