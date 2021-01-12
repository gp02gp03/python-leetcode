def threeSum(nums):
    nums.sort()
    res = []
    for i in range(len(nums)-2):
        l,r,target = i +1,len(nums) -1,0 - nums[i]
        while l < r: 
            if (nums[l] + nums[r] == target):
                if [nums[i], nums[l], nums[r]] not in res:
                    res.append([nums[i], nums[l], nums[r]])
                if (nums[l] == nums[l + 1]):
                    l = l+1
                if (nums[r] == nums[r - 1]):
                    r = r-1
                l = l+1
                r = r-1
            elif nums[l] + nums[r] < target:
                l = l+1
            else:
                r = r-1            
    return res

print(threeSum([-1,0,1,2,-1,-4]))  #3Sum [[-1,-1,2],[-1,0,1]]
