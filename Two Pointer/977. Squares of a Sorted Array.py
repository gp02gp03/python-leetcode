'''
977. Squares of a Sorted Array
Easy

1919

111

Add to List

Share
Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.

 

Example 1:

Input: nums = [-4,-1,0,3,10]
Output: [0,1,9,16,100]
Explanation: After squaring, the array becomes [16,1,0,9,100].
After sorting, it becomes [0,1,9,16,100].
Example 2:

Input: nums = [-7,-3,2,3,11]
Output: [4,9,9,49,121]
 

Constraints:

1 <= nums.length <= 104
-104 <= nums[i] <= 104
nums is sorted in non-decreasing order.
 
'''


def sortedSquares(nums):
    left, right, index = 0, len(nums) - 1, len(nums) - 1
    left_value, right_value = 0, 0
    res, temp = [0] * len(nums), 0
    while left <= right:
        left_value, right_value = pow((nums[left]), 2), pow((nums[right]), 2)
        if left_value <= right_value:
            temp = right_value
            right = right - 1
        else:
            temp = left_value
            left = left + 1
        print(index, temp)
        res[index] = temp
        index = index - 1

    return res


print(sortedSquares([-7, -3, 2, 3, 11]))
