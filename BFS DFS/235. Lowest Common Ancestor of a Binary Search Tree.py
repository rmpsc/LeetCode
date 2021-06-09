# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# EASY
# Time: O(n) Space: O(1)
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        r_val = root.val
        p_val = p.val
        q_val = q.val
        
        if p_val > r_val and q_val > r_val:
            return self.lowestCommonAncestor(root.right, p, q)
        elif p_val < r_val and q_val < r_val:
            return self.lowestCommonAncestor(root.left, p, q)
        else:
            return root
