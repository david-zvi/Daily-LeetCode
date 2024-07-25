# Solved on 25/07/2024
# https://leetcode.com/problems/single-number/

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        xor = 0
        # xor of a number with itself is zero, so if we xor all the numbers together
        # we'll get the number that appears only once.
        for num in nums: xor ^= num
        return xor
