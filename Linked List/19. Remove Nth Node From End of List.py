'''
Example 1:
Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]

Example 2:
Input: head = [1], n = 1
Output: []

Example 3:
Input: head = [1,2], n = 1
Output: [1]

def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
    first = ListNode(0)
    second = ListNode(0)
    first.next = head
    second.next = head
    for i in range(n):
        first = first.next
    if first.next == None:
        return head.next
    while first.next != None:
        first = first.next
        second = second.next
    second.next = second.next.next
    return head

'''