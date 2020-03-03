'''
给定一个由整数组成的非空数组所表示的非负整数，在该数的基础上加一。

最高位数字存放在数组的首位， 数组中每个元素只存储一个数字。

你可以假设除了整数 0 之外，这个整数不会以零开头。

示例 1:
输入: [1,2,3]
输出: [1,2,4]
解释: 输入数组表示数字 123。

示例 2:
输入: [4,3,2,1]
输出: [4,3,2,2]
解释: 输入数组表示数字 4321。
'''

class Solution:
    def plusOne(self, digits):
        """方法一"""
        ret = []

        if digits[-1] + 1 < 10:         # 如果加上1不产生进位，则直接返回结果
            digits[-1] = digits[-1] + 1
            return digits
        else:                           # 这里是产生进位的情况
            carry = 1
            ret.append(0)               # 处理最后一个产生进位的数
            digits = digits[:-1]        # 对列表切片，去掉最后一个数字元素
            while digits:               # 对剩下的数据用while循环
                if digits[-1] + carry == 10:
                    ret.append(0)
                    carry = 1
                else:
                    ret.append(digits[-1]+carry)
                    carry = 0
                digits = digits[:-1]
            if carry == 1:              # 最后处理进位
                ret.append(1)
            ret.reverse()               # 将列表反转，就是结果
            return ret

    def plusOne_2(self, d):
        """方法二
        思路：
        把需要加的数字1当成前一个数字位传过来的进位，这样就把数字1和进位统一处理
        逆序的处理数组
        使用求商取余，求得的商为进位，余数为要保存的当前值
        最后检测进位是否为1，是1则进位
        """
        carry = 1
        for i in range(len(d)-1, -1, -1):       # 从最后一个数字开始处理
            tmp = d[i] + carry                  # 把当前位置上的数字加上进位数carry，保存到一个tmp变量中
            # carry, d[i] = tmp // 10, tmp % 10   # 把余数写入当前位置，商作为进位存入carry
            carry, d[i] = divmod(tmp, 10)       # 使用求商取余函数
        if carry:       # 最后判断进位数是否等于1，等于则插入数组最前位置
            d.insert(0, carry)
        return d

    def plusOne_3(self,d):
        """方法三：只用一行代码实现
        思路步骤：
        例子，对[1,2,3] 进行加1
        1、str(d)                                                                现将数组列表转为字符串     [1,2,3] --> "[1,2,3]"
        2、str(d)[1:-1]                                                          去掉两端的中括号字符      "[1,2,3]" --> "1,2,3"
        3、str(d)[1:-1].replace(',', '').replace(' ', ''))                       用空字符替换逗号分隔符，再用空字符过滤空格 "1,2,3" --> "123"
        4、int(str(d)[1:-1].replace(',', '').replace(' ', '')) + 1               转成整形数值后加1 "123" --> 123 --> 123 + 1 = 124
        5、str(int(str(d)[1:-1].replace(',', '').replace(' ', '')) + 1)                      将结果转回字符串 124 --> "124"
        6、[int(i) for i in str(int(str(d)[1:-1].replace(',', '').replace(' ', '')) + 1)]    使用列表解析，将字符串转成数组形式 "124" --> [1,2,4]
        """
        return [int(i) for i in str(int(str(d)[1:-1].replace(',', '').replace(' ', '')) + 1)]




if __name__ == '__main__':
    sol = Solution()
    # d = [1,2,3,9,8]
    d = [1,2,3]
    ret = sol.plusOne_3(d)
    print(ret)
