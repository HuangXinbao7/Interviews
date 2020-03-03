'''
给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串，判断字符串是否有效。

有效字符串需满足：

左括号必须用相同类型的右括号闭合。
左括号必须以正确的顺序闭合。
注意空字符串可被认为是有效字符串。

示例 1:
输入: "()"
输出: true

示例 2:
输入: "()[]{}"
输出: true

示例 3:
输入: "(]"
输出: false

示例 4:
输入: "([)]"
输出: false

示例 5:
输入: "{[]}"
输出: true
'''


class Solution:
    def isValid(self, s):
        L = []
        if not s: return True       # 如果s为空字符串，也算是有效字符串

        for i in s:
            if i == "(": L.append(i)
            if i == "{": L.append(i)
            if i == "[": L.append(i)

            if len(L) == 0: return False        # 如果此时L中没有符号，则返回 False

            if i == ")" and L.pop() != "(": return False        # 如果不匹配，则返回 False
            if i == "}" and L.pop() != "{": return False
            if i == "]" and L.pop() != "[": return False

        return False if L else True     # 最后，如果L中还有没处理完的字符，返回 False


    def isValid_2(self, s):
        """方法二"""
        while '()' in s or '{}' in s or '[]' in s:
            s = s.replace('()', '')
            s = s.replace('{}', '')
            s = s.replace('[]', '')
        return s == ''



if __name__ == '__main__':
    sol = Solution()
    # s = "()[]{}"
    # s = "([)]"
    # s = "){"
    # s = '('
    s = "(]"
    ret = sol.isValid_2(s)
    print(ret)