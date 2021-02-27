'''
Example 1:

Input: nums = [2,6,4,8,10,9,15]
Output: 5
Explanation: You need to sort [6, 4, 8, 10, 9] in ascending order to make the whole array sorted in ascending order.
Example 2:

Input: nums = [1,2,3,4]
Output: 0
Example 3:

Input: nums = [1]
Output: 0
 

Constraints:

1 <= nums.length <= 104
-105 <= nums[i] <= 105
'''


def findUnsortedSubarray(nums):
    s_nums = sorted(nums)
    if len(nums) == 1 or (s_nums == nums):
        return 0
    count = start = end = 0
    for i in range(len(nums)):
        if nums[i] != s_nums[i]:
            count += 1
            end = i
            if count == 1:
                start = i
        #print(start,end)
    return end - start + 1


print(findUnsortedSubarray([2, 6, 4, 8, 10, 9, 15]))
