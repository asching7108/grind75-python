class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)

        if total % 2 != 0:
            return False

        target = total // 2

        dp = [False] * (target + 1)
        dp[0] = True

        for num in nums:
            for i in range(target, num - 1, -1):
                if dp[i - num]:
                    dp[i] = True

        return dp[target]

        # Time complexity: O(m * n) where m is the target and n is the length of nums
        # Space complexity: O(m)