class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        time = 0
        i = k
        while tickets[k] > 0:
            tickets[i] -= 1
            time += 1
            i += 1
            if i == len(tickets):
                i = 0
        return time