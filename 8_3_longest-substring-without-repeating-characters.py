"""
https://leetcode.cn/problems/longest-substring-without-repeating-characters/description/?envType=study-plan-v2&envId=top-100-liked

3. 无重复字符的最长子串

提示
给定一个字符串 s ，请你找出其中不含有重复字符的 最长 子串 的长度。



示例 1:

输入: s = "abcabcbb"
输出: 3
解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。注意 "bca" 和 "cab" 也是正确答案。
示例 2:

输入: s = "bbbbb"
输出: 1
解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。
示例 3:

输入: s = "pwwkew"
输出: 3
解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。
     请注意，你的答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串。


提示：

0 <= s.length <= 5 * 104
s 由英文字母、数字、符号和空格组成
"""


# upgrade
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # 哈希表记录每个字符最后一次出现的索引
        last_occur = {}
        left = 0
        max_len = 0

        for right, ch in enumerate(s):
            # 如果字符已经出现过且在窗口内，则移动左指针
            if ch in last_occur and last_occur[ch] >= left:
                left = last_occur[ch] + 1
            # 更新当前字符的最新索引
            last_occur[ch] = right
            # 更新最大长度
            max_len = max(max_len, right - left + 1)

        return max_len


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max = 0
        windows = []
        for i in range(len(s)):
            index = self._get_index(s[i], windows)
            if index != -1:
                max = max if len(windows) < max else len(windows)
                windows = windows[index + 1 :] + [s[i]]
            else:
                windows.append(s[i])
        max = max if len(windows) < max else len(windows)
        return max

    def _get_index(self, char: str, windows: list):

        for i in range(len(windows)):
            if windows[i] == char:
                return i
        return -1


if __name__ == "__main__":
    s = Solution()
    print(s.lengthOfLongestSubstring("dvdf"))
