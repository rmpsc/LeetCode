# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# EASY
# Time: O(n) Space: O(n)
class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        result = []
        queue = [root]
        
        while queue:
            lvl_sum = 0
            size = len(queue)
            
            for i in range(size):
                cur = queue.pop(0)
                lvl_sum += cur.val
                
                queue.append(cur.left) if cur.left else None
                queue.append(cur.right) if cur.right else None
            
            lvl_avg = lvl_sum / size
            result.append(lvl_avg)
        
        return result
