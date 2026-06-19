class Solution:
    def maxProfit(self, prices: List[int]) -> int:
# If the price at r is higher than at l, we can make a profit — so we update the maximum.
# If the price at r is lower, then r becomes the new l because a cheaper buying price is always better.
        left = 0  # buy
        right = 1    # sell

        maxprofit = 0
        while right < len(prices):
            if prices[left] < prices[right]:
                profit = prices[right] - prices[left]
                maxprofit = max(maxprofit, profit)
            else:
                left = right
            right += 1
        return maxprofit

        # T: O(n)
        # S: O(1)