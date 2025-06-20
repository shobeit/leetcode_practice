#Find the smallest missing positive integer from an unsorted list.
#Constraints: Must run in O(n) time and use constant space.

def small_missing_pos(nums):
    n = len(nums)

    for i in range(n):
        while (1 <= nums[i] <= n) and nums[nums[i] - 1] != nums[i]:
            nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] -1]

    for i in range(n):
        if nums[i] != i + 1:
            return i + 1
    return n + 1


if __name__ == "__main__":
    # Example input list
    test_input = [3, 4, -1, 1]
    result = small_missing_pos(test_input)
    print("Smallest missing positive integer:", result)
