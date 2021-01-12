def merge(nums1,nums2):
    n1,n2,tmp,tmpList,res = len(nums1),len(nums2),0,[],[]
    for i in range(n1):
        tmpList.append(nums1[i])
    for i in range(n2):
        tmpList.append(nums2[i])
    tmpList = sorted(tmpList)
    for i in range(len(tmpList)):
        if tmpList[i] != 0:
            res.append(tmpList[i])
    if n1 > n2:
        del nums1[:]
        nums1 = res
    else:
        del nums2[:]
        nums2 = res
    return res


print(merge([1,2,3,0,0,0],[2,5,6]))

'''
Input:
nums1 = [1,2,3,0,0,0], m = 3
nums2 = [2,5,6],       n = 3

Output: [1,2,2,3,5,6]
'''