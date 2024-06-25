# Solved on 07/06/2024
# https://leetcode.com/problems/find-the-difference-of-two-arrays/

class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        answer = [[], []]
        distinct_n1 = sorted(list(set(nums1)))
        distinct_n2 = sorted(list(set(nums2)))
        l1, l2 = len(distinct_n1), len(distinct_n2)
        i, j = 0, 0
        while i < l1 or j < l2:
            while (i < l1 and j < l2) and distinct_n1[i] == distinct_n2[j]:
                num = distinct_n1[i]
                while i < l1 and distinct_n1[i] == num:
                    i += 1
                while j < l2 and distinct_n2[j] == num:
                    j += 1
            if not(i < l1 or j < l2): break
            elif i < l1 and j < l2:
                if distinct_n1[i] < distinct_n2[j]:
                    num = distinct_n1[i]
                    answer[0].append(num)
                    while i < l1 and distinct_n1[i] == num:
                        i += 1
                else:
                    num = distinct_n2[j]
                    answer[1].append(num)
                    while j < l2 and distinct_n2[j] == num:
                        j += 1
            elif i < l1:
                num = distinct_n1[i]
                answer[0].append(num)
                while i < l1 and distinct_n1[i] == num:
                    i += 1
            else:
                num = distinct_n2[j]
                answer[1].append(num)
                while j < l2 and distinct_n2[j] == num:
                    j += 1
        return answer
