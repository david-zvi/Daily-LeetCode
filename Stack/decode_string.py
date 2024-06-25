# Solved on 13/06/2024
# https://leetcode.com/problems/decode-string/

class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        cur_str = ""
        cur_reps = 0
        for c in s:
            if c.isdigit():
                cur_reps = 10*cur_reps + int(c)
            elif c == '[':
                stack.append(cur_reps)
                stack.append(cur_str)
                cur_reps = 0
                cur_str = ""
            elif c == ']':
                prev_str = stack.pop()
                prev_reps = stack.pop()
                cur_str = prev_str + cur_str*prev_reps
            else:
                cur_str += c
        while stack: cur_str = stack.pop() + cur_str
        return cur_str
