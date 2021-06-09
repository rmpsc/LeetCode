# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# EASY
# Time: O(n) Space: O(1)
class Solution:
    def isSubtree(self, root: TreeNode, subRoot: TreeNode) -> bool:
        
        def isSameTree(root, subRoot):
            if root is None and subRoot is None:
                return True
            elif root is None or subRoot is None:
                return False
            elif root.val == subRoot.val:
                return (isSameTree(root.left, subRoot.left) and
                        isSameTree(root.right, subRoot.right))
            
        if root is None:
            return False
        elif isSameTree(root, subRoot):
            return True
        else:
            return (self.isSubtree(root.left, subRoot) or
                   self.isSubtree(root.right, subRoot))
        