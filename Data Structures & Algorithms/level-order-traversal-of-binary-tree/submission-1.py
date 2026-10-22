# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        qVisit = deque()
        qVisit.append(root)
        res = []
        while qVisit:
            levelSize = len(qVisit)
            currLevel = []
            for i in range(levelSize):
                curr = qVisit.popleft()
                if curr:
                    currLevel.append(curr.val)
                    qVisit.append(curr.left)
                    qVisit.append(curr.right)  
            if currLevel:
                res.append(currLevel)
        return res