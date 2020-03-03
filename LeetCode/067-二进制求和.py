'''
给定两个二进制字符串，返回他们的和（用二进制表示）。

输入为非空字符串且只包含数字 1 和 0。

示例 1:
输入: a = "11", b = "1"
输出: "100"

示例 2:
输入: a = "1010", b = "1011"
输出: "10101"
'''


class Solution:
    def addBinary(self, a, b):
        # a = list(a)
        # b = list(b)
        c = []
        ret = ''
        carry = 0

        while a and b:
            if int(a[-1]) + int(b[-1]) + carry == 0:
                c.append(0)
                carry = 0
            elif int(a[-1]) + int(b[-1]) + carry == 1:
                c.append(1)
                carry = 0
            elif int(a[-1]) + int(b[-1]) + carry == 2:
                c.append(0)
                carry = 1
            elif int(a[-1]) + int(b[-1]) + carry == 3:
                c.append(1)
                carry = 1
            a = a[:-1]
            b = b[:-1]

        while a:
            if int(a[-1]) + carry == 0:
                c.append(0)
                carry = 0
            elif int(a[-1]) + carry == 1:
                c.append(1)
                carry = 0
            elif int(a[-1]) + carry == 2:
                c.append(0)
                carry = 1
            a = a[:-1]

        while b:
            if int(b[-1]) + carry == 0:
                c.append(0)
                carry = 0
            elif int(b[-1]) + carry == 1:
                c.append(1)
                carry = 0
            elif int(b[-1]) + carry == 2:
                c.append(0)
                carry = 1
            b = b[:-1]

        if carry == 1:
            c.append(1)

        while c:
            ret += str(c[-1])
            c = c[:-1]

        return ret


if __name__ == '__main__':
    sol = Solution()
    # a = '1010'
    # b = '1011'
    a = '1111'
    b = '0001'
    ret = sol.addBinary(a, b)
    print(ret)
