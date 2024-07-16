# Solved on 16/07/2024
# https://leetcode.com/problems/n-th-tribonacci-number/

class Solution:
    def tribonacci(self, n: int) -> int:
        last_three = [0, 1, 1]
        if n < 3: return last_three[n]
        for i in range(3, n):
            ti = sum(last_three)
            last_three[0], last_three[1], last_three[2] = last_three[1], last_three[2], ti
        return sum(last_three)
