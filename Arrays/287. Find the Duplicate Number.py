# Difficulty: Medium
# Time: O(n) Space: O(n)
class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        hash = {}
        for i in nums:
            if i in hash:
                hash[i] += 1
            else:
                hash[i] = 1
        
        for key, val in hash.items():
            if val != 1:
                return key