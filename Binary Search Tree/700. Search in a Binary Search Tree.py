'''
    def searchBST(self, root, val):
        n = root
        while n:
            if val == n.val:
                return n
            if val < n.val:
                n = n.left
            else:
                n = n.right
        return n



'''