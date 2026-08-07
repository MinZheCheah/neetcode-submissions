class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        xorr = n

        for i in range(n):
            # a ⊕ a = 0 (a number cancels itself)
            # a ⊕ 0 = a
            xorr ^= i ^ nums[i]
        return xorr

    # T: O(n)
    # S: O(1)