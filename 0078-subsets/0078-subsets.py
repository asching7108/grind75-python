class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        def backtrack(i, path) -> None:
            if i == len(nums):
                res.append(path[:])
                return

            backtrack(i + 1, path)
            path.append(nums[i])
            backtrack(i + 1, path)
            path.pop()

        backtrack(0, [])
        return res