"""
给定两个排序后的数组 A 和 B，其中 A 的末端有足够的缓冲空间容纳 B。 编写一个方法，将 B 合并入 A 并排序。
初始化 A 和 B 的元素数量分别为 m 和 n。

示例:
输入:
A = [1,2,3,0,0,0], m = 3
B = [2,5,6],       n = 3

输出: [1,2,2,3,5,6]

思路：
    最直观的方法是先将数组 B 放进数组 A 的尾部，然后直接对整个数组进行排序。
"""
class Solution:
    def merge(self, A, m, B, n):
        """
        不返回任何内容，而是修改一个位置。
        :param A: List[int]
        :param m: int
        :param B: List[int]
        :param n: int
        :return: None
        """
        A[m:] = B
        A.sort()


if __name__ == "__main__":
    A = [1, 2, 3, 0, 0, 0]
    B = [2, 5, 6]

    Sol = Solution()
    res = Sol.merge(A, 3, B, 3)
    print(res)
