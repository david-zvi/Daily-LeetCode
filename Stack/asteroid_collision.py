# Solved on 12/06/2024
# https://leetcode.com/problems/asteroid-collision/

class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        after = []
        for asteroid in asteroids:
            if after and asteroid < 0 and after[-1] > 0:
                add_next = True
                while after and after[-1] > 0:
                    last = after[-1]
                    if -asteroid >= last: after.pop() # >= than last
                    if -asteroid <= last: # <= than last
                        add_next = False 
                        break
                if add_next: after.append(asteroid)
            else: after.append(asteroid)
        return after
