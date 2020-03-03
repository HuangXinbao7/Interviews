"""
思路二：
    设置一个集合类型的抽屉
    遍历数组，并判断当前遍历到的数字是否已经存在于抽屉中：
        如果存在，则说明前面的遍历过程中已经遇到相同的数字，即重复的数字找到了
        如果不存在，则将当前的数字添加到抽屉中，继续遍历
"""
class Solution:
    def findRepeatNumber(self, nums):
        drawer = set()
        for num in nums:
            if num in drawer:
                return num
            drawer.add(num)


if __name__ == '__main__':
    # nums = [2, 3, 1, 0, 2, 5, 3]
    # nums = [0, 1, 2, 3, 4, 11, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
    nums = [1,2,3,4,5,3]

    Sol = Solution()
    res = Sol.findRepeatNumber(nums)

    print(res)
