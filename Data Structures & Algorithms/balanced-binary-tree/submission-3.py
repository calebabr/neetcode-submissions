# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(r):
            if not r: # base case. No node = balanced and height 0
                return [True, 0]
            
            left = dfs(r.left)
            right = dfs(r.right) # recurse on left and right

            balanced = left[0] and right[0] and abs(left[1] - right[1]) <= 1 #balanced if both are balanced and the difference in heights is at most 1
            return [balanced, 1 + max(left[1], right[1])]
        
        return dfs(root)[0]