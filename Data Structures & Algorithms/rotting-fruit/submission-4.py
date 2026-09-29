class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        num1 = 0
        rotten = deque()
        visited = set()
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    num1 += 1
                if grid[r][c] == 2:
                    rotten.append(((r, c), 0))
        if num1 == 0:
            return 0
        def bfs(q, num):
            n = num
            if not q:
                return 0, -1
            while q:
                curr = q.popleft()
                currCoord = curr[0]
                currTime = curr[1]                
                visited.add(currCoord)
                for dr, dc in directions:
                    nr = currCoord[0] + dr
                    nc = currCoord[1] + dc
                    if (nr >= 0) and (nr < len(grid)) and (nc >= 0) and (nc < len(grid[0])) and grid[nr][nc] == 1 and (nr, nc) not in visited:
                        grid[nr][nc] == 2
                        q.append(((nr, nc), currTime + 1))
                        visited.add((nr, nc))
                        n -= 1
            return currTime, n
        answer = bfs(rotten, num1)
        if 0 == answer[1]:
            return answer[0]
        return -1