class Solution:
    def minAbsoluteDifference(self, nums: List[int], x: int) -> int:
        n = len(nums)
        ans = float('inf')

        for i in range(n - x):
            for j in range(i + x, n):
                if abs(nums[i] - nums[j]) < ans:
                    ans = abs(nums[i] - nums[j])

        return ans