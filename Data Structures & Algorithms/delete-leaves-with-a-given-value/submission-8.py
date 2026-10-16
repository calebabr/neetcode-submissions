# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def removeLeafNodes(self, root: TreeNode | None, target: int) -> TreeNode | None:
        if not root: # base case
            return None
        
        root.right = self.removeLeafNodes(root.right, target) # recurse on right and left subtree
        root.left = self.removeLeafNodes(root.left, target)

        if root.val == target and not root.left and not root.right: # if after updates, check
            root = None
        return root