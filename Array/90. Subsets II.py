'''
Example 1:

Input: nums = [1,2,2]
Output: [[],[1],[1,2],[1,2,2],[2],[2,2]]


Example 2:
Input: nums = [0]
Output: [[],[0]]
'''


def subsetsWithDup(nums):
    nums.sort()
    res = [[], [nums[0]]]
    tmp = [[nums[0]]]
    for i in range(1, len(nums)):
        if nums[i] == nums[i - 1]:
            tmp = [t + [nums[i]] for t in tmp]
        else:
            tmp = [t + [nums[i]] for t in res]
        res += tmp
    return res

print(subsetsWithDup([1, 2, 2]))
