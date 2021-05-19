class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        price = 0
        min_size = sys.maxsize
        
        for i in prices:
            min_size = min(min_size,i)
            price = max(price, i-min_size)
        
        return price

# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
