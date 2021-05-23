'''
Given an integer n, return the number of structurally unique BST's (binary search trees) which has exactly n nodes of unique values from 1 to n.

Example 1:
Input: n = 3
Output: 5

Example 2:
Input: n = 1
Output: 1

'''

'''
n = 0 => 1種(空樹)
n = 1 => 1種
n = 2 => 2種
n = 3 => root:1, left: 0  right:2   f(0) * f(2)
         root:2, left: 1  right:1   f(1) * f(1)
         root:3, left: 2  right:0   f(2) * f(0)
'''
def numTrees(n):
    dp = [0] * (n+1)
    dp[0] = 1
    for i in range(1,n+1):
        for j in range(i):
            dp[i] += dp[j] * dp[i-j-1]
    return dp[n]
print(numTrees(3))