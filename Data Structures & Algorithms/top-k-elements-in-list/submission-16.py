class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        buckets = [[] for i in range(len(nums) + 1)]
        numFreq = {}
        for i in range(len(nums)):
            numFreq[nums[i]] = 1 + numFreq.get(nums[i], 0)
        for num in numFreq:
            buckets[numFreq[num]].append(num)
        ans = []
        for i in range(len(buckets) - 1, -1, -1):
            for num in buckets[i]:
                if len(ans) < k:
                    ans.append(num)
        return ans