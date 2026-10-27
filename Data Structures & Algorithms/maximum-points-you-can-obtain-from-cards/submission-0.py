class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        l, r = 0, len(cardPoints) - 1
        score = 0
        taken = 0
        if len(cardPoints) == k:
            return sum(cardPoints)
        
        while l < r and taken < k:
            if cardPoints[l] > cardPoints[r]:
                score += cardPoints[l]
                l += 1
                taken += 1
            elif cardPoints[l] < cardPoints[r]:
                score += cardPoints[r]
                r -= 1
                taken += 1
            else: # equal case
                if cardPoints[l+1] > cardPoints[r-1]:
                    score += cardPoints[l]
                    l += 1
                else:
                    score += cardPoints[r]
                    r -= 1
                taken += 1
        return score
