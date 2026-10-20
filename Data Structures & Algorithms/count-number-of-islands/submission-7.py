class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        numIslands = 0

        def bfs(r, c):
            nextVisit = deque()
            # Process this node (append, visit)
            nextVisit.append((r, c))
            grid[r][c] = '0'
            while nextVisit:
                currR, currC = nextVisit.popleft()
                for dr, dc in directions:
                    nr, nc = dr + currR, dc + currC
                    if (nr >= 0) and (nr < len(grid)) and (nc >= 0) and (nc < len(grid[0])) and grid[nr][nc] == '1': # (append, visit)
                        nextVisit.append((nr, nc))
                        grid[nr][nc] = '0'
        
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == '1':
                    bfs(r, c)
                    numIslands += 1
        
        return numIslands