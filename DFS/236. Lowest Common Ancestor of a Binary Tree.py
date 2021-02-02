'''
class Solution:
    def dfs(self,n,p,q):
        if not n:
            return False
        l = 1 if self.dfs(n.left,p,q) else 0
        r = 1 if self.dfs(n.right,p,q) else 0
        mid = 1 if n == p or n == q else 0
        if l + r + mid == 2: 
            self.ans = n
        return l + r + mid > 0
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.dfs(root,p,q)
        return self.ans
            
'''