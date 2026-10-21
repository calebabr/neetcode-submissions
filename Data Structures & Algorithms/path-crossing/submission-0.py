class Solution:
    def isPathCrossing(self, path: str) -> bool:
        walked = set()
        walked.add((0, 0))
        curr = [0, 0]
        directions = {'N': (0, 1), 'E': (1, 0), 'W': (-1, 0), 'S':(0, -1)}
        for char in path:
            curr = [curr[0] + directions[char][0], curr[1] + directions[char][1]]
            if tuple(curr) in walked:
                return True
            walked.add(tuple(curr))
        
        return False