class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        left, right = 0, 1
        res = nums[0]
        curr = nums[0]

        while right < len(nums):
            newVal = nums[right]
            if curr < 0:
                left = right
                curr = newVal
            else:
                curr += newVal
            res = max(res, curr)
            right += 1

        return res

# Time complexity: O(n)
# Space complexity: O(1)