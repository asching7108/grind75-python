class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        lo, hi = 0, len(numbers) - 1

        while lo < hi:
            sum = numbers[lo] + numbers[hi]
            if sum == target:
                return [lo + 1, hi + 1]
            if sum < target:
                lo += 1
            else:
                hi -= 1

        return []

# Time complexity: O(n)
# Space complexity: O(1)