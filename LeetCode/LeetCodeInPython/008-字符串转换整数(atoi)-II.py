"""
方法二：使用正则
"""
import re
class Solution:
    def myAtoi(self, str):
        return max(min(int(*re.findall('^[+-]?\d+', str.lstrip())), 2**31-1), -2**31)


if __name__ == '__main__':
    # str = '42'
    str = '    -42'
    # str = '4193 with words'
    # str = 'words and 987 '
    # str = '-91283472332'
    # str = ''
    # str = "+-2"
    # str = "-+2"

    Sol = Solution()
    res = Sol.myAtoi(str)
    print(res)
