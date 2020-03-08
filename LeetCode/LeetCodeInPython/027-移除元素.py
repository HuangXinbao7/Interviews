class Solution:
    def removeElement(self, nums, val):
        L = nums
        for i in L:
            if i == val:
                nums.remove(val)
        print(nums)
        return len(nums)


if __name__ == '__main__':
    sol = Solution()
    L = [1,1,2,2,3,3]
    val = 2

    ret = sol.removeElement(L, val)
    print(ret)
