# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # Make defaultdict of parent.val : [left.val, right.val] for each tree
        # pD = defaultdict(list)
        # qD = defaultdict(list)

        pVisit = set()
        qVisit = set()

        pQ = deque()
        qQ = deque()

        def bfs(n, q):
            q.append(n)
            s = set()
            d = defaultdict(list)
            while q:
                curr = q.popleft()
                if curr: 
                    if curr.left:
                        d[curr.val].append(curr.left.val)
                        q.append(curr.left)
                    else:
                        d[curr.val].append(None)
                    if curr.right:
                        d[curr.val].append(curr.right.val)
                        q.append(curr.right)
                    else:
                        d[curr.val].append(None)
            return d
        pD = bfs(p, pQ)
        qD = bfs(q, qQ)
        # return equality of both defaultdicts
        return pD == qD