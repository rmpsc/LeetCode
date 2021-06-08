# Time: O(n) Space: O(1)
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        nums.sort()
        if nums[-1] == n - 1:
            return n
        for i in range(n):
            if nums[i] != i:
                return i