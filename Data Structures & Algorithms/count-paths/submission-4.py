class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # DP
        # use memoization to cache results of recursive calls. 
        # use hash map or 2d array to store results

        row = [1] * n

        for i in range(m - 1):
            newRow = [1] * n
            # go through every column except right most (always 1)
            for j in range(n - 2, -1, -1):
                # compute new row
                newRow[j] = newRow[j + 1] + row[j]
            row = newRow
        return row[0]

        # T: O(m*n)
        # S: O(m*n)