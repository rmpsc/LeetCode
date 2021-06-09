# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# MEDIUM
# Time: O(n) Space: O(1)
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        dummy = ListNode(next=head)
        runner = dummy
        
        while runner.next and runner.next.next:
            r1 = runner.next
            r2 = runner.next.next
            
            runner.next = r2
            r1.next = r2.next
            r2.next = r1
            
            runner = runner.next.next
        
        return dummy.next
