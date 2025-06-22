#Concatenation of Array
#You are given an integer array nums of length n. Create an array ans of length 2n where ans[i] == nums[i] and ans[i + n] == nums[i] for 0 <= i < n (0-indexed).
#Specifically, ans is the concatenation of two nums arrays.
#6/21/2025



class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:

        n = len(nums)
        ans = [0] * (2 * n)
        
        for i in range(n):
            ans[i] = nums[i]
            ans[i + n] = nums[i]

        return ans

sol = Solution()

print(sol.getConcatenation([1, 4, 1, 2]))
print(sol.getConcatenation([22,21,20,1]))