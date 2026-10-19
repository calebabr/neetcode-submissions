class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        minHeap = []
        heapq.heapify(minHeap)
        for num in nums:
            while len(minHeap) > k:
                heapq.heappop(minHeap)
            heapq.heappush(minHeap, num)
        top = heapq.heappop(minHeap)
        return top
