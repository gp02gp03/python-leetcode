class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        if not root:
            return []
        res = []
        self.findPaths(root,str(root.val),res)
        return res
    
    def findPaths(self,root,s,res):
        if root.left == None and root.right == None:
            res.append('' + s)
        if root.left != None:
            self.findPaths(root.left, s + "->" + str(root.left.val) , res)
        if root.right != None:
            self.findPaths(root.right, s + "->" + str(root.right.val) , res)   
            return res

            