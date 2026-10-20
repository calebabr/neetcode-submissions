class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        numCom = 0
        # Create adjacency list
        adjList = defaultdict(list)
        for nodeA, nodeB in edges:
            adjList[nodeA].append(nodeB)
            adjList[nodeB].append(nodeA)
        
        visited = set()
        # define bfs(node)
        def bfs(node):
            neighborhood = deque()
            neighborhood.append(node)
            visited.add(node)
            while neighborhood:
                curr = neighborhood.popleft()
                for neighbor in adjList[curr]:
                    if neighbor not in visited:
                        neighborhood.append(neighbor)
                        visited.add(neighbor)
        
        # iterate 0 to n, if i is not in visited yet, its a new component so run bfs there at that node and increment numCom
        for i in range(n):
            if i not in visited:
                bfs(i)
                numCom += 1
        # return numCom
        return numCom