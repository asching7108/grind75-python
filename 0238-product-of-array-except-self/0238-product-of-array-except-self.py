class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        answer = [0] * length
        answer[0] = 1

        for i in range(1, length):
            # store the product of all elements to the left of i in answer[i]
            answer[i] = nums[i - 1] * answer[i - 1]

        R = 1
        for i in reversed(range(length)):
            answer[i] = answer[i] * R
            R *= nums[i]

        return answer

# Time complexity: O(n)
# Space complexity: O(1) except for the answer array