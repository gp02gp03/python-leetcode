'''
Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right, which minimizes the sum of all numbers along its path.

Note: You can only move either down or right at any point in time.


Example 1:
Input: grid = [[1,3,1],[1,5,1],[4,2,1]]
Output: 7

Explanation: Because the path 1 → 3 → 1 → 1 → 1 minimizes the sum.

Example 2:
Input: grid = [[1,2,3],[4,5,6]]
Output: 12
'''

def minPathSum(grid):
    m = len(grid)
    n = len(grid[0])
    for i in range(m):
        for j in range(n):
            if i == 0 and j != 0:
                grid[i][j] = grid[i][j-1] + grid[i][j]
            elif i != 0 and j == 0:
                grid[i][j] = grid[i-1][j] + grid[i][j]
            elif i != 0 and j != 0:
                grid[i][j] = min(grid[i-1][j],grid[i][j-1]) + grid[i][j]
    return grid[m-1][n-1]

print(minPathSum([[1,2,3],[4,5,6]]))