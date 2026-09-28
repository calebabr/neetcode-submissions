class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        perimeter = 0
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 0:
                    continue
                og = 4
                for d in directions:
                    nr = r + d[0]
                    nc = c + d[1]
                    if ((nr >= 0) and (nc >= 0) and (nr < len(grid)) and (nc < len(grid[0]))) and grid[nr][nc] == 1 :
                        og -=1
                perimeter += og
        return perimeter
