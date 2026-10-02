# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        if not root: # no node, returns None
            return None
        root.left = self.removeLeafNodes(root.left, target) # recurse on left and right
        root.right = self.removeLeafNodes(root.right, target)
        
        if root.val == target and not root.left and not root.right: # node is a leaf and its value is target
            return None
        else: # root doesnt have val target and/or isnt a leaf
            return root