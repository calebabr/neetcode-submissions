class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # numCom = 0
        numCom = 0
        # Build adjacency list
        canTravel = defaultdict(list)
        for node1, node2 in edges:
            canTravel[node1].append(node2)
            canTravel[node2].append(node1)
        for i in range(n):
            if i not in canTravel:
                canTravel[i] = []
        # build and define bfs()
        visited = set()
        def bfs(i):
            neighborhood = deque()
            visited.add(i)
            neighborhood.append(i)
            while neighborhood:
                curr = neighborhood.popleft()
                for neighbor in canTravel[curr]:
                    if neighbor not in visited:
                        neighborhood.append(neighbor)
                        visited.add(neighbor)
        # Then loop over adjacency list, visiting all possible nodes. When we get to a new node, if this new node hasnt been visited yet then we can say we are at a new component, thus increment numCom += 1
        for i in range(n):
            if i not in visited:
                bfs(i)
                numCom += 1
        # return numCom
        return numCom