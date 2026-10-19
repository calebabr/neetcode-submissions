class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        buckets = [[] for i in range(len(nums) + 1)] # buckets where values in bucket[i] are values with frequency i
        numFreq = {}
        # Populate numFreq then use frequency to populate buckets
        for i in range(len(nums)):
            numFreq[nums[i]] = 1 + numFreq.get(nums[i], 0)
        for num in numFreq:
            buckets[numFreq[num]].append(num)
        # while length of answer is less than k, walk buckets backwards (to get most frequent). For nonempty buckets, append to anser while length of answer is less than or equal to k
        ans = []
        while len(ans) < k:
            for i in range(len(buckets) - 1, -1, -1):
                if len(buckets[i]) != 0:
                    for j in range(len(buckets[i])):
                        if len(ans) < k:
                            ans.append(buckets[i][j])
        return ans