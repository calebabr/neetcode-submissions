class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        minHeap = []
        heapq.heapify(minHeap)
        for num in nums:
            if len(minHeap) >= k:
                heapq.heappop(minHeap)
            heapq.heappush(minHeap, (-1) * num)
        top = heapq.heappop(minHeap) * (-1)
        return top
