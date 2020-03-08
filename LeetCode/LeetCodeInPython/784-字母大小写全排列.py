'''
给定一个字符串S，通过将字符串S中的每个字母转变大小写，我们可以获得一个新的字符串。返回所有可能得到的字符串集合。

示例:
输入: S = "a1b2"
输出: ["a1b2", "a1B2", "A1b2", "A1B2"]

输入: S = "3z4"
输出: ["3z4", "3Z4"]

输入: S = "12345"
输出: ["12345"]
注意：

S 的长度不超过12。
S 仅由数字和字母组成。
'''


class Solution:
    def letterCasePermutation(self, S):
        """
        :param S:
        :return:
        """
        res = []
        self.dfs("", S, res, 0)
        return res

    def dfs(self, pre, s, res, index):
        if index == len(s):
            res.append(pre)
        else:
            ch = s[index]
            if str.isdigit(ch):
                self.dfs(pre+ch, s, res, index+1)
            else:
                ch = str.lower(ch)
                self.dfs(pre+ch, s, res, index+1)

                ch = str.upper(ch)
                self.dfs(pre+ch, s, res, index+1)


    # 方法二，利用列表解析和递归
    def letterCasePermutation_2(self, S):
        if not S: return [S]
        rest = self.letterCasePermutation(S[1:])        # 递归
        if S[0].isalpha():
            return [S[0].lower() + s for s in rest] + [S[0].upper() + s for s in rest]      # 列表解析
        return [S[0] + s for s in rest]


if __name__ == '__main__':
    sol = Solution()
    # S = 'a1b2'
    S = 'ab'
    ret = sol.letterCasePermutation_2(S)
    print(ret)
