class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = nums[0]
        curr = nums[0]

        for num in nums[1:]:
            # Discard subarray if it's negative
            curr = max(num, curr + num)
            res = max(res, curr)

        return res

# Time complexity: O(n)
# Space complexity: O(1)