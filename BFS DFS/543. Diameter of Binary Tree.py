# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# EASY
# Time: O(n) Space: O(1)
class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        max_d = [0]
        
        def dfs(root):
            left = dfs(root.left) if root.left else -1
            right = dfs(root.right) if root.right else -1
            
            max_d[0] = max(max_d[0], left + right + 2)
            
            return max(left, right) + 1
        
        dfs(root)
        return max_d[0]
    