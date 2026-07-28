class Solution:
    def countBits(self, n: int) -> List[int]:
        # brute force
        # T: O(n log n)
        # S: O(1)

        # DP (Optimal)
        # 1 + dp[n - 4]

        dp = [0] * (n + 1)
        offset = 1 # tracks the most recent power of two

        for i in range(1, n + 1):
            if offset * 2 == i:
                offset = i
            # dp[i] = number of bits 
            dp[i] = 1 + dp[i - offset]
        
        return dp


        # T: O(n)
        # S: O(n)

        