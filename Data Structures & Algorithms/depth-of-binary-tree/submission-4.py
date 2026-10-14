# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def bfs(r):
            neighborhood = deque()
            maxLevel = 1
            neighborhood.append((r, 1))
            while neighborhood:
                node, level = neighborhood.popleft()
                if node.right:
                    neighborhood.append((node.right, level + 1))
                    maxLevel = max(maxLevel, level + 1)
                if node.left:
                    neighborhood.append((node.left, level + 1))
                    maxLevel = max(maxLevel, level + 1)
            return maxLevel
        if root == None:
            return 0
        ml = bfs(root)
        return ml