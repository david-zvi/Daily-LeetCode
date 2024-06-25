# Solved on 15/06/2024
# https://leetcode.com/problems/dota2-senate/

from collections import deque

class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        queue = deque(senate)
        n = len(queue)
        bans = 0
        group = ''
        while bans < n:
            next_senator = queue.popleft()
            if not group or group == next_senator: 
                group = next_senator
                bans += 1
                queue.append(next_senator)
            else:
                bans -= 1
                n -= 1
                if bans == 0: group = ''
        return "Radiant" if queue[0] == 'R' else "Dire"
            

