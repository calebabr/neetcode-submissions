class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        directions = [[-1, 0], [1, 0], [0, 1], [0, -1]]
        res = []
        def bfs(r, c):
            # At each r, c we keep going as far as we can. Return true if we ever overflow during bfs. If not, false
            visited = set()
            oceanMap = {'P': False, 'A': False}
            neighborhood = deque()
            visited.add((r, c))
            neighborhood.append((r, c))
            while neighborhood:
                currR, currC = neighborhood.popleft()
                for dr, dc in directions:
                    nr, nc = currR + dr, currC + dc
                    # Traverse to next
                    if (nr >= 0) and (nr < len(heights)) and (nc >= 0) and (nc < len(heights[0])) and heights[currR][currC] >= heights[nr][nc] and (nr, nc) not in visited:
                        visited.add((nr, nc))
                        neighborhood.append((nr, nc))
                    # Check if we've overflowed to either ocean
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
            