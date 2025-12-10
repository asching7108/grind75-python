class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        # Bottom-up DP
        # total = sum(nums)

        # # Total must be even
        # if total % 2 != 0:
        #     return False

        # # We need to find a subset that sums up to target
        # target = total // 2

        # dp = [False] * (target + 1)
        # dp[0] = True

        # for num in nums:
        #     for i in range(target, num - 1, -1):
        #         if dp[i - num]:
        #             dp[i] = True

        # return dp[target]

        # Time complexity: O(m * n) where m is the target and n is the length of nums
        # Space complexity: O(m)

        # Top-down DP
        total = sum(nums)

        # Total must be even
        if total % 2 != 0:
            return False

        # We need to find a subset that sums up to target
        target = total // 2

        @lru_cache(maxsize=None)
        def dfs(i: int, curr: int) -> bool:
            if curr == target:
                return True
            
            if curr > target or i == len(nums):
                return False

            # nums[i] is either included or not included in the subset
            return dfs(i + 1, curr + nums[i]) or dfs(i + 1, curr)

        return dfs(0, 0)

        # Time complexity: O(m * n) where m is the target and n is the length of nums
        # Space complexity: O(m * n), O(m * n) for memoization and O(n) for recursive call stack