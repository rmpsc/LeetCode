# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# Time: O(n) Space: O(1)
class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        dummy = ListNode
        dummy.next = head
        
        curr = head
        prev = dummy
        
        
        while curr is not None:
            if curr.val == val:
                prev.next = curr.next
            else:
                # cannot put in if statement bc curr is no longer apart of linked list
                prev = curr
            curr = curr.next
        
        return dummy.next
                
                