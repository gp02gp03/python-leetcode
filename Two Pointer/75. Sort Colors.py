"""
Example 1:

Input: nums = [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]
Example 2:

Input: nums = [2,0,1]
Output: [0,1,2]
Example 3:

Input: nums = [0]
Output: [0]
Example 4:

Input: nums = [1]
Output: [1]

"""


def sortColors(nums):
    left = 0
    right = len(nums) - 1
    i = 0
    while i <= right:
        if nums[i] == 0:
            nums[left], nums[i] = nums[i], nums[left]
            left = left + 1
            i = i + 1
        elif nums[i] == 1:
            i = i + 1
        elif nums[i] == 2:
            nums[i], nums[right] = nums[right], nums[i]
            right = right - 1
    return nums


print(sortColors([2, 0, 2, 1, 1, 0]))
