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
                curr = neighborhood.pop()
                for neighbor in curr.neighbors:
                    if neighbor not in visited:
                        visited[neighbor] = Node(neighbor.val, [])
                        neighborhood.append(neighbor) 
        
        bfs(node)
        for n in visited:
            for neighbor in n.neighbors:
                visited[n].neighbors.append(visited[neighbor])
        
        return visited[node]
        
                        