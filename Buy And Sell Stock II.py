#TC: O(n)
#SC: O(1)
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        profit = 0
        
        for i in range(1,len(prices)):
            if prices[i]>prices[i-1]:
                transaction = prices[i] - prices[i-1]
                profit += transaction
        return profit