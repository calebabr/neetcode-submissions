class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # Trees are graphs with n vertices that are connected, acyclic and n - 1 edges.
        numEdges = 0
        visited = set()
        adjList = defaultdict(list)

        # Make adjacency list
        for e in edges:
            adjList[e[0]].append(e[1])
        
        # Iterate through adjacency list.
        for sNode in adjList:
            if sNode not in visited:
                visited.add(sNode)
            for nei in adjList[sNode]:
                if nei not in visited:
                    visited.add(nei)
                    numEdges += 1
        # If dest. node hasnt been visited, visit it. 

        return numEdges == n - 1