class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Top Down
        # State: Buying or Selling?
        # If Buy -> i + 1
        # If Sell -> i + 2 (have to take cooldown day)

        dp = {} # key = (i, buying) val=max_profit
        def dfs(i, buying):
            # base cases
            if i >= len(prices):
                return 0
            if (i, buying) in dp:
                return dp[(i, buying)]

            if buying:
                buy = dfs(i + 1, not buying) - prices[i]
                cooldown = dfs(i + 1, buying)
                dp[(i, buying)] = max(buy, cooldown) # cache solution
            else:
                sell = dfs(i + 2, not buying) + prices[i]
                cooldown = dfs(i + 1, buying)
                dp[(i, buying)] = max(sell, cooldown) # cache solution
            return dp[(i, buying)]
        return dfs(0, True)

        # T: O(n)
        # S: O(n)




            



