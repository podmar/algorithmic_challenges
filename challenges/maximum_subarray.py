# LEETCODE
# Given an integer array nums, find the
# subarray
# which has the largest sum and return its sum.


# Example 1:

# Input: nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
# Output: 6
# Explanation: [4, -1, 2, 1] has the largest sum = 6.
# Example 2:

# Input: nums = [1]
# Output: 1
# Example 3:

# Input: nums = [5, 4, -1, 7, 8]
# Output: 23


# Constraints:

# 1 <= nums.length <= 105
# -104 <= nums[i] <= 104


# Follow up: If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.

def solution(nums):
    max_subarray, left_border, current_value = nums[0]

    for i in range(1, len(nums)):
        max_subarray = max(current_value + nums[i], max_subarray)

    return


def max_sum(nums):
    n = len(nums) - 1

    if n == 0:
        return nums[n]
    else:
        return max(max_sum(nums[:n-1]), max_sum(nums[:n-1]) + nums[n])


print(max_sum([1, 2, 3, 4]))
