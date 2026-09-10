class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        index, min, max = 0, prices[0], 0
        if not prices:
            return 0
        for i in range(len(prices)):
            if prices[i] < min:
                min = prices[i]
            elif prices[i] - min > max:
                max = prices[i] - min

        return max
