# Time: O(n) Space: O(n)
class Solution(object):
    def findDisappearedNumbers(self, nums):
        num_set = set(nums)
        missing = []
        for i in range(len(nums)):
            if i + 1 not in num_set:
                missing.append(i + 1)
        return missing