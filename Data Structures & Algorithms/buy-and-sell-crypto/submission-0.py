class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        for left in range(0, len(prices) -1):
            right = left + 1
            maxPrice = 0
            while right < len(prices):
                maxPrice = max(maxPrice, prices[right])
                right += 1
            maxProfit = max(maxProfit, (maxPrice - prices[left]))
        return maxProfit