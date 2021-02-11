'''
Given a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.

Example:

Input: [1,2,3,null,5,null,4]
Output: [1, 3, 4]
'''
'''
from collections import deque
class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        if not root: return []
        res = []
        q = deque([root])
        while q:
            count = len(q)
            for i in range(count):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            res.append(node.val)
        return res
'''