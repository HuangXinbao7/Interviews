"""
题目链接 https://leetcode-cn.com/problems/is-unique-lcci/

思路：
    将输入的字符串转成集合形式，利用集合中的元素不重复的特性，过滤掉字符串中可能存在的重复字符
    通过比较原输入字符串的长度和生成的集合的长度：
        如果相等，则原字符串是字符唯一的，否则不唯一

    注意：空字符串的输入("")，应该判断为字符唯一，即函数返回 True
"""
class Solution:
    def isUnique(self, astr):
        """
        :param astr: str
        :return: bool
        """
        # m = len(astr)
        # if m > 100:
        #     return False
        #
        # astr = set([item for item in astr])
        # return True if m == len(astr) else False

        # 思路二，简洁的代码
        return len({*astr}) == len(astr)


if __name__ == "__main__":
    # s = 'leetcode'
    s = 'abcdefg'

    Sol = Solution()
    res = Sol.isUnique(s)
    print(res)