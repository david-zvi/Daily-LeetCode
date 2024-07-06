# Solved on 27/05/2024
# https://leetcode.com/problems/string-compression/

class Solution(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        n = len(chars)
        if n < 2: return n
        sol_ptr = 0
        count = 0
        cur_char, last_char = chars[0], chars[0]
        ten_pow = 0
        for i in range(n):
            char_match = chars[i] == cur_char
            if char_match: 
                count += 1
                if count >= 10**(ten_pow + 1): ten_pow += 1
            if i == n-1 or not char_match:
                chars[sol_ptr] = cur_char
                sol_ptr += 1
                last_char = cur_char
                cur_char = chars[i]
                if count > 1:
                    # chars[sol_ptr] = str(count)
                    while ten_pow >= 0:
                        chars[sol_ptr] = str(count // (10**ten_pow))
                        sol_ptr += 1
                        ten_pow -= 1
                        count %= 10
                    # sol_ptr += 1
                count = 1
                ten_pow = 0
        # if not chars[sol_ptr-1].isdigit(): 
        if last_char != cur_char:
            chars[sol_ptr] = cur_char
            sol_ptr += 1
        return sol_ptr
