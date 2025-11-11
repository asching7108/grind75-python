class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        uniqueNums = set()
        for i in nums:
            if i in uniqueNums:
                return True
            uniqueNums.add(i)
        return False

# Time complexity: O(n)
# Space complexity: O(n)