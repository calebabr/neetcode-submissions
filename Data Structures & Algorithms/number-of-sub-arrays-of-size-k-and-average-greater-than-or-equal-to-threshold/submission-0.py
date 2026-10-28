class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        res = 0
        currSum = 0
        # Build first window
        for r in range(k):
            currSum += arr[r]
        if (currSum // k) >= threshold:
            res += 1

        l, r = 0, k-1
        while r < len(arr) - 1:
            currSum -= arr[l]
            l += 1
            r += 1
            currSum += arr[r]
            if (currSum // k) >= threshold:
                res += 1
        
        return res
        