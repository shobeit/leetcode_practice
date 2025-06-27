# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] where nums[i] + nums[j] + nums[k] == 0, and the indices i, j and k are all distinct.

# The output should not contain any duplicate triplets. You may return the output and the triplets in any order.

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for i, a in enumerate(nums):
            if i > 0 and a == nums[i - 1]:
                continue

            j = i + 1
            k = len(nums) - 1

            while j < k:
                threeSum = a + nums[j] + nums[k]
                if threeSum > 0:
                    k -= 1
                elif threeSum < 0:
                    j += 1
                else:
                    res.append([a, nums[j], nums[k]])
                    j += 1
                    while nums[j] == nums[j - 1] and j < k:
                        j += 1
        return res