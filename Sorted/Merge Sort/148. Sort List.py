'''
Input: head = [4,2,1,3]
Output: [1,2,3,4]
Example 2:


Input: head = [-1,5,3,4,0]
Output: [-1,0,3,4,5]
Example 3:

Input: head = []
Output: []
'''
'''
class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        prev, slow, fast = None, head, head
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next
        prev.next = None

        left = self.sortList(head)
        right = self.sortList(slow)

        return self.merger(left, right)

    def merger(self, left, right):
        n = ListNode(0)
        lte = n
        while right and left:
            if left.val < right.val:
                lte.next = left
                left = left.next
            else:
                lte.next = right
                right = right.next
            lte = lte.next
        if right:
            lte.next = right
        if left:
            lte.next = left
        return n.next
'''
