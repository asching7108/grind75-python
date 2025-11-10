# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        lo, hi = 1, n

        while lo < hi:
            mid = (lo + hi) // 2
            isBad = isBadVersion(mid)
            if isBad:
                hi = mid
            else:
                lo = mid + 1

        return lo

# Time complexity: O(log n)
# Space complexity: O(1)