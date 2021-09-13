'''
Example 1:
Input: root = [1,7,0,7,-8,null,null]
Output: 2
Explanation:
Level 1 sum = 1.
Level 2 sum = 7 + 0 = 7.
Level 3 sum = 7 + -8 = -1.
So we return the level with the maximum sum which is level 2.

Example 2:

Input: root = [989,null,10250,98693,-89388,null,null,null,-32127]
Output: 2

'''


'''
deque res:

deque
(
 [
   TreeNode
   {
    val: 1,
	left:
	    TreeNode
		{
	      val: 7,
		  left:
		    TreeNode
			{
			  val: 7,
			  left: None,
			  right: None
			},
			right:
			  TreeNode
			  {
				val: -8,
				left: None,
				right: None
			  }
		},
	right:
		TreeNode
		{
		  val: 0,
		  left: None,
		  right: None
		}
 ]
)

'''

'''
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        level,res,resLevel = 1,float(-inf),1
        q = collections.deque([root])
        while q:
            cur= 0
            count = len(q)
            while count > 0:
                n = q.popleft()
                cur += n.val
                if n.left: q.append(n.left)
                if n.right: q.append(n.right)
                count -= 1
            if cur > res:
                res = cur
                resLevel = level
            level +=1
        return resLevel
'''