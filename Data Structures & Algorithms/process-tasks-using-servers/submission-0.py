class Solution:
    def assignTasks(self, servers: List[int], tasks: List[int]) -> List[int]:
        free=[(weight,i) for i,weight in enumerate(servers)]
        heapq.heapify(free)
        busy=[]
        answer=[]
        time=0

        for j,duration in enumerate(tasks):
            time=max(time,j)
            if not free:
                time=max(time,busy[0][0])
            while busy and busy[0][0]<=time:
                _,weight,i=heapq.heappop(busy)
                heapq.heappush(free,(weight,i))
            weight,i=heapq.heappop(free)
            answer.append(i)
            heapq.heappush(busy,(time+duration,weight,i))
            
        return answer
