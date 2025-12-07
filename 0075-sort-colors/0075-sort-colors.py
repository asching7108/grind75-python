class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # Use p1 for the right boundary of 0s and p2 for left boundary of 2s
        curr, p1, p2 = 0, 0, len(nums) - 1

        while curr <= p2:
            if nums[curr] == 0:
                # swap curr and p1 values
                nums[curr] = 1  # nums[p1] will always be 1
                nums[p1] = 0
                p1 += 1
                curr += 1
            elif nums[curr] == 1:
                curr += 1
            else:
                # swap curr and p2 values
                nums[curr] = nums[p2]
                nums[p2] = 2
                p2 -= 1

# Time complexity: O(n)
# Space complexity: O(1)