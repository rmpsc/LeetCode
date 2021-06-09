# Difficulty: Medium
# Time: O(n) Space: O(n)
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left_products = []
        right_products = []
        answer = []
        prev_product = 1
        
        # previous products from left side
        for i in nums:
            left_products.append(prev_product)
            prev_product *= i
            
        prev_product = 1
        # previous products from left side
        for i in reversed(nums):
            right_products.append(prev_product)
            prev_product *= i
        
        right_products = list(reversed(right_products))
        
        for i in range(len(nums)):
            answer.append(left_products[i] * right_products[i])
        
        return answer