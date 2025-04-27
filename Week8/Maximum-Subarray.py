class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_sum_until_i = max_sum = nums[0]
        for i, num in enumerate(nums[1:], start=1):
            max_sum_until_i = max(max_sum_until_i + num, num)
            max_sum = max(max_sum, max_sum_until_i, max_sum)
        return max_sum
