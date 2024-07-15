# Solved on 15/07/2024
# https://leetcode.com/problems/combination-sum-iii/

class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        self.combinations = []
        self.cur = []
        self.cur_sum = 0 # Faster than summing self.cur again and again

        def helper(num):
            self.cur.append(num)
            self.cur_sum += num
            l = len(self.cur)
            # If l == k and cur_sum == n add cur to the combonations
            if l == k:
                if self.cur_sum == n: self.combinations.append(self.cur[:])
            # If l < k add numbers to it till l == k
            elif l < k:
                for i in range(num + 1, 10): helper(i)
            self.cur_sum -= num
            self.cur.pop()
        
        for i in range(1,10): helper(i)
        return self.combinations
