'''
Example 1:
Input: nums = [10, 5, 2, 6], k = 100
Output: 8
Explanation: The 8 subarrays that have product less than 100 are: [10], [5], [2], [6], [10, 5], [5, 2], [2, 6], [5, 2, 6].
Note that [10, 5, 2] is not included as the product of 100 is not strictly less than k.
Note:

0 < nums.length <= 50000.
0 < nums[i] < 1000.
0 <= k < 10^6.

'''


def numSubarrayProductLessThanK(nums, k):
    if len(nums) == 0: return 0
    left, right, product, res = 0, 0, 1, 0
    while right < len(nums):
        if product * nums[right] < k:
            product = product * nums[right]
            res = res + right - left + 1
            right = right + 1
        else:
            product /= nums[left]
            left = left + 1
            if left > right:
                right = right + 1
                product = 1
    return res


print(numSubarrayProductLessThanK([10, 5, 2, 6], 100))
