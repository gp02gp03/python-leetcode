def lowestCommonAncestor(root, p,q):
    while True:
        rootVal = root.val
        if (p.val >= rootVal and q.val <= rootVal) or (p.val <= rootVal and q.val >= rootVal) :
            return root
        elif p.val > rootVal and q.val > rootVal:
            root = root.right
        else:
            root = root.left
print(lowestCommonAncestor([6,2,8,0,4,7,9,None,None,3,5],2,8))
