'''
Input:
    3
   / \
  9  20
    /  \
   15   7
Output: [3, 14.5, 11]
Explanation:
The average value of nodes on level 0 is 3,  on level 1 is 14.5, and on level 2 is 11. Hence return [3, 14.5, 11].


def averageOfLevels(self, root: TreeNode) -> List[float]:
  res = []
  q = [root]
  while q:
    tmp = []
    sum = 0
    for i in q :
      sum += i.val
      if i.left:
        tmp.append(i.left)
        if i.right:
          tmp.append(i.right)
    res.append(sum / len(q))
    q = tmp
  return res

'''