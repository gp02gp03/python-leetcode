'''
Example 1:

Input: [3,2,1,5,6,4] and k = 2
Output: 5
Example 2:

Input: [3,2,3,1,2,4,5,5,6] and k = 4
Output: 4
Note:
You may assume k is always valid, 1 ≤ k ≤ array's length.
'''
'''
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        import random
        k = len(nums) - k
        def select(nums,k):
            pivot = int( random.randint(0,len(nums) -1))
            l,r = [],[]
            for i,n in enumerate(nums):
                if n <= nums[pivot] and i != pivot:
                    l.append(n)
                if n > nums[pivot]:
                    r.append(n)
            if k == len(l): 
                return nums[pivot]
            elif k < len(l):
                return select(l,k)
            else:
                return select(r,k-len(l) -1)
        return select(nums,k)
'''