# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Time: O(n) Space: O(1)
class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if head is None or head.next is None:
            return False
        
        slow = fast = head
        
        while fast is not None and slow is not None:
            slow = slow.next
            
            # you must check if there is a valid node for fast
            if fast.next is None:
                return False
            fast = fast.next.next
            
            if slow == fast:
                return True
        
        return False
