class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        majority = len(nums) // 2
        counter = {}

        for i in nums:
            counter[i] = counter.get(i, 0) + 1
            if counter[i] > majority:
                return i

        # counts = collections.Counter(nums)
        # return max(counts.keys(), key=counts.get)

# Time complexity: O(n)
# Space complexity: O(n)