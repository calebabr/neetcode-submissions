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
        # O(V) pass over original graph to map original to clone(original.val, [])
        def bfs(n):
            neighborhood = deque()
            visited[n] = Node(n.val, [])
            neighborhood.append(n)
            while neighborhood:
                curr = neighborhood.popleft()
                for nei in curr.neighbors:
                    if nei not in visited:
                        visited[nei] = Node(nei.val, [])
                        neighborhood.append(nei)
        # Iterate through map adding neighbors of origina to clone

        bfs(node)
        for v in visited:
            for n in v.neighbors:
                visited[v].neighbors.append(visited[n])
        return visited[node]
