# Solved on 08/06/2024
# https://leetcode.com/problems/unique-number-of-occurrences/

class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        counts = dict()
        for num in arr:
            if num in counts: counts[num] += 1
            else: counts[num] = 1
        return sorted(list(set(counts.values()))) == sorted(list(counts.values()))
