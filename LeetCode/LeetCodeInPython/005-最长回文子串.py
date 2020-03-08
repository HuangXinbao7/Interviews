'''
给定一个字符串 s，找到 s 中最长的回文子串。你可以假设 s 的最大长度为 1000。

示例 1：

输入: "babad"
输出: "bab"
注意: "aba" 也是一个有效答案。
示例 2：

输入: "cbbd"
输出: "bb"

'''


class Solution:
    def longestPalindrome(self, s: str) -> str:
        """
        :param s: str
        :return: str
        """
        for i in range(len(s)):
            for j in range(i+1, len(s)):
                if s[i] == s[j]:
                    tmp = s[i:j+1]
                    for k in range(1, len(tmp)//2):
                        if tmp[k]!=tmp[-k]:
                            break
                    print(i, j, tmp)



        return s


if __name__ == "__main__":
    sol = Solution()
    # s = "babad"
    # s = ""
    s = "abcca"
    ret = sol.longestPalindrome(s)
    print(ret)

