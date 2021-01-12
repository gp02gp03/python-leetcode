'''
Example 1:

Input: 1->1->2
Output: 1->2
Example 2:

Input: 1->1->2->3->3
Output: 1->2->3

'''
'''
    def deleteDuplicates(self, head):
        ite = head
        while ite:
            tmp = ite.next
            while tmp and tmp.val == ite.val:
                tmp = tmp.next
            ite.next = tmp
            ite = ite.next
        return head


'''