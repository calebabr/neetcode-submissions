# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        def preOrder(n):
            if not n:
                return
            res.append(n.val)
            preOrder(n.left)
            preOrder(n.right)

        preOrder(root)
        return res