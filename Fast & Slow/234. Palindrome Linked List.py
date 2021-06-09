# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# Time: O(n) Space: O(1)
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        slow = fast = head
        
        # slow pointer will stop at middle
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # reverse half of linked list
        prev = None
        while slow:
            temp = slow.next
            slow.next = prev
            prev = slow
            slow = temp
        
        l, r = head, prev
        while r:
            if l.val != r.val:
                return False
            l = l.next
            r = r.next

        return True
        