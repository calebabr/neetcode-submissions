class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        dictFreq = {}
        for num in nums:
            if num not in dictFreq:
                dictFreq[num] = 0
            else:
                dictFreq[num] += 1
        print(dictFreq)
        print(len(nums) // 2)
        for num in dictFreq:
            if dictFreq[num] >= (len(nums) // 2):
                return num
        return -1
        # print(dictFreq)
        