'''
For example, this binary tree [1,2,2,3,4,4,3] is symmetric: True

    def isSymmetric(self, root: TreeNode):
        if not root:
            return True
        return self.isSym(root.left,root.right)
    
    def isSym(self, l: TreeNode, r: TreeNode) -> bool:
        if not l and not r: return True
        if not l or not r: return False
        if l.val != r.val: return False
        return self.isSym(l.left,r.right) and self.isSym(l.right,r.left)
        
'''