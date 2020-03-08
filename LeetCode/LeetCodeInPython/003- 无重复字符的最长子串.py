'''
给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度。

示例 1:
输入: "abcabcbb"
输出: 3
解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。

示例 2:
输入: "bbbbb"
输出: 1
解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。

示例 3:
输入: "pwwkew"
输出: 3
解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。
     请注意，你的答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串。

'''


class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :param s: str
        :return: int
        """
        if len(s)==0: return 0
        if len(s)==1: return 1

        longestSubstring = ""
        for i in range(len(s)):
            subString = s[i]
            for j in s[i+1:]:
                if j in subString:
                    break
                # elif j not in subString:
                subString += j

            if len(subString)>len(longestSubstring):
                longestSubstring = subString

        return len(longestSubstring)


    def lengthOfLongestSubstring_2(self, s):
        st = {}
        i, ans = 0, 0
        for j in range(len(s)):
            if s[j] in st:              # 当前索引位置上的字符
                i = max(st[s[j]], i)
            ans = max(ans, j - i + 1)
            st[s[j]] = j + 1
        return ans


if __name__ == '__main__':
    sol = Solution()
    # s = "abcabcbb"
    # s = " "       # 长度为1的空字符串
    # s = ""          # 长度为0的空字符串
    s = "au"
    ret = sol.lengthOfLongestSubstring(s)
    print(ret)