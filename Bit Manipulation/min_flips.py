# Solved on 26/07/2024
# https://leetcode.com/problems/minimum-flips-to-make-a-or-b-equal-to-c/

# Note that the formula that bits should be counted for is (a or b) == c and not a or (b == c)
class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        flips = 0
        while a or b or c:
            # lsb = least significant bit
            # If c's lsb is 1 add 1 if the lsb of a|b isn't 1
            if (c & 1): flips += ((~(a | b)) & 1)
            # If c's lsb is 0 add 1 for each lsb in a and b which isn't 0
            else: flips += ((a & 1) + (b & 1))
            a >>= 1
            b >>= 1
            c >>= 1
        return flips
