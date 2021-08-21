# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

'''
step 1 => 先求出整棵樹所有節點的總和
step 2 => 透過dfs求出左右子樹個別的和
step 3 => 更新結果t*(s-t)
'''

'''
class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        def dfs(root):
            if not root:
                return 0
            left, right = dfs(root.left), dfs(root.right)
            res[0] = max(res[0], left * (s[0] - left), right * (s[0] - right))
            return root.val + left + right
        sum = 0
        q = [root]
        while q:
            cur = q.pop()
            sum = sum + cur.val
            if cur.left:
                q.append(cur.left)
            if cur.right:
                q.append(cur.right)

        res = [0]  # initial result
        s = [sum]  # sum of all nodes
        dfs(root)

        return res[0] % (10**9 + 7)
'''
