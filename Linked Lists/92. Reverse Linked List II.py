# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# MEDIUM
# Time: O(n) Space: O(1)
class Solution:
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        if head.next is None or left == right:
            return head
        
        dummy = ListNode(next=head)
        l = r = dummy
        end = head
        
        for i in range(left):
            l = l.next
        
        for i in range(right):
            r = r.next
            end = end.next
        
        prev = end
        # reversal
        # tsps tlpl
        while l != r:
            temp = l.next
            l.next = prev
            prev = l
            l = temp
        temp = l.next
        l.next = prev
        prev = l
        l = temp
        
        if head.next == end:
            return r
        else:
            move = dummy
            for i in range(left - 1):
                move = move.next
            move.next = r   
            return dummy.next