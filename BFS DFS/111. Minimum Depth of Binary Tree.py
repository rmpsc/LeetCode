# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# EASY
# Time: O(n) Space: O(n)
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if root is None:
            return 0
        
        queue = [root]
        min_depth = 1
        
        while queue:
            size = len(queue)
            
            for i in range(size):
                cur = queue.pop(0)
                
                if cur.left is None and cur.right is None:
                    return min_depth
                else:
                    queue.append(cur.left) if cur.left else None
                    queue.append(cur.right) if cur.right else None
            
            min_depth += 1
            