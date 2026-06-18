class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # brute force
        # left and right pointer, 
        # move pointer to the right to the end and then point left
        res = 0

        for i in range(len(heights)):
            for j in range(i + 1, len(heights)):
                res = max(res, min(heights[i], heights[j]) * (j - i))
        return res

        T: O(n^2)

        
