# Difficulty: Medium
# Time: O(n) Space: O(n)
class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        hashbrown = {}
        output = []
        # counts amount of each num
        for i in nums:
            if i in hashbrown:
                hashbrown[i] += 1
            else:
                hashbrown[i] = 1
        
        for key, val in hashbrown.items():
            if val == 2:
                output.append(key)
            
        return output
        