# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        if not root: # Base case, if there is no root, return None
            return None
        if not root.left and not root.right and root.val == target: # if these root is a leaf with given value, delete it
            return None

        root.left = self.removeLeafNodes(root.left, target) # recurse on left
        root.right = self.removeLeafNodes(root.right, target) # recurse on right

        if root.val == target and not root.left and not root.right: #after updates, check if this root is now a leaf and has target value
            root = None
        else:
            return root