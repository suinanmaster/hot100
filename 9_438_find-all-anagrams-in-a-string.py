"""
https://leetcode.cn/problems/find-all-anagrams-in-a-string/?envType=study-plan-v2&envId=top-100-liked

438. 找到字符串中所有字母异位词

给定两个字符串 s 和 p，找到 s 中所有 p 的 异位词 的子串，返回这些子串的起始索引。不考虑答案输出的顺序。



示例 1:

输入: s = "cbaebabacd", p = "abc"
输出: [0,6]
解释:
起始索引等于 0 的子串是 "cba", 它是 "abc" 的异位词。
起始索引等于 6 的子串是 "bac", 它是 "abc" 的异位词。
 示例 2:

输入: s = "abab", p = "ab"
输出: [0,1,2]
解释:
起始索引等于 0 的子串是 "ab", 它是 "ab" 的异位词。
起始索引等于 1 的子串是 "ba", 它是 "ab" 的异位词。
起始索引等于 2 的子串是 "ab", 它是 "ab" 的异位词。


提示:

1 <= s.length, p.length <= 3 * 104
s 和 p 仅包含小写字母
"""

import collections
from typing import List


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        ans = []
        target = [0] * 26
        for c in p:
            target[ord(c) - ord("a")] += 1
        windows = [0] * 26
        for c in s[: len(p)]:
            windows[ord(c) - ord("a")] += 1
        if windows == target:
            ans.append(0)
        for index, c in enumerate(s[len(p) :]):
            windows[ord(c) - ord("a")] += 1
            windows[ord(s[index]) - ord("a")] -= 1
            if windows == target:
                ans.append(index + len(p))
        return ans


if __name__ == "__main__":
    s = Solution()
    print(s.findAnagrams("cbaebabacd", "abc"))
