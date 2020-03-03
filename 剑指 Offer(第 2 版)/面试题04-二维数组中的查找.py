'''
注意：本题与LeetCode主站 240 题相同：https://leetcode-cn.com/problems/search-a-2d-matrix-ii/

本题链接：https://leetcode-cn.com/problems/er-wei-shu-zu-zhong-de-cha-zhao-lcof/

思路：二分查找
遍历每一行，对每一行进行二分查找
初始化，left = 第一个元素下标，right = 最后一个元素下标，middle = (left + right)//2
    如果 matrix[i][middle] = target, 则找到
    如果 matrix[i][middle] < target, 说明 target 不可能存在于数组的左半边，left = middle + 1
    如果 matrix[i][middle] > target, 说明 target 不可能存在于数组的右半边，right = middle -1
'''
class Solution:
    def findNumberIn2DArray(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        m = len(matrix)
        if m == 0:
            return False
        n = len(matrix[0])
        if n == 0:
            return False

        i = 0
        while i < m:
            left = 0
            right = n - 1
            while left <= right:
                middle = (left + right) // 2
                if matrix[i][middle] == target:
                    return True
                elif matrix[i][middle] < target:
                    left = middle + 1
                else:
                    right = middle - 1
            # 遍历下一行
            i = i + 1
        return False


if __name__ == "__main__":
    matrix = [
        [1,   4,  7, 11, 15],
        [2,   5,  8, 12, 19],
        [3,   6,  9, 16, 22],
        [10, 13, 14, 17, 24],
        [18, 21, 23, 26, 30]
    ]

    target = 5

    s = Solution()
    res = s.findNumberIn2DArray(matrix, target)
    print(res)