class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        maxHeap = []
        heapq.heapify(maxHeap)
        for num in nums:
            while len(maxHeap) > k:
                heapq.heappop(maxHeap)
            heapq.heappush(maxHeap, (-1) * num)
        top = heapq.heappop(maxHeap) * (-1)
        return top
