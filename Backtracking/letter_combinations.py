# Solved on 14/07/2024
# https://leetcode.com/problems/letter-combinations-of-a-phone-number/

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits: return []
        self.combinations = []
        self.cur = []
        self.n = len(digits)

        # Returns a tuple of the start and end of the range of letters for digit.
        def get_letter_range(digit):
            start_inc = 1 if digit > 7 else 0
            end_inc = 1 if digit in (7,9) else 0
            start = 97 + 3 * (digit - 2) + start_inc
            return start, start + 3 + end_inc
        
        # Recursive function that backtracks on every letter for every digit
        # in digits and adds it to self.cur, and self.cur to self.combinations
        # if we got to the last digit.
        def helper(index: int):
            start, end = get_letter_range(int(digits[index]))
            for unicode_char in range(start, end):
                self.cur.append(chr(unicode_char))
                if index == self.n - 1: self.combinations.append(''.join(self.cur))
                else: helper(index + 1)
                self.cur.pop()
        
        helper(0)
        return self.combinations
