# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        diam = 0
        # diam of subtree at root r = length of longest path on left subtree + length of longest path on right subtree
        def dfs(r):
            nonlocal diam

            if not r:
                return 0 # base case. 
            
            leftHeight = dfs(r.left) # get longest heights on both
            rightHeight = dfs(r.right)
            diam = max(diam, leftHeight + rightHeight) # diam is largest possible

            return 1 + max(leftHeight, rightHeight) # return diam for this node
        dfs(root)
        return diam