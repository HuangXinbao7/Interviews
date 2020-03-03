'''
罗马数字包含以下七种字符： I， V， X， L，C，D 和 M。

字符          数值
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
例如， 罗马数字 2 写做 II ，即为两个并列的 I。12 写做 XII ，即为 X + II 。 27 写做  XXVII, 即为 XX + V + II 。

通常情况下，罗马数字中小的数字在大的数字的右边。
但也存在特例，例如 4 不写做 IIII，而是 IV。数字 1 在数字 5 的左边，所表示的数等于大数 5 减小数 1 得到的数值 4 。
同样地，数字 9 表示为 IX。这个特殊的规则只适用于以下六种情况：

I 可以放在 V (5) 和 X (10) 的左边，来表示 4 和 9。
X 可以放在 L (50) 和 C (100) 的左边，来表示 40 和 90。
C 可以放在 D (500) 和 M (1000) 的左边，来表示 400 和 900。


给定一个整数，将其转为罗马数字。输入确保在 1 到 3999 的范围内。

示例 1:
输入: 3
输出: "III"

示例 2:
输入: 4
输出: "IV"

示例 3:
输入: 9
输出: "IX"

示例 4:
输入: 58
输出: "LVIII"
解释: L = 50, V = 5, III = 3.

示例 5:
输入: 1994
输出: "MCMXCIV"
解释: M = 1000, CM = 900, XC = 90, IV = 4.
'''


class Solution:
    def intToRoman(self, num):
        dic2 = {1:'I', 5: 'V', 10: 'X', 50: 'L', 100: 'C', 500: '500', 1000: 'M'}
        spe_dic2 = {4: 'IV', 9: 'IX', 40: 'XL', 90: 'XC', 400: 'CD', 900: 'CM'}

        res = ''


        if num >= 1000:
            quo, rem = divmod(num, 1000)
            res += dic2[1000] * quo
            num = rem
        if num >= 100:
            quo, rem = divmod(num, 100)
            if quo * 100 in spe_dic2:       # 400 900
                res += spe_dic2[quo*100]
            elif quo > 5:
                res += dic2[500] + dic2[100]*(quo-5)    # 500 600 700 800
            else:
                res += dic2[100]*quo        # 100 200 300
            num = rem
        if num >= 10:
            quo, rem = divmod(num, 10)
            if quo * 10 in spe_dic2:        # 数值为 40 或 90
                res += spe_dic2[quo*10]
                num = rem
            if quo >= 5:
                res += dic2[50]+dic2[10]*(quo-5)        # 50 60 70 80
                num = rem
            else:
                res += dic2[10]*quo     # 10 20 30
            num = rem
        if num in spe_dic2:     # # 判断数字是否为 4 或 9
            res += spe_dic2[num]
        elif num >5:
            res += dic2[5] + dic2[1]*(num-5)        # 数字为 5 6 7 8 中的一个
        else:       # 数字为 1,2,3 中的一个
            res += dic2[1] * num

        return res      # 返回最后的结果


if __name__ == '__main__':
    sol = Solution()
    ret = sol.intToRoman(1994)
    print(ret)
