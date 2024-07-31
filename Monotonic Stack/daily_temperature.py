# Solved on 31/07/2024
# https://leetcode.com/problems/daily-temperatures/

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # Monotonically increasing stack of indexes - every index from 0 to n
        # represents the temperature at that index, and if temp[i] < temp[j]
        # i will be higher in the stack than j.
        n = len(temperatures)
        answers = [0]*n
        stack = []
        for i in range(n):
            cur_temp = temperatures[i]
            if stack and temperatures[stack[-1]] < cur_temp:
                while stack and temperatures[stack[-1]] < cur_temp:
                    temp_index = stack.pop()
                    answers[temp_index] = i - temp_index
            stack.append(i)
        return answers
