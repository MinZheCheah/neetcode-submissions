class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # optimal
        # left pointer at the start of list
        # right pointer at end of list
        res = 0
        i = 0
        j = len(heights) - 1

        while i < j:
            res = max(res, min(heights[i], heights[j]) * (j - i)) # max area: width * height
            if heights[i] < heights[j]:
                i += 1
            else:
                j -= 1
        return res

        # T: O(n)
        # S: O(1)
