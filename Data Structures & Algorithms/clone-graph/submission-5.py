"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None

        visited = {} # visited dict mapping original to clone
        # Iterate over visited adding neighbors of copies
        def bfs(n):
            nextVisit = deque()
            visited[n] = Node(n.val, [])
            nextVisit.append(n)
            while nextVisit:
                curr = nextVisit.popleft()
                for nei in curr.neighbors:
                    if nei not in visited:
                        visited[nei] = Node(nei.val, [])
                        nextVisit.append(nei)
        
        bfs(node)
        for n in visited:
            for nei in n.neighbors:
                visited[n].neighbors.append(visited[nei])
        return visited[node]