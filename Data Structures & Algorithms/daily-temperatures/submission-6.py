class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        waiting = []
        for i in range(len(temperatures)):
            while waiting and temperatures[waiting[-1]] <= temperatures[i]:
                top = waiting.pop()
                result[top] = i - top
            waiting.append(i)
        return result