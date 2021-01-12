'''
def mergeTwoLists(self, l1, l2):
    dummy = ListNode(None)
    prev = dummy
    while l1 and l2:
        if l1.val <= l2.val:
            prev.next = l1
            l1 = l1.next
        else:
            prev.next = l2
            l2 = l2.next
            prev = prev.next
        prev.next = l1 or l2

    return dummy.next
'''
