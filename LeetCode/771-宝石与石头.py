'''
给定字符串J 代表石头中宝石的类型，和字符串 S代表你拥有的石头。 S 中每个字符代表了一种你拥有的石头的类型，你想知道你拥有的石头中有多少是宝石。

J 中的字母不重复，J 和 S中的所有字符都是字母。字母区分大小写，因此"a"和"A"是不同类型的石头。

示例 1:
输入: J = "aA", S = "aAAbbbb"
输出: 3

示例 2:
输入: J = "z", S = "ZZ"
输出: 0

注意:
S 和 J 最多含有50个字母。
J 中的字符不重复。
'''


class Solution:
    def numJewelsInStones(self, J, S):
        count = 0

        if not J or not S:
            return 'J 或 S 为空'

        if len(J) != len(set(J)):
            return 'J 非法'

        if len(J) > 50 or len(S) > 50:
            return 'J 或 S 长度超出范围'

        for i in J:
            for j in S:
                if i == j:
                    count += 1
        return count

    # 方法二
    def numJewelsInStones_2(self, J, S):
        """这个方法很牛逼啊"""
        return sum(S.count(i) for i in J)

    # 方法三
    def numJewelsInStones_3(self, J, S):
        """利用列表解析"""
        return len([i for i in S if i in J])


if __name__ == '__main__':
    sol = Solution()
    # j = ''        # J 或 S 为空
    # s = 'a'

    # j = 'aa'        # J 非法
    # s = 'fasdf'

    j = 'aA'
    s = 'abcABCaa'
    ret = sol.numJewelsInStones_2(j,s)
    print(ret)
