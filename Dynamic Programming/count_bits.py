# Solved on 24/07/2024
# https://leetcode.com/problems/counting-bits/

class Solution:
    def countBits(self, n: int) -> List[int]:
        # Will hold bit counts for every 0 <= i <= n
        bit_counts = [0]*(n+1)
        # See how many bits i shifted right by one has (base case being 0 having
        # zero 1 bits) and add 1 if the rightmost bit is 1
        for i in range(1, n+1): bit_counts[i] = bit_counts[i >> 1] + (i & 1)
        return bit_counts
