'''
input : 
[1,3,2,5]
[2,1,3,null,4,null,7]

output:
[3,4,5,5,4,null,7]

    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        if not t1 and not t2: 
            return None
        if not t1 or not t2:
            return t1 or t2
        t1.val += t2.val
        t1.left = self.mergeTrees(t1.left,t2.left)
        t1.right = self.mergeTrees(t1.right,t2.right)
        return t1


'''