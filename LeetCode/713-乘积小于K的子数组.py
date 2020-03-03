"""

"""
from functools import reduce
from operator import mul


class Solution:
    def numSubarrayProductLessThanK(self, nums, k):
        """
        :param nums: List[int]
        :param k: int
        :return: int
        """
        count = 0
        m = len(nums)

        for i in range(m):
            j = i + 1
            while j <= m:
                temp = nums[i:j]
                if reduce(mul, temp, 1) < k:
                    print(temp)
                    j += 1
                    count += 1
                else:
                    break
        return count


if __name__ == '__main__':
    nums = [10, 5, 2, 6, 7, 8]
    k = 1000

    Sol = Solution()
    res = Sol.numSubarrayProductLessThanK(nums, k)
    print(res)