# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        diam = 0

        def dfs(r):
            nonlocal diam

            if not r:
                return 0
            
            leftHeight = dfs(r.left)
            rightHeight = dfs(r.right)
            diam = max(diam, leftHeight + rightHeight)

            return 1 + max(leftHeight, rightHeight)
        dfs(root)
        return diam