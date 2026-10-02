class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        trusts = defaultdict(list)
        trustedBy = defaultdict(list)

        for p in trust: # Make trusts and trustedBy
            trusts[p[0]].append(p[1])
            trustedBy[p[1]].append(p[0])
        
        for i in range(1, n+1): # judge trusts no one and everyone trusts them
            if len(trusts[i]) == 0 and len(trustedBy[i]) == n - 1:
                return i
        return -1