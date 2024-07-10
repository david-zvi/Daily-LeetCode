# Solved on 10/07/2024
# https://leetcode.com/problems/guess-number-higher-or-lower/

# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        def binary_search(l, r):
            mid = (l+r)//2
            guess_res = guess(mid)
            if guess_res == 0: return mid
            elif guess_res == -1: return binary_search(l, mid)
            return binary_search(mid+1, r)
        return binary_search(1, n)
        
