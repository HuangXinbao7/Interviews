"""

"""
class Solution:
    def canPermutePalindrome(self, s):
        """
        :param s: str
        :return: bool
        """
        m = len(s)
        n = len({*s})

        if len(s) <= 1:
            return True
        elif m == n:
            return False
        else:
            return m <= 2*n + 1