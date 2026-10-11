"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if node == None:
            return None
        
        visited = {}
        def bfs(n):
            neighborhood = deque()
            visited[n] = Node(n.val, [])
            neighborhood.append(n)
            while neighborhood:
                currNode = neighborhood.popleft()
                for nei in currNode.neighbors:
                    if nei not in visited:
                        visited[nei] = Node(nei.val, [])
                        neighborhood.append(nei)
        bfs(node)
        for v in visited:
            for n in v.neighbors:
                visited[v].neighbors.append(visited[n])
        return visited[node]
                        