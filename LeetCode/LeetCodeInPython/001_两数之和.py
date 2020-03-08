List = [2, 7, 11, 15]
target = 9

class Solution:
    def twoSum(self, nums, target):
        L = []
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i] + nums[j] == target:
                    L.append(i)
                    L.append(j)
                    return L

s = Solution()
ret = s.twoSum(List, target)
print(ret)