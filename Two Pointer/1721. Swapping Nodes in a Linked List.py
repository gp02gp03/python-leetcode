'''
1. 設定兩個指針
2. 第一個指針先往右走找到第K個位置
3. 第一個及第二個指針同時繼續往右走,直到結束
4. 做交換

'''


'''
Input: head = [1,2,3,4,5], k = 2
Output: [1,4,3,2,5]
Example 2:

Input: head = [7,9,6,6,7,8,3,0,9,5], k = 5
Output: [7,9,6,6,8,7,3,0,9,5]
Example 3:

Input: head = [1], k = 1
Output: [1]
Example 4:

Input: head = [1,2], k = 1
Output: [2,1]
Example 5:

Input: head = [1,2,3], k = 2
Output: [1,2,3]
'''

'''
class Solution:
    def swapNodes(self, head: ListNode, k: int) -> ListNode:
        first,second = head,head
        for i in range(k-1):
            first = first.next
        tmp = first
        while first.next:
            first = first.next
            second = second.next
        tmp.val,second.val = second.val, tmp.val
        return head

'''