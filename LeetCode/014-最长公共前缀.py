'''
编写一个函数来查找字符串数组中的最长公共前缀。

如果不存在公共前缀，返回空字符串 ""。

示例 1:
输入: ["flower","flow","flight"]
输出: "fl"

示例 2:
输入: ["dog","racecar","car"]
输出: ""
解释: 输入不存在公共前缀。

说明:
所有输入只包含小写字母 a-z 。
'''


class Solution:
    def longestCommonPrefix(self, strs):
        """
        这个方法提交了很多次才成功，这个方法效率应该不高
        :param strs List[str]:
        :return str:
        """
        if len(strs) == 0:      # 判断输入，如果为空，则返回
            return ""
        if len(strs) == 1:      # 判断输入，如果只有一个字符串，则返回这个字符串
            return strs[0]

        lm = len(strs[0])       # 取字符串数组中的第一个字符的长度
        eq = False              #
        res = ''                # 最后返回的前缀字符串

        for i in strs:
            if i == '':         # 如果有任意一个字符串为空，则返回 res
                return res
            lm = min(lm, len(i))        # 这里取所有字符串中最短的字符串长度，在循环中使用

        for i in range(lm):     # 循环最大次数为最短字符串长度，避免字符串下标越界
            for j in strs[1:]:      # 从第二个字符串开始对比
                if strs[0][i] == j[i]:      # 对比字符串中的相同下标的字符
                    eq = True
                else:
                    eq = False
                    break
            if eq == True:
                res += strs[0][i]       # 将相同的字符加入前缀字符串中
            else:
                break
        return res

    # 方法二
    def longestCommonPrefix_2(self, strs):
        """
        利用python的max()和min()，在Python里字符串是可以比较的，
        按照ascII值排，举例abb， aba，abac，最大为abb，最小为aba。
        所以只需要比较最大最小的公共前缀就是整个数组的公共前缀"""
        if not strs: return ""
        s1 = min(strs)
        s2 = max(strs)
        for i, x in enumerate(s1):
            if x != s2[i]:
                return s2[:i]
        return s1

    # 方法三
    def longestCommonPrefix_3(self, strs):
        """
        利用python的zip函数，
        把str看成list然后把输入看成二维数组，左对齐纵向压缩，
        然后把每项利用集合去重，之后遍历list中找到元素长度大于1之前的就是公共前缀
        :param strs:
        :return:
        """
        if not strs: return ""
        ss = list(map(set, zip(*strs)))     #
        res = ''
        for i, x in enumerate(ss):
            print(i, x)
            x = list(x)
            if len(x) > 1:
                break
            res = res + x[0]
        return res


if __name__ == '__main__':
    sol = Solution()
    # List = ["flower","flow","flight"]
    # List = ["c", "acc", "ccc"]
    # List = ["aca", "acba"]
    List = ["abab", "abaf", "abac"]
    # List = []
    ret = sol.longestCommonPrefix_3(List)
    print(ret)
