class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        buckets = [[] for _ in range(len(nums) + 1)]
        numF = {}
        kFinal = []
        for i in range(len(nums)):
            numF[nums[i]] = 1 + numF.get(nums[i], 0)
        for num in numF:
            buckets[numF[num]].append(num)
        while len(kFinal) < k:
            for i in range(len(buckets) - 1, -1, -1):
                if len(buckets[i]) != 0:
                    for j in range(len(buckets[i])):
                        if len(kFinal) >= k:
                            break
                        kFinal.append(buckets[i][j])
        return kFinal
