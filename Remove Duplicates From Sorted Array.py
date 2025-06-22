# <!-- Remove Duplicates From Sorted Array
# You are given an integer array nums sorted in non-decreasing order. Your task is to remove duplicates from nums in-place so that each element appears only once.

# After removing the duplicates, return the number of unique elements, denoted as k, such that the first k elements of nums contain the unique elements.

# Note:

# The order of the unique elements should remain the same as in the original array.
# It is not necessary to consider elements beyond the first k positions of the array.
# To be accepted, the first k elements of nums must contain all the unique elements.
# Return k as the final result.

# 6/21/2025
from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        n = len(nums)
        k = 0

        for i in range(n):
            if k == 0 or nums[i] != nums[k-1]:
                nums[k] = nums[i]
                k += 1
        return k


sol = Solution()

nums1 = [1, 1, 2, 3, 4]
k1 = sol.removeDuplicates(nums1)
print(f"Original: [1, 1, 2, 3, 4], Unique count: {k1}, Modified array (first {k1} elements): {nums1[:k1]}")

nums2 = [2, 10, 10, 30, 30, 30]
k2 = sol.removeDuplicates(nums2)
print(f"Original: [2, 10, 10, 30, 30, 30], Unique count: {k2}, Modified array (first {k2} elements): {nums2[:k2]}")