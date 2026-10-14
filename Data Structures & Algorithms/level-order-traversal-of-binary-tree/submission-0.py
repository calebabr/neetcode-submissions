# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        if not root:
            return res
        nextVisit = deque()
        nextVisit.append(root)

        while nextVisit:
            qLen = len(nextVisit)
            level = []
            for i in range(qLen):
                curr = nextVisit.popleft()
                if curr:
                    level.append(curr.val)
                    nextVisit.append(curr.left)
                    nextVisit.append(curr.right)
            if level:
                res.append(level)
        return res
        
        
