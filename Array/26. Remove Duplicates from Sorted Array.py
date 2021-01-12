def removeDuplicates(nums):
    dic,count,nums_Len = {},1,len(nums)
    for i in range(nums_Len):
        key = str(nums[i])
        if key in dic:
            dic[key] = dic.get(key) + 1
        else:
          dic[key] = count
    for i in range(nums_Len):
        key = nums[i]
        if key in dic.keys():
            if dic.get(key) > 1:  
                dic[key] = dic.get(key) -1
    del nums[:]
    for i in dic.keys():
        nums.append(i)
    return len(nums)

print(removeDuplicates([1,1,2]))
print(removeDuplicates([0,0,1,1,1,2,2,3,3,4]))


'''
Input: nums = [0,0,1,1,1,2,2,3,3,4]
Output: 5, nums = [0,1,2,3,4]

Input: nums = [1,1,2]
Output: 2, nums = [1,2]
'''