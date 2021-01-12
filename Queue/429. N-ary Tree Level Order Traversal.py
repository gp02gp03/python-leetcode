def levelOrder(root):
  result = []
  if not root:
    return result
  from collections import deque
  q = deque([root])
  while q:
    count = len(q)
    level = []
    while count > 0:
      n = q.popleft()
      level.append(n.value)
      for c in n.children:
        q.append(c)
        count -= 1
        result.append(level)
    return result


print(levelOrder([1, None, 3, 2, 4, None, 5, 6]))
