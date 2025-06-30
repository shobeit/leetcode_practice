Given an integer array nums, return true if any value appears more than once in the array, otherwise return false.

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        my_set = set()

        for n in nums:
            if n in my_set:
                return True
            my_set.add(n)
        return False