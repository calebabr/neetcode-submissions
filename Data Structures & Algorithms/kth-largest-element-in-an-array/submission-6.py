class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        maxHeap = []
        heapq.heapify(maxHeap)
        for num in nums:
            while len(maxHeap) > k:
                heapq.heappop(maxHeap)
            heapq.heappush(maxHeap, (num))
        while len(maxHeap) > k:
            heapq.heappop(maxHeap)
        top = heapq.heappop(maxHeap)
        return top
