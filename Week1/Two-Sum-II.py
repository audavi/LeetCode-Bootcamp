class Solution(object):
    def twoSum(self, numbers, target):
        solution = []
        start = 0
        end = len(numbers) - 1
        while start <= end:
            if numbers[start] + numbers[end] == target:
                solution.append(start + 1)
                solution.append(end + 1)
                return solution
            elif numbers[start] + numbers[end] < target:
                start += 1
            else:
                end -= 1