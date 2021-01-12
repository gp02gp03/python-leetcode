'''
Given an array nums of n integers where n > 1,  return an array output such that output[i] is equal to the product of all the elements of nums except nums[i].

Example:

Input:  [1,2,3,4]
Output: [24,12,8,6]
Constraint: It's guaranteed that the product of the elements of any prefix or suffix of the array (including the whole array) fits in a 32 bit integer.

Note: Please solve it without division and in O(n).

Follow up:
Could you solve it with constant space complexity? (The output array does not count as extra space for the purpose of space complexity analysis.)


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [1] * n
        for i in range(1,n):
            res[i] = res[i-1] * nums[i-1]
        r = 1
        for i in range(n-1,-1,-1):
            res[i]*=r
            r*=nums[i]
        return res

nums  2       3       4       5
res   3*4*5   2*4*5   2*3*5   2*3*4
l             2       2*3     2*3*4     
r     3*4*5   4*5     5

'''