# Time: O(n) Space: O(1)
class Solution(object):
    def climbStairs(self, n):
        prev = 0
        prev2 = 1
        temp = 0
        
        for i in range(n):
            temp = prev  # holds old value of prev
            prev = prev2  # prev becomes prev2
            prev2 += temp
        
        return prev2