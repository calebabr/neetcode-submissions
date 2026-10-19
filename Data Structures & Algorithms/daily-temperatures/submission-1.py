class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        for i in range(len(temperatures) - 2, -1, -1):
            if temperatures[i] < temperatures[i + 1]:
                result[i] = 1 + result[i + 1]
        return result
