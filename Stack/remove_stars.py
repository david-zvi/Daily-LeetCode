# Solved on 11/06/2024
# https://leetcode.com/problems/removing-stars-from-a-string/

class Solution:
    def removeStars(self, s: str) -> str:
        n = len(s)
        ret = []
        for letter in s:
            if letter == '*':
                if ret:
                    ret.pop()
            else: ret.append(letter)
        return "".join(ret)
