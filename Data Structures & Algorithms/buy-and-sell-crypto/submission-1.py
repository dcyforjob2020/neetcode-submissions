class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        result = 0

        min_price = prices[0]

        for price in prices:
            result = max(result, price - min_price)

            min_price = min(min_price, price)

        return result
