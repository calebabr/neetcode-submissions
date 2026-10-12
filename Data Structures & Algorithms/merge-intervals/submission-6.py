class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals, key=lambda i:i[0])
        merged = []

        for interval in intervals:
            if merged and merged[-1][1] > interval[0] and merged[-1][1] > interval[1]: # contained
                continue
            # merged
            elif merged and merged[-1][1] > interval[0] and merged[-1][1] <= interval[1]:
                start, end = merged.pop()
                end = interval[1]
            # touching ends
            elif merged and merged[-1][1] == interval[0]:
                start, end = merged.pop()
                end = interval[1]
            else: # new interval
                start = interval[0]
                end = interval[1]
            merged.append([start, end])
        return merged
            
            