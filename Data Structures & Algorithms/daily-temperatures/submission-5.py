class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        answer = [0] * len(temperatures)
        waiting = []
        for i in range(len(temperatures)):
            while waiting and temperatures[waiting[-1]] < temperatures[i]:
                top = waiting.pop()
                answer[top] = i - top
            waiting.append(i)
        return answer