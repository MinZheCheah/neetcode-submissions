class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # Bottom up
        # create 2d array with extra columns and rows filled with 0
        dp = [[0 for j in range(len(text2) + 1)] for i in range(len(text1) + 1)]

        for i in range(len(text1) - 1, -1, -1):
            for j in range(len(text2) -1, -1, -1):
                if text1[i] == text2[j]:
                    # add 1, move diagonally
                    dp[i][j] = 1 + dp[i + 1][j + 1]
                else:
                    # find max value of moving to the right and down
                    dp[i][j] = max(dp[i][j + 1], dp[i+ 1][j])
        return dp[0][0]

        # T: O(m*n)
        # S: O(m*n)