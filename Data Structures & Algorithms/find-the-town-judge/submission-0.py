class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        trusts = defaultdict(set)
        trustedBy = defaultdict(set)

        for pair in trust:
            print(pair)
            trusts[pair[0]].add(pair[1])
            trustedBy[pair[1]].add(pair[0])
        # print(trusts)
        # print(trustedBy)
        for i in range(1, n+1):
            if len(trusts[i]) == 0 and len(trustedBy[i]) == n - 1:
                return i
        return -1