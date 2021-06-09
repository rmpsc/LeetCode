# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# Time: O(n) Space: O(1)
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        dummy = ListNode(next=head)
        
        prev, curr = dummy, head
        
        # if you check curr.next inside while loop, you must adjust while loop for that
        while curr and curr.next:
            if curr.val == curr.next.val:
                prev.next = curr.next
            else:
                prev = curr
            curr = curr.next
        
        return dummy.next