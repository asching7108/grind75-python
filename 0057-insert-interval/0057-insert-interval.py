class Solution:
    def hasOverlap(self, i1: List[int], i2: List[int]) -> bool:
        # the start of the later interval <= the end of the earlier interval
        return max(i1[0], i2[0]) <= min(i1[1], i2[1])

    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        [newStart, newEnd] = newInterval

        for i, interval in enumerate(intervals):
            if not self.hasOverlap(interval, newInterval):
                if newInterval[0] < interval[0]:
                    res.append(newInterval)
                    return res + intervals[i:]
                res.append(interval)
            else:
                newInterval = [
                    min(interval[0], newInterval[0]),
                    max(interval[1], newInterval[1])
                ]

        if newInterval:
            res.append(newInterval)

        return res

# Time complexity: O(n)
# Space complexity: O(n)