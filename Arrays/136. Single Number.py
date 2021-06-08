# Time: O(n) Space: O(n)
class Solution(object):
    def singleNumber(self, nums):
        hashh = {}
        for i in nums:
            if i in hashh:
                hashh[i] += 1
            else:
                hashh[i] = 1
        for key in hashh:
            if hashh[key] == 1:
                return key

# Time: O(n) Space: O(1)
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        a = 0
        for i in nums:
            a ^= i
        return a