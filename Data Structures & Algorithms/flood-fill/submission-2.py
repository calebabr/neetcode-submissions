class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        visited = set()
        og = image[sr][sc]
        if og == color:
            return image
        
        def bfs(r, c):
            image[r][c] = color
            visited.add((r, c))
            neighborhood = deque()
            neighborhood.append((r, c))
            while neighborhood:
                currR, currC = neighborhood.popleft()
                for dr, dc in directions:
                    nr = currR + dr
                    nc = currC + dc
                    if (nr < 0) or (nr >= len(image)) or (nc < 0) or (nc >= len(image[0])) or (nr, nc) in visited or image[nr][nc] != og:
                        continue
                    image[nr][nc] = color
                    visited.add((nr, nc))
                    neighborhood.append((nr, nc))
        bfs(sr, sc)
        return image
