class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res = []

        def backtrack(i, curr) -> None:
            res.append(curr[:]) # Copy current subset into result list

            for j in range(i, n):
                curr.append(nums[j])
                backtrack(j + 1, curr)
                curr.pop()  

        backtrack(0, [])
        return res

# Time complexity: O(n * 2^n). Since each element can be included or excluded,
# total subsets = 2^n. Copying a subset costs up to O(n).
# Space complexity: O(n) for recursion stack.