# Time: O(n) Space: O(1)
class Solution(object):
    def maxProfit(self, prices):
        min_buy = 100000
        max_profit = 0
        
        for price in prices:
            if price < min_buy:
                min_buy = price
            max_profit = max(max_profit, price - min_buy)
        
        return max_profit