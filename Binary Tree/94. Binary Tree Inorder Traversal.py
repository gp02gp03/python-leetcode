'''
Input: root = [1,null,2,3]
Output: [1,3,2]
Example 2:

Input: root = []
Output: []
Example 3:

Input: root = [1]
Output: [1]

'''
'''
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        self.res = []
        def dfs(root):
            if not root: 
                return
            if root.left:
                dfs(root.left)
            self.res.append(root.val)
            if root.right:
                dfs(root.right)
        dfs(root)
        return self.res

'''