'''
Input: root = [4,2,6,3,1,5], val = 1, depth = 2
Output: [4,1,1,2,null,null,6,3,1,5]

Input: root = [4,2,null,3,1], val = 1, depth = 3
Output: [4,2,null,1,1,3,null,null,1]


class Solution:
    def addOneRow(self, root: TreeNode, val: int, depth: int) -> TreeNode:
        if depth == 1:
            n = TreeNode(val)
            n.left = root
            return n
        q = [root]
        for _ in range(depth-2):
            tmp = []
            for j in q:
                if j.left:
                    tmp.append(j.left)
                if j.right:
                    tmp.append(j.right)
            q = tmp
        for node in q:
            tmp = node.left
            node.left = TreeNode(val)
            node.left.left = tmp
            tmp = node.right
            node.right = TreeNode(val)
            node.right.right = tmp
        return root
            
'''