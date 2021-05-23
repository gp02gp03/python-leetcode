'''
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected and it will automatically contact the police if two adjacent houses were broken into on the same night.
Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.


Example 1:
Input: nums = [1,2,3,1]
Output: 4

Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
Total amount you can rob = 1 + 3 = 4.

Example 2:
Input: nums = [2,7,9,3,1]
Output: 12

Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
Total amount you can rob = 2 + 9 + 1 = 12.
'''

'''
1. 定義dp陣列的含義(找最大值)
2. 建立轉移方程 => dp[i] = max(dp[i-2] + nums[i], dp[i-1]), 分兩種情況: 偷與不偷
3. 初始化初始值 => dp[0] = nums[0], dp[1] = max(nums[0],nums[1])
'''

def rob(nums):
    l = len(nums)
    if l == 0:
        return 0
    if l == 1:
        return nums[0]
    rob = [0] * l
    rob[0],rob[1] = nums[0],max(nums[0],nums[1])
    for i in range(2,l):
        rob[i] = max(nums[i] + rob[i-2], rob[i-1])
    return rob[l-1]

print(rob([1,2,3,1]))