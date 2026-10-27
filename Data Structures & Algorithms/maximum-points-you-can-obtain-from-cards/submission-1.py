class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        n = len(cardPoints)
        totalSum = sum(cardPoints)
        currSum = 0
        maxSum = 0
        if n == k:
            return sum(cardPoints)

        # Build first window
        for r in range(n-k): # iterates from 0 to n - k - 1 for a window if n - k leaving k elements => n total elements
            currSum += cardPoints[r]
        
        maxSum = totalSum - currSum
        r = n-k-1
        l = 0
        # Slide window across
        while r < n - 1:
            currSum -= cardPoints[l]
            l += 1
            r += 1
            currSum += cardPoints[r]

            maxSum = max(maxSum, totalSum - currSum)
        return maxSum
