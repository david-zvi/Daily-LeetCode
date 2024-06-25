# Solved on 24/05/2024
# https://leetcode.com/problems/reverse-vowels-of-a-string/

class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowels = {'A', 'a', 'E', 'e', 'I', 'i', 'O', 'o', 'U', 'u'}
        s_list = list(s)
        l = 0
        r = len(s) - 1
        while l < r:
            while l < r and s_list[l] not in vowels:
                l += 1
            while l < r and s_list[r] not in vowels:
                r -= 1
            s_list[l], s_list[r] = s_list[r], s_list[l]
            l += 1
            r -= 1
        return "".join(s_list)
       

        
