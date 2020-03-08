'''
罗马数字包含以下七种字符: I， V， X， L，C，D 和 M。

字符          数值
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
例如， 罗马数字 2 写做 II ，12 写做 XII ，即为 X + II 。 27 写做  XXVII, 即为 XX + V + II 。

通常情况下，罗马数字中小的数字在大的数字的右边。
但也存在特例，例如 4 不写做 IIII，而是 IV。数字 1 在数字 5 的左边，所表示的数等于大数 5 减小数 1 得到的数值 4 。
同样地，数字 9 表示为 IX。这个特殊的规则只适用于以下六种情况：

I 可以放在 V (5) 和 X (10) 的左边，来表示 4 和 9。
X 可以放在 L (50) 和 C (100) 的左边，来表示 40 和 90。
C 可以放在 D (500) 和 M (1000) 的左边，来表示 400 和 900。

给定一个罗马数字，将其转换成整数。输入确保在 1 到 3999 的范围内。

示例 1:
输入: "III"
输出: 3

示例 2:
输入: "IV"
输出: 4

示例 3:
输入: "IX"
输出: 9

示例 4:
输入: "LVIII"
输出: 58
解释: L = 50, V= 5, III = 3.

示例 5:
输入: "MCMXCIV"
输出: 1994
解释: M = 1000, CM = 900, XC = 90, IV = 4.
'''


class Solution:
    def romanToInt(self, s):
        """
        :param s:
        :return int:
        """
        roman_Num_dic = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        roman_Spe_dic = {'IV': 4, 'IX': 9, 'XL': 40, 'XC': 90, 'CD': 400, 'CM': 900}        # 特殊的规则
        toInt = 0

        while s:
            if s[:2] in roman_Spe_dic:          # 取前两位字符串，判断是否符合特殊规则
                toInt += roman_Spe_dic[s[:2]]   # 符合特殊规则，计算其数值
                s = s[2:]                       # 切割字符串，用剩下未计算的字符串进入下一个循环
            else:                               # 若不符合特殊规则，则取第一个字符，转为整数
                toInt += roman_Num_dic[s[:1]]   # 取第一个字符，转为整数
                s = s[1:]

        return toInt

    # 方法二, 比较高效
    def romanToInt_2(self, s):
        roman_Num_dic = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        res = 0

        for i in range(len(s)):
            # 当第i个字符不是最后的字符，且对应的整数小于后面的字符对应的整数，则用总数减去它
            if i < len(s) - 1 and roman_Num_dic[s[i]] < roman_Num_dic[s[i+1]]:
                res -= roman_Num_dic[s[i]]
            else:
                res += roman_Num_dic[s[i]]
        return res


if __name__ == '__main__':
    sol = Solution()
    # 测试用例
    # s = 'MCMXCIV'
    s = 'XCIV'
    ret = sol.romanToInt_2(s)
    print(ret)


