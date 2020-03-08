'''
给定一个非负整数 numRows，生成杨辉三角的前 numRows 行。

在杨辉三角中，每个数是它左上方和右上方的数的和。

示例:

输入: 5
输出:
[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]

'''
import time

class Solution:
    def generate(self, numRows):
        """
        :param numRows: int
        :return: List[List[int]]
        """
        List = [[1], [1,1]]

        if numRows == 0:
            return []
        elif numRows == 1:
            return [[1]]
        elif numRows == 2:
            return List

        for i in range(3, numRows+1):
            L = [0 for x in range(i)]

            L[0] = L[-1] = 1

            tmp = L[1:-1]
            for j in range(len(tmp)):
                L[j+1] = List[-1][j]+List[-1][j+1]

            List.append(L)
        return List

    def generate_2(self, numRows):
        """方法二"""
        # 创建初始对象，并赋值
        List = [[1]*i for i in range(1, numRows+1)]

        # 从第三行元素开始更新
        for i in range(2, numRows):
            # 每次更新第2个元素~倒数第2个元素
            for j in range(1, i):
                # 更新内容
                List[i][j] = List[i-1][j-1] + List[i-1][j]
        return List


if __name__ == '__main__':
    sol = Solution()
    ret = sol.generate_2(5)
    print(ret)
