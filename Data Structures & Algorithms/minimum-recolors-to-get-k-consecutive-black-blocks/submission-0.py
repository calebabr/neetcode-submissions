class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        # freqDict = {}
        l = 0
        blackC = 0
        best = 0
        # build window size k
        for r in range(k):
            if blocks[r] == 'B':
                blackC += 1
        r = k-1
        best = k - blackC
        while r < (len(blocks)):
            if blocks[l] == 'B':
                blackC -= 1
            l += 1
            r += 1
            if r < len(blocks) and blocks[r] == 'B':
                blackC += 1
            best = min(best, k - blackC)
        return best
            

        