'''
给定一个包含 n + 1 个整数的数组 nums，其数字都在 1 到 n 之间（包括 1 和 n），可知至少存在一个重复的整数。假设只有一个重复的整数，找出这个重复的数。

示例 1:
输入: [1,3,4,2,2]
输出: 2

示例 2:
输入: [3,1,3,4,2]
输出: 3

说明：
不能更改原数组（假设数组是只读的）。
只能使用额外的 O(1) 的空间。
时间复杂度小于 O(n2) 。
数组中只有一个重复的数字，但它可能不止重复出现一次。
'''


class Solution:
    def findDuplicate(self, nums):
        """
        :param nums: List[int]
        :return: int
        """
        # su = sum(nums) - sum(set(nums))
        return (sum(nums) - sum(set(nums))) // (len(nums) - len(set(nums)))


    # 方法二，二分法, 这个方法还没弄明白
    def findDuplicate_2(self, nums):
        """使用二分法 我们在下标区间[0, n]中搜索，首先求出中点mid
        然后遍历整个数组，统计所有小于等于mid的数的个数，如果个数小于等于mid，则说明重复值在[mid+1, n]之间，
        反之，重复值应在[1, mid-1]之间，然后依次类推，直到搜索完成，此时的right就是我们要求的重复值。"""
        # if not nums or len(nums) == 0:
        #     return 0
        # left = 0
        # right = len(nums)-1
        # while left < right:
        #     mid = left + (right-left)//2
        #     count = 0
        #     for i in nums:
        #         if nums[i] < nums[mid]:
        #             count += 1
        #     if count <= mid:
        #         left = mid +1
        #     else:
        #         right = mid
        # return right

        left = 1
        right = len(nums)
        while left < right:
            mid = int(left + (right - left) / 2)
            cnt = 0
            for num in nums:
                if num <= mid:
                    cnt += 1
            if cnt <= mid:
                left = mid + 1
            else:
                right = mid
        return right


    # 方法三，使用排序异或, 内存开销比方法一的小
    def findDuplicate_3(self, nums):
        s = sorted(nums)
        for i in range(len(s)-1):
            if not s[i]^s[i+1]:
                return s[i+1]


    # 方法四，使用排序
    def findDuplicate_4(self, nums):
        s = sorted(nums)
        for i in range(len(nums)):
            if nums[i-1] == nums[i]:     # 相邻的两个数相等，即为重复值
                return nums[i]


    # 方法五, 看不大懂
    def findDuplicate_5(self, nums):
        for i in range(len(nums)):
            while (nums[i] != i):
                if nums[i] == nums[nums[i]]:
                    return nums[i]
                else:
                    # tmp = nums[i]
                    # nums[i] = nums[tmp]
                    # nums[tmp] = tmp
                    nums[i], nums[nums[i]] = nums[nums[i]], nums[i]


if __name__ == '__main__':
    sol = Solution()
    L = [1, 3, 4, 2, 2]
    ret = sol.findDuplicate_2(L)
    print(ret)