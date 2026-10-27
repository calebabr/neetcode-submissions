class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        # Create adjacency list of key digit to value [neighAbove, neighBelow]
        # Traverse each digit changing it to match target. Keep track of minimum changes to get to target digit. After solidyfing a digit, check if 

        if target == "0000":
            return 0

        visited = set(deadends)
        
        nextVisit = deque(["0000"])
        totalChange = 0

        if "0000" in visited:
            return -1
        visited.add("0000")
        while nextVisit:
            totalChange += 1
            for _ in range(len(nextVisit)):
                currLock = nextVisit.popleft()
                for i in range(4):
                    for j in [1, -1]:
                        digit = str((int(currLock[i]) + j + 10) % 10)
                        nextLock = currLock[:i] + digit + currLock[i+1:]
                        if nextLock in visited:
                            continue
                        
                        if nextLock == target:
                            return totalChange
                        nextVisit.append(nextLock)
                        visited.add(nextLock)
        
        return -1
