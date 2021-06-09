# EASY
# Time: O(n) Space: O(n)
class Solution(object):
    def twoSum(self, nums, target):
        hashbrown = {}  # value : index
        
        for i, val in enumerate(nums):
            diff = target - val
            if diff in hashbrown:
                return [i, hashbrown[diff]]
            hashbrown[nums[i]] = i
                