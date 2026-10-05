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
        # O(V) pass, mapping original to clone in visited {}
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
        # O(V + E) pass looping over visited this time adding neighbors of original to clone
        bfs(node)
        for n in visited:
            for x in n.neighbors:
                visited[n].neighbors.append(visited[x])

        return visited[node]
        # for n in visited:
           #  res.append(n.)
