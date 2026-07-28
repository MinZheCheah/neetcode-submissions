class Solution:
    def reverseBits(self, n: int) -> int:
        # Bit Mani
        # extract each bit from original number starting from least significant bit
        # place that bit into correct reversed position in the result
        # repeat for all 32 bits

        res = 0

        for i in range(32):
            bit = (n >> i) & 1 # extract the ith bit of n
            res = res | (bit << (31 - i)) # shift this bit to position 31 - i
        return res

        # T: O(1)
        # S: O(1)