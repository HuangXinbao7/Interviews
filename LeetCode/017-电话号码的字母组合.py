'''
给定一个仅包含数字 2-9 的字符串，返回所有它能表示的字母组合。
给出数字到字母的映射如下（与电话按键相同）。注意 1 不对应任何字母。

示例:
输入："23"
输出：["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
说明: 尽管上面的答案是按字典序排列的，但是你可以任意选择答案输出的顺序。
'''
class Solution:
    def letterCombinations(self, digits):
        """
        :param digits: str
        :return: list
        """
        numDic = {
            2: ['a', 'b', 'c'],
            3: ['d', 'e', 'f'],
            4: ['g', 'h', 'i'],
            5: ['j', 'k', 'l'],
            6: ['m', 'n', 'o'],
            7: ['p', 'q', 'r', 's'],
            8: ['t', 'u', 'v'],
            9: ['w', 'x', 'y', 'z']
        }
        from functools import reduce
        L = []

        # 当输入为空时，返回一个空列表
        if digits == '':
            return []

        # 定义一个一次处理两个列表的组合关系的函数
        def myfunc(list1, list2):
            return [str(i)+str(j) for i in list1 for j in list2]

        # 获取每个数字字符对应的列表
        for d in digits:
            if int(d) in numDic.keys():
                L.append(numDic[int(d)])
        print(L)

        # 使用 reduce 函数累计的处理列表
        return reduce(myfunc, L)


if __name__ == '__main__':
    # digits = ''
    digits = '234'

    sol = Solution()
    ret = sol.letterCombinations(digits)
    print(ret)
