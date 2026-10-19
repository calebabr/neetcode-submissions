class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numF = {}
        kFinal = []
        for i in range(len(nums)):
            numF[nums[i]] = 1 + numF.get(nums[i], 0)
        buckets = [[] for _ in range(len(nums) + 1)]
        for num, count in numF.items():
            buckets[count].append(num)
        for i in range(len(buckets)-1, -1, -1):
            if len(buckets[i]) == 0:
                continue
            while len(kFinal) < k:
                kFinal.append(item for item in buckets[i])
            if (len(kFinal) == k):
                break
        return kFinal