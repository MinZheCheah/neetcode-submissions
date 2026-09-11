class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        # DP Top Down
        if len(s1) + len(s2) != len(s3):
            return False

        dp = {}

        def dfs(i, j, k):
            if k == len(s3):
                return (i == len(s1)) and (j == len(s2))

            if (i, j) in dp:
                return dp[(i, j)]

            res = False
            # Try taking the next character from s1 if it matches s3[k]
            if i < len(s1) and s1[i] == s3[k]:
                res = dfs(i + 1, j, k + 1)
            # If that does not work, try taking the next character from s2 if it matches s3[k]
            if not res and j < len(s2) and s2[j] == s3[k]:
                res = dfs(i, j + 1, k + 1)

            dp[(i, j)] = res
            return res

        return dfs(0, 0, 0)

        #T: O(m*n)
        #S: O(m*n)