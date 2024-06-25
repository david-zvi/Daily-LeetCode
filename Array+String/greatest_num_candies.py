# Solved on 22/05/2024
# https://leetcode.com/problems/kids-with-the-greatest-number-of-candies/

class Solution:
    def kidsWithCandies(self, candies, extraCandies):
        max_candies = float("-inf")
        for num_candies in candies:
            max_candies = max(max_candies, num_candies)
        greatest = []
        for i in range(len(candies)):
            greatest.append(candies[i]+extraCandies >= max_candies)
        return greatest
