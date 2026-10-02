# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        def postOrder(n):
            if not n:
                return
            postOrder(n.left)
            postOrder(n.right)
            res.append(n.val)
        
        postOrder(root)
        return res