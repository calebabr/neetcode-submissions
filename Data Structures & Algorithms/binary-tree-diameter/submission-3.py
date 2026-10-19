# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        diam = 0
        if not root:
            return 0
        
        def bfs(r):
            maxPath = 0
            nextVisit = deque()
            nextVisit.append((r, maxPath))
            while nextVisit:
                curr, l = nextVisit.popleft()
                if curr.left:
                    nextVisit.append((curr.left, l + 1))
                    maxPath = max(maxPath, l + 1)
                if curr.right:
                    nextVisit.append((curr.right, l + 1))
                    maxPath = max(maxPath, l + 1)
                if not curr.left and not curr.right:
                    maxPath = max(maxPath, l)
            return maxPath

        diam = bfs(root)
        return diam