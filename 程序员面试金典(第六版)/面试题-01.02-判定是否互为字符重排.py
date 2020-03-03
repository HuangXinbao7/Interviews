"""
题目链接：https://leetcode-cn.com/problems/check-permutation-lcci/

思路1：
    首先判断s1和s2的长度是否相等，如果不相等，则不可能互为重排
    如果长度相等：
        那么s1和s2中能找到一一对应的字符，且重复的字符个数也相同
        利用集合去重后，s1和s2中的字符必须相同，即两个集合想减为空集合

思路2：
    直接利用Python内置函数sorted对s1和s2进行排序，再比较排序后的两个字符串是否相等。
    return sorted(s1) == sorted(s2)

"""
class Solution:
    def CheckPermutation(self, s1: str, s2: str) -> bool:
        """
        :param s1: str
        :param s2: str
        :return: bool
        """
        # 另一个思路，先排序，再判断是否相等
        # return sorted(s1) == sorted(s2)

        return len({*s1}) - len({*s2}) == 0


if __name__ == "__main__":
    s1 = 'leetcode'
    s2 = 'codeleet'

    Sol = Solution()
    res = Sol.CheckPermutation(s1, s2)
    print(res)