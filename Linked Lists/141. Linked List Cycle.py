# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# COULD BE DONE WITH O(1) SPACE
class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        visited = set()
        
        while head is not None:
            visited.add(head)
            if head.next in visited:
                return True
            head = head.next
            
        return False