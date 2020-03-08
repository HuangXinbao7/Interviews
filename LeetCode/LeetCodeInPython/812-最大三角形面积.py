'''
给定包含多个点的集合，从其中取三个点组成三角形，返回能组成的最大三角形的面积。

示例:
输入: points = [[0,0],[0,1],[1,0],[0,2],[2,0]]
输出: 2
解释:
这五个点如下图所示。组成的橙色三角形是最大的，面积为2。


注意:
3 <= points.length <= 50.
不存在重复的点。
-50 <= points[i][j] <= 50.
结果误差值在 10^-6 以内都认为是正确答案。
'''

'''
已知三点求三角形面积可以用矩阵求 化简公式得 S=(x1y2+x2y3+x3y1-x1y3-x2y1-x3y2) /2
'''


class Solution:
    def largestTriangleArea(self, points):
        """
        :param points: List[List[int]]
        :return: float
        """
        maxArea = 0
        x_axis = []
        y_axis = []
        for p in points:
            if p[1] == 0:
                x_axis.append(p[0])
            if p[0] == 0:
                y_axis.append(p[1])

        maxArea_x = (max(x_axis)-min(x_axis)) * max(y_axis) / 2
        maxArea_y = (max(y_axis)-min(y_axis)) * max(x_axis) / 2
        return max(maxArea_x, maxArea_y)


    #
    def largestTriangleArea_2(self, points):
        from itertools import combinations
        amax = 0
        for i in combinations(points, 3):
            x = [i[0][0], i[1][0], i[2][0]]
            y = [i[0][1], i[1][1], i[2][1]]
            s = abs((x[0] - x[2]) * (y[1] - y[2]) - (x[1] - x[2]) * (y[0] - y[2])) / 2
            amax = max(s, amax)
        return amax






if __name__ == '__main__':
    sol = Solution()
    # points = [[0, 0], [0, 1], [1, 0], [0, 2], [2, 0]]
    points = [[4, 6], [6, 5], [3, 1]]
    ret = sol.largestTriangleArea(points)
    print(ret)