# Solved on 03/06/2024
# https://leetcode.com/problems/max-consecutive-ones-iii/

class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        n = len(nums)
        ones = []
        counter = 0
        for i in range(n):
            if nums[i] == 0: 
                ones.append(counter)
                counter = 0
            else: counter += 1
        ones.append(counter)
        
        if k == 0: return max(ones)

        num_zeros = len(ones) - 1
        if k >= num_zeros: return n

        s = sum(ones[:k+1]) + k
        m = s
        for i in range(k+1, num_zeros + 1):
            s += ones[i] - ones[i-k-1]
            m = max(s, m)
        
        return m
