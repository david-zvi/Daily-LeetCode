# Solved on 19/07/2024
# https://leetcode.com/problems/domino-and-tromino-tiling/

class Solution:
    def numTilings(self, n: int) -> int:
        # Base cases:
        # 2x0: 1 - only one way (to not add dominos)
        # 2x1: 1 - single way to fit a domino
        # 2x2: 2 - two ways to fit a pair of dominos
        last_two = [1, 2]
        if n < 3: return last_two[n-1]
        sum_till_m_minus_2 = 1
        # From here, for each 2 < m <= n we look at the number of ways with each piece combination on the side of the 2xm board,
        # and the total number of possible ways to fill the board is the sum of the following:
        for m in range(3, n+1):
            # If there's a 2x1 domino on the side: number of ways to fill an 2x(m-1) board.
            # If there are two horisontal dominos (one on top of the other) on the side: number of ways to fill an 2x(m-2) board.
            # If there's a tromino on the side (with the entire side covered by two of it's parts - or else it's not a legal way to fill the board),
            # we can add any 0 <= k <= n-3 horisontal dominos after it, add another tromino to make what we've filled a full 2x(2+k) board,
            # and then we have the possible number of ways to fill a 2x(n-(2+k)) board possibilities to fill the rest of the board -
            # in total 2*sum([number of ways to fill a 2xk board for k in range(n-1)]) ways (2 ways for each orientation of the initial tromino).
            # In total: number of ways to fill an 2x(m-1) board + number of ways to fill an 2x(m-2) board + 2*sum([number of ways to fill a 2xk board for k in range(n-1)])
            next_num = sum(last_two) + 2*sum_till_m_minus_2
            sum_till_m_minus_2 += last_two[0]
            last_two[0], last_two[1] = last_two[1], next_num
        return last_two[-1]%(10**9 + 7)
