'''
判断一个整数是否是回文数。回文数是指正序（从左向右）和倒序（从右向左）读都是一样的整数。

示例 1:
输入: 121
输出: true
示例 2:

输入: -121
输出: false
解释: 从左向右读, 为 -121 。 从右向左读, 为 121- 。因此它不是一个回文数。

示例 3:
输入: 10
输出: false
解释: 从右向左读, 为 01 。因此它不是一个回文数。

进阶:
你能不将整数转为字符串来解决这个问题吗？
'''


class Solution:
    def isPalindrome(self, x):
        """
        :param x:
        :return bool:
        """
        if x < 0:       # 若数值小于0，则返回False
            return False

        str_x = str(x)      # 将非负的数值转为字符串类型
        re_x = str_x[len(str_x)-1::-1]      # 反向切割字符串，保存到 re_x
        if re_x == str_x:       # 比较re_x 是否等于str_x,相等则是回文数，返回True
            return True

        return False


    # 方法二
    def isPalindrome2(self, x):
        """
        :param x:
        :return bool:
        """
        reverse = str(x)[::-1]
        return reverse == str(x)


if __name__ == '__main__':
    sol = Solution()
    ret = sol.isPalindrome(10)
    print(ret)
