'''
Given a fixed-length integer array arr, duplicate each occurrence of zero, shifting the remaining elements to the right.

Note that elements beyond the length of the original array are not written. Do the above modifications to the input array in place and do not return anything.

Example 1:

Input: arr = [1,0,2,3,0,4,5,0]
Output: [1,0,0,2,3,0,0,4]
Explanation: After calling your function, the input array is modified to: [1,0,0,2,3,0,0,4]
Example 2:

Input: arr = [1,2,3]
Output: [1,2,3]
Explanation: After calling your function, the input array is modified to: [1,2,3]

'''

'''
class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        n,count,cur,f = len(arr),0,0,False
        for num in arr:
            count += 2 if num == 0 else 1
            if count >= n:
                f = count == n + 1
                break
            cur += 1
        right = n-1
        if f:
            arr[-1] = 0
            cur -= 1
            right -= 1
        while cur >= 0:
            arr[right] = arr[cur]
            if arr[cur] == 0:
                arr[right - 1] = 0
                right -= 1
            right -= 1
            cur -= 1

'''

