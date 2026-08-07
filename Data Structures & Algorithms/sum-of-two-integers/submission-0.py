class Solution:
    def getSum(self, a: int, b: int) -> int:
        # b = carry
        mask = 0xFFFFFFFF
        max_int = 0x7FFFFFFF

        while (b != 0):
            
            carry = (a & b) << 1

            # compute sum without carry
            a = (a ^ b) & mask
            b = carry & mask

        return a if a <= max_int else  ~(a ^ mask)





        # T: O(1)
        # S: O(1)