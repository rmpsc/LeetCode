# Time: O(n) Space: O(1)
class Solution(object):
    def maxSubArray(self, nums):
        curr_sum = max_sum = nums[0]
        
        for i in nums[1:]:
            curr_sum = max(i, curr_sum + i) # either gives us the number that can stand on its own or adds that number
            max_sum = max(max_sum, curr_sum)
            
        return max_sum
    