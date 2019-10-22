#!/usr/bin/env python3
# coding: utf-8

# https://leetcode.com/problems/minimum-window-substring/
# https://leetcode.com/problems/minimum-window-substring/discuss/26804/12-lines-Python
# https://leetcode.com/problems/minimum-window-substring/discuss/26808/Here-is-a-10-line-template-that-can-solve-most-'substring'-problems
# Time complexity: O(n)
# Space complexity: O(n)


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need = collections.Counter(t)
        missing = len(t)
        start = i = 0
        end = 0
        for j, char in enumerate(s, 1):
            if need[char] > 0:  # 遇到t里面的词语，而且missing还需要，需要-missing
                missing -= 1
            need[char] -= 1  # 所有词都需要减need
            if missing == 0:
                while i < j and need[s[i]] < 0:  # 如果遇到need<0证明该词不再t里面，或者有重复，多个包含在t里的词，需要过掉
                    need[s[i]] += 1
                    i += 1
                if end == 0 or j - i < end - start:  # 更新新的窗口
                    start, end = i, j
                need[s[i]] += 1  # i需要往前走一步，原来的need要加上
                i += 1
                missing += 1

        return s[start:end]
