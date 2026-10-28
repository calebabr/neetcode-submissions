class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals, key=lambda i:i[0])
        merged = []
        for interval in intervals:
            # Contained
            if merged and merged[-1][1] > interval[0] and merged[-1][1] > interval[1]:
                continue
            # Overlapping
            elif merged and merged[-1][1] > interval[0] and merged[-1][0] <= interval[1]:
                start, end = merged.pop()
                end = interval[1]
            # Touching
            elif merged and merged[-1][1] == interval[0]:
                start,end = merged.pop()
                end = interval[1]
            # Neither
            else:
                start, end = interval[0], interval[1]
            merged.append([start, end])
        return merged
