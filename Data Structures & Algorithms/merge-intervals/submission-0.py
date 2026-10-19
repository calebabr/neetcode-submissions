class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals, key=lambda i:i[0])
        merged = []

        for interv in intervals:
            if merged and merged[-1][1] > interv[0] and merged[-1][1] > interv[1]:
                continue
            elif merged and merged[-1][1] > interv[0] and merged[-1][1] <= interv[1]:
                merge = merged.pop()
                start = merge[0]
                end = interv[1]
            elif merged and merged[-1][1] == interv[0]:
                start = merge[0]
                end = interv[1]
            else:
                start = interv[0]
                end = interv[1]
            merged.append([start, end])
        return merged