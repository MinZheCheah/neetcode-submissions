class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        # Bottom Up
        n = len(coins)
        coins.sort()
        dp = [[0] * (amount + 1) for _ in range(n + 1)]

        for i in range(n + 1):
            dp[i][0] = 1
        
        for i in range(n - 1, -1, -1):
            for a in range(amount + 1):
                # if cur coin can be used
                if a >= coins[i]:
                    dp[i][a] = dp[i + 1][a] # skip cur coin
                    dp[i][a] += dp[i][a - coins[i]]  # use cur coin

        return dp[0][amount]


            
        # T: O(n*a)
        # S: O(n*a)