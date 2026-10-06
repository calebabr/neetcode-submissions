class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        res = []
        def bfs(r, c):
            visited = set()
            oceanMap = {'P' : False, 'A': False} # P is top or left, A is bottom or right
            neighborhood = deque()
            neighborhood.append((r, c))
            visited.add((r, c))
            while neighborhood:
                currR, currC = neighborhood.popleft()
                for dr, dc in directions:
                    nr = currR + dr
                    nc = currC + dc
                    if (nr >= 0) and (nr < len(heights)) and (nc >= 0) and (nc < len(heights[0])) and heights[currR][currC] >= heights[nr][nc] and (nr, nc) not in visited:
                        visited.add((nr, nc))
                        neighborhood.append((nr, nc))
                    if (nr < 0) or (nc < 0):
                        oceanMap['P'] = True
                        continue
                    if (nr >= len(heights)) or (nc >= len(heights[0])):
                        oceanMap['A'] = True
                        continue
            for ocean in oceanMap:
                if not oceanMap[ocean]:
                    return False
            return True
        for r in range(len(heights)):
            for c in range(len(heights[0])):
                if bfs(r, c):
                    res.append([r, c])
        return res
