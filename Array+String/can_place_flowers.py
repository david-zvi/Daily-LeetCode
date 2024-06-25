# Solved on 24/05/2024
# https://leetcode.com/problems/can-place-flowers/description/

class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        if not len(flowerbed):
            return 0 >= n
        if len(flowerbed) == 1:
            return ((flowerbed[0] + 1) % 2) >= n
        if len(flowerbed) <= n:
            return False
        flowers = 0
        new_flowerbed = flowerbed[:]
        size = len(flowerbed)
        for i in range(size): 
            if not new_flowerbed[i]:
                if (i == 0 and not new_flowerbed[i+1]) or \
                    (i == size - 1 and not new_flowerbed[i-1]) or \
                    (not new_flowerbed[i-1] and not new_flowerbed[i+1]):
                    new_flowerbed[i] = 1
                    flowers += 1
        return flowers >= n
        
