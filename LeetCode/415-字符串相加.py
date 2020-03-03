'''
给定两个字符串形式的非负整数 num1 和num2 ，计算它们的和。

注意：
num1 和num2 的长度都小于 5100.
num1 和num2 都只包含数字 0-9.
num1 和num2 都不包含任何前导零。

你不能使用任何內建 BigInteger 库， 也不能直接将输入的字符串转换为整数形式。
'''


class Solution:
    def addStrings(self, n1, n2):
        carry = 0
        ret = []
        r = ''
        while n1 and n2:
            tmp = int(n1[-1]) + int(n2[-1]) + carry
            carry, val = divmod(tmp, 10)
            ret.append(val)
            n1 = n1[:-1]
            n2 = n2[:-1]
        while n1:
            tmp = int(n1[-1]) + carry
            carry, val = divmod(tmp, 10)
            ret.append(val)
            n1 = n1[:-1]
        while n2:
            tmp  = int(n2[-1]) + carry
            carry, val = divmod(tmp, 10)
            ret.append(val)
            n2 = n2[:-1]

        if carry:
            ret.append(1)

        while ret:
            r += str(ret[-1])
            ret = ret[:-1]

        return r


if __name__ == '__main__':
    sol = Solution()
    # num1 = '12345'
    # num2 = '456'
    num1 = '98'
    num2 = '9'
    ret = sol.addStrings(num1, num2)
    print(ret)


