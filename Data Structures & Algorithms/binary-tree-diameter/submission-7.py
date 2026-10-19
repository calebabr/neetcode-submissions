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

            if not root:
                return 0
            
            leftDiam = dfs(r.left)
            rightDiam = dfs(r.right)
            diam = max(diam, leftDiam + rightDiam)
        
            return 1 + max(leftDiam, rightDiam)

        dfs(root)
        return diam