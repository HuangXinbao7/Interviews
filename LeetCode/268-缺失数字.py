'''
给定一个包含 0, 1, 2, ..., n 中 n 个数的序列，找出 0 .. n 中没有出现在序列中的那个数。

示例 1:
输入: [3,0,1]
输出: 2

示例 2:
输入: [9,6,4,2,3,5,7,0,1]
输出: 8

说明:
你的算法应具有线性时间复杂度。你能否仅使用额外常数空间来实现?
'''


class Solution:
    def missingNumber(self, nums):
        """
        :param nums: List[int]
        :return: int
        """
        return sum(set(range(len(nums)+1))) - sum(set(nums))

    # 方法二
    def missingNumber_2(self, nums):
        """
        好像和以前的一道题（只出现一次的数字）有异曲同工之处。
        看了大家的题解，异或操作（^）是一种很好的方式，不用考虑sum越界问题。

        举个例子：
        0 ^ 4 = 4
        4 ^ 4 = 0
        那么，就可以不用求和，直接使用异或运算^进行 抵消，剩下的数字就是缺失的了。

        再举个例子：
        1^1^2^2^3 = 3
        :param nums:
        :return:
        """
        su = len(nums)
        for i in range(len(nums)):
            su ^= nums[i] ^ i       # 对每个索引位置已经对应的值连续异或，最后剩下的出现一次的结尾丢失的数，因为只有这个索引没有对应值
            # su ^= i
        return su


    # 这个方法和方法一差不多，只是没有转成集合，执行效率高，内存消耗少
    def missingNumber_3(self, nums):
        """取一个len(nums)+1 长度的range()并求和
        减去原数组sums的和，剩下的那个数就是丢失的数
        例如
        nums = [3,0,1]
        range(len(nums)+1) = [0,1,2,3]
        多出的2就是答案"""
        return sum(range(len(nums)+1)) - sum(nums)



if __name__ == '__main__':
    sol = Solution()
    L = [9,6,4,2,3,5,7,0,1]
    ret = sol.missingNumber_3(L)
    print(ret)
