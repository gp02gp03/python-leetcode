'''
Example 1:

Input: nums = [1,2,2,4]
Output: [2,3]
Example 2:

Input: nums = [1,1]
Output: [1,2]
'''


def findErrorNums(nums):
    sum_uniqe = sum(set(nums))
    dup = sum(nums) - sum_uniqe
    miss = (len(nums) + 1) * len(nums) // 2 - sum_uniqe
    return [dup, miss]


print(findErrorNums([1, 2, 2, 4]))
