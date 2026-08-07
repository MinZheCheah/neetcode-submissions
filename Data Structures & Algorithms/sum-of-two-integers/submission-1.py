class Solution:
    def getSum(self, a: int, b: int) -> int:
        mask = 0xFFFFFFFF # keep only 32 bits
        max_int = 0x7FFFFFFF # as largest 32-bit signed integer

        while (b != 0):
            carry = (a & b) << 1
            # compute sum without carry
            a = (a ^ b) & mask
            # move carry into b
            b = carry & mask
        # after loop a holds res. if a within signed range return
        # otherwise convert from unsigned 32-bit to a negative signed value
        return a if a <= max_int else  ~(a ^ mask)





        # T: O(1)
        # S: O(1)