# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # 3 Base cases
        # 1) Both nodes DON'T exist => equal
        if not p and not q:
            return True
        # 2) One node exists but another doesnt => not equal
        if not p or not q:
            return False
        # 3) both exist but have different values => not equal
        if p.val != q.val:
            return False
        # recurse on both left and right subtrees
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)