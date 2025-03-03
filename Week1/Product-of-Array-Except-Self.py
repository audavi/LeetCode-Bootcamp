class Solution(object):
    def productExceptSelf(self, nums):
        solution = [1] * len(nums)
        products_before = [1] * len(nums)
        products_after = [1] * len(nums)

        for i in range(1, len(nums)):
            products_before[i] = products_before[i - 1] * nums[i - 1]

        for i in range(len(nums) - 2, -1, -1):
            products_after[i] = products_after[i + 1] * nums[i + 1]

        for i in range(len(nums)):
            solution[i] = products_before[i] * products_after[i]

        return solution