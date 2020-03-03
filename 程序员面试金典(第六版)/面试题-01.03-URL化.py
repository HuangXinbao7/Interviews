"""
思路：
    先根据字符串的真实长度切割字符串，将真实字符串后面多余的空格去除，并转换成字符列表
    遍历字符列表，如果是空字符，则用'%20'字符串替换
    最后将这里遍历后的字符列表拼接成一个字符串并返回
"""
class Solution:
    def replaceSpaces(self, S, length):
        """
        :param S: str
        :param length: int
        :return: str
        """
        tmp = list(S[:length])
        for i in range(len(tmp)):
            if tmp[i] == ' ':
                tmp[i] = '%20'
        return ''.join(tmp)


if __name__ == "__main__":
    # S = "Mr John Smith    "
    S = "               "

    Sol = Solution()
    res = Sol.replaceSpaces(S, 5)
    print(res)