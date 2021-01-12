'''
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Output: Because nums[0] + nums[1] == 9, we return [0, 1].
'''




def twoSum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    numMap = {}
    for i in range(len(nums)):
        if target -nums[i] in numMap:
            return [numMap.get(target -nums[i]),i]
        else:
            numMap[nums[i]] = i
    return [-1,-1]

print(twoSum([2,7,11,15],9))