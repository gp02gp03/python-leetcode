'''
Input: root = [5,4,5,1,1,5]
Output: 2
'''
'''
class Solution:
    def longestUnivaluePath(self, root: TreeNode) -> int:
        if not root: return 0
        self.res = 0
        self.getPath(root)
        return self.res
    
    def getPath(self, root):
        if not root: return 0
        left = self.getPath(root.left)
        right = self.getPath(root.right)
        pl, pr = 0, 0
        if root.left and root.left.val == root.val: pl = 1 + left
        if root.right and root.right.val == root.val: pr = 1 + right
        self.res = max(self.res, pl + pr)
        return max(pl, pr)
                
'''