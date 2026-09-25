class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:

        # record og (original) color of (sr, sc) change color of (sr, sc) to color  
        og = image[sr][sc]
        if og == color:
            return image
        # recursive dfs(r, c) for row column:
        def helpDFS(r, c):
            if (r < 0) or (r >= (len(image))) or (c < 0) or (c >= len(image[0])) or image[r][c] != og:
                return
            else:                    
                image[r][c] = color
                helpDFS(r + 1, c)
                helpDFS(r - 1, c)
                helpDFS(r, c + 1)
                helpDFS(r, c - 1)
        # recursive DFS floodFill on every neighboring pixel ONLY if it is the og 
        # color of sr sc
        # 4 adjacent neighboring
        # (sr, sc + 1) (sr, sc - 1)
        # (sr + 1, sc) (sr - 1, sc)
        # base case is do nothing because it is not og color
        helpDFS(sr, sc)
        return image
        
        