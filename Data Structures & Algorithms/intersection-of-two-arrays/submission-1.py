class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        num1S = set()
        num2S = set()

        seen = set()
        for num in nums1:
            num1S.add(num)
        for num in nums2:
            num2S.add(num)
        res = []
        if len(nums1) > len(nums2):
            for i in range(len(nums1)):
                if nums1[i] in num1S and nums1[i] in num2S and nums1[i] not in seen:
                    res.append(nums1[i])
                    seen.add(nums1[i])

        else:
            for i in range(len(nums2)):
                if nums2[i] in num1S and nums2[i] in num2S and nums2[i] not in seen:
                    res.append(nums2[i])
                    seen.add(nums2[i])
        return res
