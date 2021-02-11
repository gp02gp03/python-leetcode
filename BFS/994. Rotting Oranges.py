'''
ou are given an m x n grid where each cell can have one of three values:

0 representing an empty cell,
1 representing a fresh orange, or
2 representing a rotten orange.
Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten.

Return the minimum number of minutes that must elapse until no cell has a fresh orange. If this is impossible, return -1.


Input: grid = [[2,1,1],[1,1,0],[0,1,1]]
Output: 4

Input: grid = [[2,1,1],[0,1,1],[1,0,1]]
Output: -1

'''
'''
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        res,fresh = 0,0
        q = set()
        m,n = len(grid),len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    fresh += 1
                elif grid[i][j] == 2:
                    q.add((i,j))
        dirrec = [(0,1),(0,-1),(1,0),(-1,0)]
        while q:
            tmp = set()
            for curx,cury in q:
                for dirx,diry in dirrec:
                    tx,ty = curx + dirx,cury + diry
                    if 0 <= tx < m and 0 <= ty < n and grid[tx][ty] == 1:
                        tmp.add((tx,ty))
                        grid[tx][ty] = 2
            q = tmp
            if q:
                res += 1
                fresh -= len(q)
        return res if fresh == 0 else -1
'''