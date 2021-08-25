'''
Input: root = [5,3,6,2,4,null,7], k = 9
Output: true

Input: root = [5,3,6,2,4,null,7], k = 28
Output: false
Example 3:

Input: root = [2,1,3], k = 4
Output: true
Example 4:

Input: root = [2,1,3], k = 1
Output: false
Example 5:

Input: root = [2,1,3], k = 3
Output: true
'''

'''
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        tmp = set()
        q = [root]
        while q:
            n = q.pop()
            if k-n.val in tmp:
                return True
            tmp.add(n.val)
            if n.left:
                q.append(n.left)
            if n.right:
                q.append(n.right)
        return False

'''
