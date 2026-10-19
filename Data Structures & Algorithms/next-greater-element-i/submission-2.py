class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = []
        waiting = []
        answerDict = {}
        for i in range(len(nums2)):
            if not waiting: 
                waiting.append(nums2[i])
            elif waiting[-1] > nums2[i]:
                waiting.append(nums2[i])
            else:
                pair = waiting.pop()
                answerDict[pair] = nums2[i]
                waiting.append(nums2[i])
        for num in nums1:
            if num in answerDict:
                res.append(answerDict[num])
            else:
                res.append(-1)
        return res

        