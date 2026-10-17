class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        answer = [0] * len(temperatures) # Days since => difference in index
        waiting = [] # indices waiting for warmer day
        for i in range(len(temperatures)):
            while waiting and temperatures[waiting[-1]] < temperatures[i]: # remove from waiting if they have found warmer
                top = waiting.pop()
                answer[top] = i - top
            waiting.append(i) # is now waiting
        return answer