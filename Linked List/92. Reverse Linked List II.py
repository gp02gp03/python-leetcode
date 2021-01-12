'''
class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        if m == n: return head
        st = []
        left, node = None, head
        if m != 1:
            for i in range(1, m - 1):
                node = node.next
            left = node
            node = node.next # position m
        
        for i in range(m, n + 1):
            st.append(node)
            node = node.next
        
        l1, l2 = st.pop(), None
        if m == 1:
            head = l1
        else:
            left.next = l1
        
        while st:
            l2 = st.pop()
            l1.next = l2
            l1 = l2
        
        l1.next = node
        
        return head

'''