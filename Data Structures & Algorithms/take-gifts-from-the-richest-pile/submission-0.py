import math 

class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        gifts = [-x for x in gifts]
        print(gifts)
        heapq.heapify(gifts)
        for i in range(k):
            curr = -1 * heapq.heappop(gifts)
            curr = math.floor(math.sqrt(curr))
            heapq.heappush(gifts, -1 * curr)
        gifts = [-x for x in gifts]
        total = 0
        for pile in gifts:
            total += pile
        return total
