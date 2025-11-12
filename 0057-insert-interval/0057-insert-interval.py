class Solution:
    def hasOverlap(self, i1: List[int], i2: List[int]) -> bool:
        # the start of the later interval <= the end of the earlier interval
        return max(i1[0], i2[0]) <= min(i1[1], i2[1])

    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        [newStart, newEnd] = newInterval

        for i, [start, end] in enumerate(intervals):
            if end < newStart:
                res.append([start, end])
            elif start > newEnd:
                res.append([newStart, newEnd])
                return res + intervals[i:]
            else:
                [newStart, newEnd] = [
                    min(start, newStart),
                    max(end, newEnd)
                ]
            print([newStart, newEnd])

        if newStart or newEnd:
            res.append([newStart, newEnd])

        return res

# Time complexity: O(n)
# Space complexity: O(n)