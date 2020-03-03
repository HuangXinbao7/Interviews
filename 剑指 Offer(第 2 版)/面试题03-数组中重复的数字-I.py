"""
思路一：
    先排序，排序后重复的数字就会连在一起
    遍历数组，用当前遍历的数字和其后面的数字比较，相等则找到了重复的数字
"""
class Solution:
    def findRepeatNumber(self, nums):
        # sorted() 返回排序后的新数组，不改变原数组
        nums = sorted(nums)

        for i in range(len(nums)):
            if nums[i] == nums[i+1]:
                return nums[i]


if __name__ == '__main__':
    # nums = [0, 1, 2, 3, 4, 11, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
    nums = [2, 3, 1, 0, 2, 5, 3]

    Sol = Solution()
    res = Sol.findRepeatNumber(nums)

    print(res)
