# Approach 1

nums = [-1]
n = len(nums)


for i in range(1, n):
    nums[i] += nums[i-1]

min_sum = 0
max_sum = float('-inf')

for i in nums:
    cur_sum = i - min_sum
    max_sum = max(cur_sum, max_sum)
    min_sum = min(i, min_sum)

print(max_sum)


# Approach 2

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        min_sum = nums[0]
        max_sum = min_sum

        for i in range(1, len(nums)):

            tmp_sum = min_sum + nums[i]

            if tmp_sum > nums[i]:
                min_sum = tmp_sum
            else:
                min_sum = nums[i]

            if min_sum > max_sum:
                max_sum = min_sum

        return max_sum