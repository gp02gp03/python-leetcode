def hasPathSum(self, root: TreeNode, sum: int) -> bool:
    def checkSum(root,s):
        if (root.left == None) and (root.right == None):
            res.append(s)
            s = s + root.val
            return s == sum
        if root.left != None and root.right == None:
            return checkSum(root.left, s + root.val)
        if root.left == None and root.right != None:
            return checkSum(root.right, s + root.val)
        return  checkSum(root.left, s + root.val) or checkSum(root.right, s + root.val)
        
        if root == None:
            return False
        res = []
        return checkSum(root,0)
        