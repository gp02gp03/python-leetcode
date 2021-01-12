'''
Input: root = [3,9,20,null,null,15,7]
Output: true


Input: root = [1,2,2,3,3,null,null,4,4]
Output: false
Example 3:

Input: root = []
Output: true

'''
'''
    def isBalanced(self, root: TreeNode) -> bool:
        def check(root:TreeNode) -> int:
            if root == None:
                return 0
            l = check(root.left)
            r = check(root.right)
            if l == -1 or r == -1 or abs(l - r) > 1:
                return -1
            return 1 + max(l,r)
        return check(root) != -1


'''