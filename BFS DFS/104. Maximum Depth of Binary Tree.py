# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# EASY
# Time: O(n) Space: O(1)
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        max_d = [0]
        
        def dfs(root):
            if root is None:
                return 0
            left = self.maxDepth(root.left)
            right = self.maxDepth(root.right)
            
            depth = max(left, right) + 1
            max_d[0] = max(max_d[0], depth)
            
            return depth
            
        dfs(root)
        return max_d[0]
    