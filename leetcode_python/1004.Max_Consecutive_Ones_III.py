#!/usr/bin/env python3
# coding: utf-8

# Time complexity: O()
# Space complexity: O()

# https://leetcode.com/problems/max-consecutive-ones-iii/

class Solution(object):
    def longestOnes(self, A, K):
        i = 0
        count = 0
        max_len = 0

        for j, char in enumerate(A):
            if A[j] == 0:
                count += 1

            while count > K:
                if A[i] == 0:
                    count -= 1
                i += 1

            max_len = max(max_len, j-i+1)
        return max_len