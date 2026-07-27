class Solution:
    def hammingWeight(self, n: int) -> int:
        # Bit Mask
        # res = 0
        # for i in range(32):
        #     if (1<<i) & n:  # create a mask with only the ith bit set
        #         res += 1
        # return res

        # T: O(1) 
        # S: O(1)

        res = 0
        while n:
            n &= (n - 1) # remove the rightmost 1 bit
            res += 1
        return res

        # T: O(1) 
        # S: O(1)
