class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        peopleHeap = []
        for i in range(len(names)):
            heapq.heappush(peopleHeap, ((-1) * heights[i], names[i]))
        
        res = []
        while peopleHeap:
            _, person = heapq.heappop(peopleHeap)
            res.append(person)
        
        return res