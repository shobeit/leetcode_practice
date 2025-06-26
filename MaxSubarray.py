# Given an array of integers nums, find the subarray with the largest sum and return the sum.
# 06/24/2025
# 06/25/2025

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        maxSub = nums[0]
        curSum = 0

        for n in nums:
            if curSum < 0:
                curSum = 0
            curSum += n
            maxSub = max(maxSub, curSum)
        return maxSub