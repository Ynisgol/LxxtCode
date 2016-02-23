class Solution:
    """
    @param a: The first integer
    @param b: The second integer
    @return:  The sum of a and b
    """
    def aplusb(self, a, b):
        # write your code here, try to do it without arithmetic operators.

        count = 1
        carry = 0
        c = 0
        m = 1 << 31

        while (a != 0 or b != 0 or carry != 0) and m > 0:
            last_a = a & 1 # last bit
            last_b = b & 1
            currt = last_a ^ last_b ^ carry
            carry = (last_a & last_b) | (last_a & carry) | (carry & last_b)
            tmp = count
            while tmp > 1:
                currt <<= 1
                tmp >>= 1
            c |= currt
            a >>= 1
            b >>= 1
            count <<= 1
            m >>= 1

        return c

print Solution().aplusb(1000000000, 1000000000)
