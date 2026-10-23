class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        maxEl = -1
        temp = 0
        for i in range(len(arr) - 1, -1, -1):
            temp = arr[i]
            arr[i] = maxEl
            if temp >= maxEl:
                maxEl = temp
        return arr