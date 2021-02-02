'''
Example 1:
Input: root = [1,2,5,3,4,null,6]
Output: [1,null,2,null,3,null,4,null,5,null,6]

Example 2:
Input: root = []
Output: []

Example 3:
Input: root = [0]
Output: [0]
'''
'''
class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return None
        l,r = root.left,root.right
        self.flatten(root.left)
        self.flatten(root.right)
        root.left,root.right = None,l
        while root.right:
            root = root.right
        
        root.right = r
'''