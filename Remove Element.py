# Remove Element
# Solved 
# You are given an integer array nums and an integer val. Your task is to remove all occurrences of val from nums in-place.

# After removing all occurrences of val, return the number of remaining elements, say k, such that the first k elements of nums do not contain val.

# Note:

# The order of the elements which are not equal to val does not matter.
# It is not necessary to consider elements beyond the first k positions of the array.
# To be accepted, the first k elements of nums must contain only elements not equal to val.
# Return k as the final result.

# 6/21/2025

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:

        n = len(nums)
        k = 0

        for i in range(n):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1

        return k