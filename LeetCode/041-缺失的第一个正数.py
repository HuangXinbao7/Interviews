
class Solution:
    def firstMissingPositive(self, nums):
        if not nums: return 1
        if len(nums) == 1:
            if nums[0] == 1: return 2
            else: return 1

        for i in range(1, max(nums)+2):
            if i not in nums:
                return i


if __name__ == '__main__':
    sol = Solution()
    # L = [7,8,9,11,12]
    # L = [3,4,-1,1]
    # L = [1,2,3,4,5]
    # L = [1,2,0]
    # L = []
    # L = [-5]
    # L = [3]
    # L = [3,4,-1,1]
    L = [7,8,9,11,12]
    ret = sol.firstMissingPositive(L)
    print(ret)