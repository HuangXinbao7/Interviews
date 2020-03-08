'''
给出一个 32 位的有符号整数，你需要将这个整数中每位上的数字进行反转。

示例 1:
输入: 123
输出: 321

示例 2:
输入: -123
输出: -321

示例 3:
输入: 120
输出: 21

注意:
假设我们的环境只能存储得下 32 位的有符号整数，则其数值范围为 [−231,  231 − 1]。请根据这个假设，如果反转后整数溢出那么就返回 0。
'''

class Solution:
    def reverse(self, x):
        scope = [-2 ** 31, 2 ** 31 - 1]     # 数值范围
        signs = 1     # 有符号整数的标记
        res = ''     # 保存反转后的字符串
        # ret = 0     # 最后返回的结果

        # 若整数x为负数，则把符号标记设为 -1，并将x转为正整数，用于while循环
        if x < 0:
            signs = -1          # 修改符号标记
            x = signs * x       # 转为整数

        # 若整数x等于0，则转为字符串形式后直接返回
        if x == 0:
            res = res + str(x)
            ret = int(res)
            return ret

        # 对大于0的整数用while 循环处理
        # 每次取出个位数上的数字，拼接到字符串上
        while x:
            x, val = divmod(x, 10)      # 每次循环去掉整数的最后一位数字
            res = res + str(val)

        # 恢复有符号整数的符号
        ret = int(res)          # 从字符串转为整数类型
        if signs == -1:
            ret = ret * signs       # 给原来是负数的整数加上负号

        # 判断最后的数值是否在允许的范围内
        if ret > scope[0] and ret < scope[1]:       # 在范围内，就返回当前数值
            return ret
        else:       # 超出范围，返回 0
            ret = 0

        return ret


    # 方法二
    def reverse_2(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x==0:
            return 0
        str_x = str(x)      # 先将整数转为字符串
        x = ''
        if str_x[0] == '-':     # 先取出整数的符号，放在字符串的第一位
            x += '-'
        x += str_x[len(str_x)-1::-1].lstrip("0").rstrip("-")        # 对字符串进行倒叙切片，并去除首字符 ‘-’ 和整数后边的0
        x = int(x)      # 将字符串类型的数值转回整数类型
        if -2**31<x<2**31-1:        # 判断数值是否在范围内
            return x
        return 0


if __name__ == '__main__':
    sol = Solution()
    ret = sol.reverse(2 ** 31 - 7)
    print(ret)


